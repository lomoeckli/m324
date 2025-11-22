.PHONY: test

test: src/file.py tests/test.py
	python -m coverage run -m unittest discover tests
	python -m coverage report
	del .coverage
	rmdir /s /q src\__pycache__
	rmdir /s /q tests\__pycache__

# Dieses Makefile muss mit Powershell ausgeführt werden!