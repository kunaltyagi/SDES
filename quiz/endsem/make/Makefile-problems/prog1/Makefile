.PHONY: all test clean
all: main

MAINDEPENDS = $(shell gcc -MM main.c|sed 's/main[.]o://')

main.o: $(MAINDEPENDS)
	gcc -c main.c -o main.o

main: main.o
	gcc -o main main.o

clean:
	$(RM) main.o main

test:
	@expr $$(./main "Hello") == "olleH"
