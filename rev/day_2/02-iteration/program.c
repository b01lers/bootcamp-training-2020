#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char slots[17] = {0};
int shuff[16] = {0x0a, 0x0b, 0x0c, 0x03, 0x00, 0x0d, 0x02, 0x09, 0x08, 0x01, 0x07, 0x04, 0x06, 0x05, 0x0f, 0x0e};
char flag[17] = {'{', 'a', 'o', 'g', 'l', 'o', 'o', 'l', 's', 'p', 'f', 'l', 'a', 'o', '}', 'p', 0};

void examine(void);
void delete(void);
void swap(void);
void check(void);
void set(void);
void debug(void);

void (*funcs[6]) (void);

void examine(void) {
    printf("\n");
    printf("[");
    for (int i = 0; i < 0x10; i++) {
        if (i == 0xf) {
            printf("%d]\n", slots[i]);
        } else {
            printf("%d, ", slots[i]);
        }
    }
}

void delete(void) {
    int i, c;
    while (1) {
        printf("\nEnter an index to delete: ");
        scanf(" %d", &i);
        while ((c = getchar()) != EOF && c != '\n');
        if (i >= 0 && i <= 0x10) {
            slots[i] = 0;
            break;
        }
        printf("Invalid index.\n");
    }
}

void swap(void) {
    int i, j, c;
    while (1) {
        printf("\nEnter 2 indices separated by a space: ");
        scanf(" %d%*c%d", &i, &j);
        while ((c = getchar()) != EOF && c != '\n');
        if (i >= 0 && i <= 0x10) {
            if (j >= 0 && j <= 0x10) {
                slots[i] ^= slots[j];
                slots[j] ^= slots[i];
                slots[i] ^= slots[j];
                break;
            }
        }
        printf("Invalid indices.\n");
    }
}

void shuffle(char * c) {
    size_t l = strlen(c);
    char tmp[l];
    for (unsigned i = 0; i < l; i++) {
        printf("Putting %c at %d\n", c[i], shuff[i % 0x10]);
        tmp[shuff[i % 0x10]] = c[i];
    }
    strcpy(c, tmp);
}

void check(void) {
    shuffle(slots);
    int i = 0xf;
    do {
        if (slots[i] != flag[i]) {
            printf("\nNope!\n");
            return;
        }
    } while (i-- != 0);
    printf("You got it!\n");
}

void set(void) {
    int i, c;
    char j;
    while (1) {
        printf("\nEnter an index and a value, separated by a space: ");
        scanf(" %d%*c%c", &i, &j);
        printf("Trying to insert %c at index %d\n", j, i);
        printf("%d %d\n", i >= 0, i <= 0x10);
        while ((c = getchar()) != EOF && c != '\n');
        if (i >= 0 && i <= 0x10) {
            slots[i] = j;
            break;
        }
        printf("Invalid index. %d\n", i);
    }
}

void debug(void) {
    printf("The array we want is: \n");
    printf("[");
    for (int i = 0; i < 0x10; i++) {
        if (i == 0xf) {
            printf("%d]\n", flag[i]);
        } else {
            printf("%d, ", flag[i]);
        }
    }
    char buf[17] = {0};
    strcpy(buf, slots);
    shuffle(buf);
    printf("Your input is: \n");
    printf("[");
    for (int i = 0; i < 0x10; i++) {
        if (i == 0xf) {
            printf("%d]\n", buf[i]);
        } else {
            printf("%d, ", buf[i]);
        }
    }
}


int prompt(void) {
    int choice;
    while (1) {
        printf("Options:\n"
            "1. Examine Slot\n"
            "2. Delete Slot\n"
            "3. Swap Slots\n"
            "4. Check Slots\n"
            "5. Set Slot\n"
            "> ");
        scanf(" %d", &choice);
        int c;
        while ((c = getchar()) != EOF && c != '\n');
        if (choice <= 6 && choice >= 1) {
            /* 5 is allowed because we have a hidden option */
            break;
        }
        printf("Error! You didn't enter a valid choice.\n");
    }
    return choice;
}

void start(void) {
    while (1) {
        int choice = prompt();
        (*funcs[choice - 1])();
    }
}

void setup(void) {
    funcs[0] = examine;
    funcs[1] = delete;
    funcs[2] = swap;
    funcs[3] = check;
    funcs[4] = set;
    funcs[5] = debug;
}

int main(void) {
    setup();
    start();
}

