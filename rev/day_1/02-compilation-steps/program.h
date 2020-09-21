#include <stdio.h>


// This define will be replaced in the preprocess step
#define name_prompt "Hello! What is your name?\n> "
// This macro will be replaced in the preprocess step
#define ROTBR(byte, amount) ((byte + amount) % 256)

/*
 * This is a block comment. You will notice that when you run the GCC preprocessor
 * on this project, it will not appear in the output. 
 */

char * get_name(void);
void rot(char * name, int amount);

