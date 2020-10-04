#include <stdio.h>
#include <stdlib.h>

long numbers[16];

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char * inp;
    int c;

    while(1) {
        inp = malloc(16); 
        printf("Which number would you like to write to?\n> ");
        fgets(inp, 16, stdin);
        c = atol(inp);
        printf("What value should be written?\n> ");
        fgets(inp, 16, stdin);
        numbers[c] = atol(inp);
        printf("Which number would you like to print?\n> ");
        fgets(inp, 16, stdin);
        c = atol(inp);
        printf("%lu\n", numbers[c]);
        free(inp);
    }

}
