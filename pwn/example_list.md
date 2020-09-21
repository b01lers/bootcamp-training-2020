Example 1 (20 min): Getting familiar with pwntools, negative index to overwrite variable and buffer overflow variable. (Same challenge)

Example 2 (30 min): Buffer overflow to win function and win2(int arg) function. win2 requires arguments and some rop

> Introduce ASLR

Mini-Example (5 min) Buffer overflow to shellcode [prerecorded since ASLR is a problem]
 - This is just to show the history. Explain progression of ASLR and NX from this example, and explain how both prevent this type of exploit.

> Introduce PIE

Example 3 (15 min) Partial Overwrite TODO: Skip/Move/Add Technique?

Example 4 (20 min) GOT and libc (Leaking and using) - BSS unbounded array indexes
 - Mention RELRO
 - Demo onegadget and libc
 - Part 2 with relro enabled, and using `__malloc_hook`.

## Example 5 (20 min) Format Strings (leak GOT, overwrite ret addr)

#### Example 6 (20 min): Buffer overflow to libc (ret2system, then onegadget) Skippable?

> Introduce Stack Canaries
 - GOT overwrites bypass this, since execution never makes it to the stack pointer

#### Example 7 (20 min) Stack Canary & Pie Leaks (no null termination): tell it how many bytes to read, zeros that many.
 - Leak stack canary, then overwrite ret addr
 - Note that this technique can also be used to leak PIE (Add that to this demo?)

#### Example 8 (20 min) Libc leak, but no PIE/stack leak: `__libc_free_hook/__libc_malloc_hook/environ`; Uninitialized Data for leak (If size > 0, read name, else unitialized data?); Buffer overflow into pointer
 - Full relro

> Introduce Heap

Explain Heap Structure (15 min)
 - Note types of vulnerabilities: Overflows that heap metadata (change sizes of chuns for example), double free, use after free, wild free (free fake chunk)

## Example 9 (20 min) Double Free - 'evildragon' style: make name and enemy struct overlap and set enemy hp to 0.

## Example 10 (20 min) Use after free (tcache) - Read freed chunk's fd pointer to leak heap. Set freed chunk's fd ptr to GOT for an overwrite.
 - Note that this is similar to some heap overflows (which there is no example for), which can similarly overwrite the fd pointer to corrupt the freelist

Example 11 (not happening) Heap Overflow: change size of chunk, free that chunk, create overlapping chunks
