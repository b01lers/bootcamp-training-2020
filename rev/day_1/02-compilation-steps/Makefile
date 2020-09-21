CC = gcc
all: program.s program.i program.o program program-static

# Preprocess and Compile but do not assemble
program.s: program.c
	gcc -S -o program.s program.c -no-pie -g -O0

# Preprocess Only
program.i: program.c
	gcc -E -o program.i program.c -no-pie -g -O0

# Preprocess, compile, and assemble but do not link
program.o: program.c
	gcc -c -o program.o program.c -no-pie -g -O0

# Preprocess, compile, assemble, and link (produce executable)
program: program.c
	gcc -o program program.c -no-pie -g -O0

program-static: program.c
	gcc -o program program.c -no-pie -g -O0 -static

clean:
	rm program.s
	rm program.i
	rm program.o
	rm program
