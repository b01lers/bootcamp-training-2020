program: program.c liblib.so
	gcc -L . -o program program.c -llib -O0 -s

liblib.so: lib.c
	gcc -c -fPIC lib.c -o lib.o
	gcc -shared -o liblib.so lib.o
