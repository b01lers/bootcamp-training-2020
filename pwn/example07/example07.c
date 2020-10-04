// Example 7 (20 min) Format Strings (leak GOT, overwrite ret addr)

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    printf("%p\n", & setvbuf);

    char * a = malloc(32);

    char * b = malloc(32);
    free(b);

    fgets(b, 128, stdin);

    b = malloc(32);
    char * c = malloc(32);

    fgets(c, 128, stdin);

    free(a);
    free(b);

    exit(0);
}
