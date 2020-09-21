// Example 6 (20 min): Buffer overflow to libc (ret2system, then onegadget)

// SCRAPPED?
#include <stdio.h>

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}
