// Example 10 (20 min) Use after free (tcache) - Read freed chunk's fd pointer to leak heap. Set freed chunk's fd ptr to GOT for an overwrite.
// - Note that this is similar to some heap overflows (which there is no example for), which can similarly overwrite the fd pointer to corrupt the freelist
#include <stdio.h>

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    
}
