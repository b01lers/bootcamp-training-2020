#include<time.h>
#include<stdlib.h>
#include<stdio.h>


void main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    // Keep track of the game state in a struct
    struct {
        int secret_number;      // Secret Number
        int number_list[16];    // List of known numbers
        char name[32];          // Name of Winner
        int score;              // Your score
    } game_state ;

    srand(time(NULL));

    // Initialize Game state
    game_state.secret_number = rand() % 1000; // Generate an impossible to guess number
    for(int i = 0; i < 16; i++) {
        game_state.number_list[i] = rand() % 1000;
    }

    // Print Item number_list
    printf("Which number in number_list would you like to print?\n> ");
    int choice;
    scanf("%d", &choice);

    printf("number_list[%d] = %d\n", choice, game_state.number_list[choice]);

    // Guess Secret Number
    printf("Now guess the secret number.\n> ");
    scanf("%d", &choice);

    // Calculate Score
    if(choice == game_state.secret_number) {
        game_state.score = 1337;
        printf("You are right! Score: %d\n", game_state.score);
        printf("Enter your name to save your score:\n> ");
        scanf("%s", game_state.name);
    } else {
        game_state.score = 0;
        printf("You are wrong! Score: %d\n", game_state.score);
    }

    // Easter Egg
    if(game_state.score == 0x1337) {
        printf("You won the secret prize, since you had a score of 0x%x! You found an easter egg... shell!\n", game_state.score);
        system("/bin/bash");
    }
}
