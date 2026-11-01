PYTHON  := python
MAIN    := ./src/main.py

.PHONY: run run-p run-s run-m run-o run-d run-f test-package test-json test-no-info test-dependencies test-empty clean

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

test-package:
	$(PYTHON) $(MAIN) -p package-that-does-not-exist-123456 -s https://pypi.org/pypi -m real -o Graf.png -d 3 -f test

test-json:
	$(PYTHON) $(MAIN) -p example -s ./tests/test_invalid.json -m test -o Graf.png -d 3 -f test

test-no-info:
	$(PYTHON) $(MAIN) -p example -s ./tests/test_no_info.json -m test -o Graf.png -d 3 -f test

test-dependencies:
	$(PYTHON) $(MAIN) -p example -s ./tests/test_invalid_dependencies.json -m test -o Graf.png -d 3 -f test

test-empty:
	$(PYTHON) $(MAIN) -p empty-example -s ./tests/test_empty.json -m test -o Graf.png -d 3 -f test

clean:
	rm -rf ../src/__pycache__ ./__pycache__