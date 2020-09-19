#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char FLAG[] = {0xaa, 0xb0, 0xa5, 0xab, 0xbf, 0xbb, 0x77, 0xb0, 0xa7, 0xb3, 0xb1, 0x76, 0xb6, 0xa9, 0xc1};

void scream_abuse() {
    FILE * abuse = fopen("abuse.txt", "r");
    char * file = (char *) malloc(2048 * sizeof(char));
    memset(file, 0, 2048);
    char * start = file;
    char * end;
    fread(file, 1, 2048, abuse);
    int which = rand() % 59;
    int at = 0;
    while (at < which) {
        if (*start++ == '\n') {
            at++;
        }
    }
    end = start;
    while (*end++ != '\n' && *end != '\0');
    *end = '\0';
    printf("%s", start);
    free(file);
    file = NULL;
    return;
}

int check(char * input) {
    for (int i = 0x0; i < 0xf; i++) {
        if (input[i] == (char)(FLAG[i] - 0x44)) {
            scream_abuse();
        } else {
            return 0;
        }
    }
    return 1;
}


int main(int argc, char ** argv) {
    srand(12312);
    char * input = (char *) malloc(0x10 * sizeof(char));
    fgets(input, 0x10, stdin);
    printf("Hmm...%s, you say?\n", input);
    if (check(input)) {
        printf("Win!\n");
    } else {
        printf("Fail!\n");
    }
}
