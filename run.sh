#!/usr/bin/env bash
python3 ./src/main.py -p idna -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f test

python3 ./src/main.py -p -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f test

python3 ./src/main.py -p idna -s hptts://pypi.org/pypi -m real -o Graf.png -d 3 -f test

python3 ./src/main.py -p idna -s https://pypi.org/pypi -m neveroyatno -o Graf.png -d 3 -f test

python3 ./src/main.py -p idna -s https://pypi.org/pypi -m real -o Graf.ggg -d 3 -f test

python3 ./src/main.py -p idna -s https://pypi.org/pypi -m real -o Graf.png -d -99 -f test

python3 ./src/main.py -p idna -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f