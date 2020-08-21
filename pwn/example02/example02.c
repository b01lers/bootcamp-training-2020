#include<stdio.h>
#include<stdlib.h>

void win1() {
    printf("You win! Now try to use this program to call /bin/sh");
}

void win2(char * arg) {
    system(arg);
}

void main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char buffer[16];
     
    gets(buffer);
}
