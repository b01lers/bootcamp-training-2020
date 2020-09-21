// Some Example C Code
#include <stdio.h>

int bar(int n) {
    return n + 20;
}

int foo(int n) {
    return bar(n) * 2;
}

int main(int argc, char ** argv) {
    printf("%d\n", foo(10));
}
