@echo off
python .\src\main.py -p idna -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f test

python .\src\main.py -p -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f test

python .\src\main.py -p idna -s hptts://pypi.org/pypi -m real -o Graf.png -d 3 -f test

python .\src\main.py -p idna -s https://pypi.org/pypi -m neveroyatno -o Graf.png -d 3 -f test

python .\src\main.py -p idna -s https://pypi.org/pypi -m real -o Graf.ggg -d 3 -f test

python .\src\main.py -p idna -s https://pypi.org/pypi -m real -o Graf.png -d -99 -f test

python .\src\main.py -p idna -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f

python ./src/main.py -p package-that-does-not-exist-123456 -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f test

python ./src/main.py -p example -s ./tests/test_invalid.json -m test -o Graf.png -d 3 -f test

python ./src/main.py -p example -s ./tests/test_no_info.json -m test -o Graf.png -d 3 -f test

python ./src/main.py -p example -s ./tests/test_invalid_dependencies.json -m test -o Graf.png -d 3 -f test

python ./src/main.py -p empty-example -s ./tests/test_empty.json -m test -o Graf.png -d 3 -f test