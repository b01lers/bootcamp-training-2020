## What is PWN?
 - Binary Exploitation
 - Compare to RE / Background required
 - In most real CTFs, source is not provided for pwn chals, and a lot of reversing still needs to happen. For these trainings, I will be providing source, since my goal is to teach exploitation concepts. The bootcamp CTF will have some challenges with and some challenges without source.
 - We will be focusing on the same architecture as RE: 64bit intel. The same techniques generally apply to different architectures.

## High-level PWN concepts
 - What is pwn at it's most basic
   - Finding a way to make a program do something it wasn't intended to do.
   - At it's simplest, often it's just exploiting a missing check.
   - Often involves controlled memory correuption
 - Common Vulnerabilities: preview
   - Shell tricks: PWN generally focuses on binary exploitation, but occasionally you will see bash challenges or need to elevate privlidges in a bash shell. https://overthewire.org/wargames/bandit/ is a great resource to get familiar with basic exploitation tricks. We will not go into detail about any of these tricks during these trainings.
   - Buffer Overflows: Writing out of bounds, overwritting variables or enabling further memory corruption.
   - Integer Over/Underflows: Sometimes leads to buffer overflows when an index is over/underflowed.
   - Off-by one errors: Less than or equal to instead of less than.
   - Misuse of functions: format strings, the misuse of printf can allow for memory corruption
   - Race conditions: Accessing files out of order, threading protections
 - Defenses: preview
   - ASLR (Address Space Layout Randomisation)
   - PIE (Position Independent Executables)
   - NX (Non-executable memory)
   - Stack Canaries
 - Techniques to bypass defenses: preview
   - Randomization and Stack Canaries
     - Leak addresses or stack canaries
     - Partial/LSB Overwrites
     - Brute forcing works in some cases
     - GOT (Global Offset Table) overwrites
   - NX
     - Return oriented programming
     - GOT (Global Offset Table) overwrites
   - Different techniques will be used depending on the situation.
 - Tooling
   - GDB
   - GEF
   - python3 & Pwntools
   - onegadget, checksec, a few other utilities
   - RE Tools (Ghidra)

Good Resources for further practice and learning:
 - Live Overflow Binary Exploitation
 - Exploit Exersizes (Protostar, Fusion)
 - Overthewire (Narnia, others)

Structure:
 - This will be example based, starting with simple programs, and introducing a new technique or two in each example.

Day 1:
------

Example 1 (20 min): Getting familiar with pwntools, negative index to overwrite variable and buffer overflow variable. (Same challenge)

Example 2 (30 min): Buffer overflow to win function and win2(int arg) function. win2 requires arguments and some rop, GDB via pwntools introduced used

> Introduce ASLR

Mini-Example (5 min) Buffer overflow to shellcode [prerecorded since ASLR is a problem]
 - This is just to show the history. Explain progression of ASLR and NX from this example, and explain how both prevent this type of exploit.

> Introduce PIE

Example 3 (15 min) Partial Overwrite TODO: Skip/Move/Add Technique?

Example 4 (20 min) GOT (Leaking and using) - BSS unbounded array indexes
 - Mention RELRO

Example 5 (20 min) Format Strings (leak GOT, overwrite ret addr)

Day 2:
------

Example 6 (20 min): Buffer overflow to libc (ret2system, then onegadget)

> Introduce Stack Canaries
 - GOT overwrites bypass this, since execution never makes it to the stack pointer

Example 7 (20 min) Stack Canary & Pie Leaks (no null termination): tell it how many bytes to read, zeros that many.
 - Leak stack canary, then overwrite ret addr
 - Note that this technique can also be used to leak PIE (Add that to this demo?)

Example 8 (20 min) Libc leak, but no PIE/stack leak: __libc_free_hook/__libc_malloc_hook/environ; Uninitialized Data for leak (If size > 0, read name, else unitialized data?); Buffer overflow into pointer

> Introduce Heap

Explain Heap Structure (15 min)
 - Note types of vulnerabilities: Overflows that heap metadata (change sizes of chuns for example), double free, use after free, wild free (free fake chunk)

Example 9 (20 min) Double Free - 'evildragon' style: make name and enemy struct overlap and set enemy hp to 0.

Example 10 (20 min) Use after free (tcache) - Read freed chunk's fd pointer to leak heap. Set freed chunk's fd ptr to GOT for an overwrite.
 - Note that this is similar to some heap overflows (which there is no example for), which can similarly overwrite the fd pointer to corrupt the freelist

Example 11 (not happening) Heap Overflow: change size of chunk, free that chunk, create overlapping chunks
