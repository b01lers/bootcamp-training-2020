// Example 11 (not happening) Heap Overflow: change size of chunk, free that chunk, create overlapping chunks
#include <stdio.h>

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}
