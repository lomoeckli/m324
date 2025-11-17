all: a.out build run
a.out: main.cpp
	g++ main.cpp
build: a.out
	docker build -t cpp-image .
	rm -f a.out
run:
	docker run --rm -it cpp-image
clean:
	docker rmi cpp-image