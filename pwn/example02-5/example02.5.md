# Example 2.5: Shellcoding

This is a recorded example, demonstrating a shellcoding attack. This was historically one of the most common ways to exploit a stack buffer overflow, but in modern operating systems with modern protections, they are obsolete. Sometimes shellcoding is still used in attacks against embedded devices. CTFs do occasionally have shellcoding challenges, but usually the challenge is writing a custom shellcode to fit a difficult set of requirements rather than a classic shellcoding attack.

# ASLR
The reason we are not doing this together, is because of a protection called 'ASLR' or Address Space Layout Randomization. It is possible to disable ASLR on some systems, but your Docker images will inherit the setting of your host, and we do not want to mess with the host.

ASLR will cause the address of the stack and other memory segments to be randomized at runtime. In the example, we knew what address the shellcode would have been at and could overwrite the return address to our buffer. If ASLR were enabled, that address would be different every time the program is run, so we would need a leak of the stack address to effectively use the same exploit.

# NX
Another protection that is seen in most modern software is 'NX' or non-executable memory. This ensures that no writeable memory locations are marked as executable. If NX were enabled and we were to attempt to solve this example, we would get a segmentation fault for trying to execute our shellcode.
