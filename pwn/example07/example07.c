// Example 7 (20 min) Stack Canary & Pie Leaks (no null termination): tell it how many bytes to read, zeros that many.
// - Leak stack canary, then overwrite ret addr
// - Note that this technique can also be used to leak PIE (Add that to this demo?)
#include<stdio.h>
#include<string.h>

void readInput(char * buffer) {
    char c;
    int i = 0;
    c = fgetc(stdin);
    while(c != '\n') {
        buffer[i] = c;
        c = fgetc(stdin);
        i = i + 1;
    }
}

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char buffer[32];
    do { 
        readInput(buffer);
        printf("%s\n", buffer);
    } while(strcmp(buffer, "exit") != 0);
}
