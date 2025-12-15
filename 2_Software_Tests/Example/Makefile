.PHONY: test

test: src/compare.py tests/test.py
	python3 -m unittest discover tests
	rm -rf src/__pycache__
	rm -rf tests/__pycache__

# // generate report and run tests
# python3 -m coverage run -m unittest discover tests -v

# Der Report kann mit diesem Befehl gelesen werden: python3 -m coverage report

# Aus dem File .coverage kann ein xml mit diesem Befehl erstellt werden: python3 -m coverage xml -i