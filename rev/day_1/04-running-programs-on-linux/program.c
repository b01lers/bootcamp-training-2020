#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>



int main(int argc, char ** argv) {
    pid_t pid = fork();
    char * const args[] = {"ls", "-lah", "/bin/", NULL};
    switch(pid) {
        case 0:     /* We are in the child process, see `man 2 fork`. */
            /* Execute `ls -lah /bin` */
            printf("Hello, I am the child process! My pid is %d\n", getpid());
            execvp(args[0], args);
            perror("exec");
            exit(2);
        case -1:    /* Something went wrong and the fork() call failed. */
            /* Print an error */
            perror("fork");
            exit(1);
        default:    /* We are in the parent process and pid == the child pid */
            /* Print out something and exit */
            printf("I have run the ls command from PID %d\n", pid);
            exit(0);
    }

}
