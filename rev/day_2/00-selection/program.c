#include <stdio.h>
#include <string.h>

int check_a(char * inp) {
    if (inp[0x00] != 'f') {
        return 0;
    }
    if (inp[0x01] != 'l') {
        return 1;
    }
    if (inp[0x02] != 'a') {
        return 2;
    }
    if (inp[0x03] != 'g') {
        return 3;
    }
    if (inp[0x04] != '{') {
        return 4;
    }
    if (inp[0x05] != 'p') {
        return 5;
    }
    if (inp[0x06] != 'k') {
        return 6;
    }
    if (inp[0x07] != 'c') {
        return 7;
    }
    if (inp[0x08] != 'u') {
        return 8;
    }
    if (inp[0x09] != 'i') {
        return 9;
    }
    if (inp[0x0a] != 'c') {
        return 10;
    }
    if (inp[0x0b] != 'h') {
        return 11;
    }
    if (inp[0x0c] != '0') {
        return 12;
    }
    if (inp[0x0d] != '0') {
        return 13;
    }
    if (inp[0x0e] != 's') {
        return 14;
    }
    if (inp[0x0f] != 'u') {
        return 15;
    }
    if (inp[0x10] != '}') {
        return 16;
    }
    return -1;
}

int check_b(char * inp) {
    if (inp[0x00] >= 0x30 && inp[0x00] <= 0x39) {
        if ((inp[0x00] - '0') >= 5) {
            return 0;
        }
        if ((inp[0x00] - '0') <= 3) {
            if ((inp[0x00] - '0') > 1) {
                return 0;
            } else {
                if ((inp[0x00] - '0') <= 0) {
                    return 0;
                } else {
                }
            }
        } else {
            return 0;
        }
    }
    if (inp[0x01] >= 0x30 && inp[0x01] <= 0x39) {
        if ((inp[0x01] - '0') != 3) {
            return 1;
        }
    }
    if (inp[0x02] >= 0x30 && inp[0x02] <= 0x39) {
        if ((inp[0x02] - '0') != 3) {
            return 2;
        }
    }
    if (inp[0x03] >= 0x30 && inp[0x03] <= 0x39) {
        if ((inp[0x03] - '0') != 7) {
            return 3;
        }
    }
    if (inp[0x04] >= 0x30 && inp[0x04] <= 0x39) {
        if ((inp[0x04] - '0') == 6) {
        } else {
            return 4;
        }
    }
    if (inp[0x05] >= 0x30 && inp[0x05] <= 0x39) {
        if ((inp[0x05] - '0') != 6) {
            return 5;
        }
    }
    if (inp[0x06] >= 0x30 && inp[0x06] <= 0x39) {
        if ((inp[0x06] - '0') == 6) {
            return -1;
        } else {
            return 6;
        }
    }
    return 10;
}

int main(void) {
    char inp[0x12];
    printf("Password: ");
    fgets(inp, 0x12, stdin);
    int c = check_a(inp);
    getc(stdin);
    if (c == -1) {
        printf("Password correct. PIN: ");
        memset(inp, 0, 0x12);
        fflush(stdin);
        fgets(inp, 0x8, stdin);
        int d = check_b(inp);
        if (d == -1) {
            printf("Logged in!\n");
        } else {
            printf("Error @ %d\n", d);
        }
    } else {
        printf("Error @ %d!\n", c);
    }
}
