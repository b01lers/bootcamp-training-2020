#include<stdio.h>
#include<stdlib.h>


void readInput() {
    char buffer[16];
    char c;
    int i = 0;
    c = fgetc(stdin);
    while(c != '\n') {
        buffer[i] = c;
        c = fgetc(stdin);
        i = i + 1;
    }
}

void win() {
    system("/bin/sh");
}

void go() {
    readInput();
}

int main() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);

    printf("In this example, use a LSB overwrite to call 'win'.\n");
    
    go();
}

