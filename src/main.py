"""CLI-прототип для анализа зависимостей пакетов (этап 2)."""

import argparse
import os
import sys
from urllib.parse import urlparse

import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

EXIT_OK = 0
EXIT_ERROR = 2
MIN_DEPTH = 1
ALLOWED_MODES = ("real", "test")
PNG_EXT = ".png"
NAME_ALLOWED = set("abcdefghijklmnopqrstuvwxyz"
                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")


def check_package(value):
    """Проверка имени пакета."""
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("Имя пакета пустое.")
    if not set(value).issubset(NAME_ALLOWED):
        raise argparse.ArgumentTypeError(
            f"Недопустимые символы в имени пакета: '{value}'."
        )
    return value


def check_source(value):
    """URL или путь к файлу."""
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("Источник пустой.")
    parsed = urlparse(value)
    if parsed.scheme in ("http", "https") and parsed.netloc:
        return value
    if os.path.exists(value):
        return value
    raise argparse.ArgumentTypeError(
        f"Источник '{value}' не URL и не файл."
    )


def check_mode(value):
    """Режим: real или test."""
    if value not in ALLOWED_MODES:
        raise argparse.ArgumentTypeError(
            f"Режим '{value}' недопустим. Нужно: {', '.join(ALLOWED_MODES)}."
        )
    return value


def check_output(value):
    """Имя файла должно оканчиваться на .png."""
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("Имя файла пустое.")
    if not value.lower().endswith(PNG_EXT):
        raise argparse.ArgumentTypeError(
            f"Файл '{value}' должен оканчиваться на '{PNG_EXT}'."
        )
    return value


def check_depth(value):
    """Целое число >= 1."""
    try:
        depth = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Глубина '{value}' не целое число."
        )
    if depth < MIN_DEPTH:
        raise argparse.ArgumentTypeError(
            f"Глубина должна быть >= {MIN_DEPTH}, получено {depth}."
        )
    return depth


def check_filter(value):
    """Подстрока фильтрации (может быть пустой)."""
    return value.strip()

def get_package_data(package, source, mode):
    """Получение информации о пакете из репозитория."""

    if mode == "real":
        url = f"{source.rstrip('/')}/{package}/json"

        try:
            with urlopen(url, timeout=15) as response:
                data = json.loads(response.read().decode("utf-8"))

        except HTTPError as error:
            raise RuntimeError(
                f"Ошибка HTTP: {error.code}. "
                f"Пакет '{package}' не найден или недоступен."
            ) from error

        except URLError as error:
            raise RuntimeError(
                f"Не удалось подключиться к репозиторию: {error.reason}"
            ) from error

        except json.JSONDecodeError as error:
            raise RuntimeError(
                "Не удалось прочитать ответ репозитория."
            ) from error

    else:
        try:
            with open(source, "r", encoding="utf-8") as file:
                data = json.load(file)

        except (OSError, json.JSONDecodeError) as error:
            raise RuntimeError(
                f"Не удалось прочитать тестовый файл: {error}"
            ) from error

    return data

def get_dependencies(data):
    """Извлечение списка прямых зависимостей пакета."""

    if not isinstance(data, dict):
        raise RuntimeError("Некорректный формат данных.")

    info = data.get("info")

    if not isinstance(info, dict):
        raise RuntimeError(
            "В полученных данных отсутствует информация о пакете."
        )

    dependencies = info.get("requires_dist") or []

    if not isinstance(dependencies, list):
        raise RuntimeError(
            "Некорректный формат списка зависимостей."
        )

    return dependencies

def build_parser():
    """Сборка парсера аргументов."""
    parser = argparse.ArgumentParser(
        prog="depviz",
        description="Этап 2: получение зависимостей пакета.",
    )
    parser.add_argument("--package", "-p", required=True,
                        type=check_package,
                        help="Имя анализируемого пакета.")
    parser.add_argument("--source", "-s", required=True,
                        type=check_source,
                        help="URL репозитория или путь к файлу.")
    parser.add_argument("--mode", "-m", required=True,
                        type=check_mode,
                        help="Режим: real | test.")
    parser.add_argument("--output", "-o", required=True,
                        type=check_output,
                        help="Имя файла графа (.png).")
    parser.add_argument("--depth", "-d", required=True,
                        type=check_depth,
                        help="Максимальная глубина анализа.")
    parser.add_argument("--filter", "-f", required=True,
                        type=check_filter,
                        help="Подстрока фильтрации пакетов.")
    return parser


def main(argv=None):
    """Точка входа: разбор аргументов и вывод ключ-значение."""
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        return exc.code if exc.code is not None else EXIT_ERROR

    print("Параметры:")
    print(f"package = {args.package}")
    print(f"source  = {args.source}")
    print(f"mode    = {args.mode}")
    print(f"output  = {args.output}")
    print(f"depth   = {args.depth}")
    print(f"filter  = {args.filter}")

    try:
        data = get_package_data(
            args.package,
            args.source,
            args.mode
        )

        dependencies = get_dependencies(data)

    except RuntimeError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return EXIT_ERROR

    print("\nПрямые зависимости:")

    if dependencies:
        for dependency in dependencies:
            print(f"- {dependency}")
    else:
        print("У пакета нет прямых зависимостей.")

    return EXIT_OK


if __name__ == "__main__":
    main()