#include "program.h"

#define NAME_SIZE 40
char g_name[NAME_SIZE];

/* Rotate each byte's bits a certain number
 * of times. Modify inplace
 *
 * @param name      The name to rotate
 * @param amount    The number of times to rotate the bits
 */
void rot(char * name, int amount) {
    while (*name) {
        *name = ROTBR(*name, amount);
        name++;
    }
}

/* Get a user's name from stdin
 *
 * @returns         The user's name (max 39 chars)
 */
char * get_name(void) {
    printf("%s", name_prompt);
    if (!fgets(g_name, NAME_SIZE - 1, stdin)) {
        printf("Error: unable to read your name!\n");
    }
    return g_name;
}

int main(int argc, char ** argv) {
    char * name = get_name();
    rot(name, 13);
    printf("Your rotated name is: ");
    while (*name) {
        printf("%c", *name);
        name++;
    }
}
