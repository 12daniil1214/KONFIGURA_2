PYTHON  := python
MAIN    := ./src/main.py

.PHONY: run run-p run-s run-m run-o run-d run-f clean

run:
	$(PYTHON) $(MAIN) -p idna -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f test

run-p:
	$(PYTHON) $(MAIN) -p -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f test

run-s:
	$(PYTHON) $(MAIN) -p idna -s hptts://pypi.org/pypi -m real -o Graf.png -d 3 -f test

run-m:
	$(PYTHON) $(MAIN) -p idna -s https://pypi.org/pypi -m neveroyatno -o Graf.png -d 3 -f test

run-o:
	$(PYTHON) $(MAIN) -p idna -s https://pypi.org/pypi -m real -o Graf.ggg -d 3 -f test

run-d:
	$(PYTHON) $(MAIN) -p idna -s https://pypi.org/pypi -m real -o Graf.png -d -99 -f test

run-f:
	$(PYTHON) $(MAIN) -p idna -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f

clean:
	rm -rf ../src/__pycache__ ./__pycache__