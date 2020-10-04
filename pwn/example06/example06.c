// Example 5 (20 min) Format Strings (leak GOT, overwrite ret addr)

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

int randint(int * val) {
    int urandom_fd = open("/dev/urandom", O_RDONLY);

    read(urandom_fd, val, sizeof(int));

    close(urandom_fd);
}

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char input[512];
    int stackvar;
    randint(&stackvar);

    // Basic Format String to Leak Stack Variable
    printf("What is your name?\n");
    fgets(input, 512, stdin);
    printf("Hello ");
    printf(input);
    
    fgets(input, 512, stdin);
    if(atoi(input) != stackvar) {
        printf("Sorry!\n");
        exit(0);
    }

    // Format String to Leak Arbitrary Address
    fgets(input, 512, stdin);
    printf(input);
    

    // Format String to Write To an Arbitrary Address
    fgets(input, 512, stdin);
    printf(input);

    memset(input, 0, 512);
    puts("Exiting");

    exit(0);
}
