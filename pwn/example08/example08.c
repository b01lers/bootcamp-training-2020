#include <stdio.h>
#include <stdlib.h>

// This is a super crafted example designed to show the danger of uninitialized data, in addition to the use of __free_hook and __malloc_hook and one_gadget when exploiting a binary. These techniques are often useful when dealing with heap exploitation, since a complex ROP is often sufficient for other challenges. 

void readInput(char * buffer, int len) {
    char c;
    int i = 0;
    c = fgetc(stdin);
    while(c != '\n') {
        if (i > len) {
            break;
        }
        buffer[i] = c;
        c = fgetc(stdin);
        i = i + 1;
    }
}

typedef struct {
    char chars[32];
    char * chars2;
} DoubleString;

typedef struct {
    char chars[32];
    int (*print) (const char *);
} Thing;

void readAndEchoInput() {
    Thing asdf;
    asdf.print = &puts;
    
    fgets(asdf.chars, 32, stdin);
    if(asdf.chars[0] != 0);
    asdf.print(asdf.chars);
}

void leakUninitializedMemory() {
    char str[40];
    readInput(str, 40);
    puts(str);
}

void OverflowIntoPointerThenWrite() {
    DoubleString str;
    str.chars2 = malloc(32);
    fgets(str.chars, 42, stdin);
    fgets(str.chars2, 42, stdin);
    free(str.chars2);
}

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    
    readAndEchoInput();
    leakUninitializedMemory();
    OverflowIntoPointerThenWrite();
} 
