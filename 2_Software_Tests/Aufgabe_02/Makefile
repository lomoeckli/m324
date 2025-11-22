.PHONY: all

all: setup test

setup: user.py db.py testDb.py
	docker run -d --name test-mongo -p 27017:27017 mongo:latest

test:
	python -m coverage run -m unittest testDb.py
	python -m coverage report
	docker stop test-mongo
	docker rm test-mongo
	del .coverage
	rmdir /s /q __pycache__