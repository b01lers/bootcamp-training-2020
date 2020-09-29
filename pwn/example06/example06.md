# PWN Example 05

This example will introduce format string vulnerabilities and how they are used for leaks and arbitrary write.

## Printf and Variadic Arguments

Printf has variadic arguments: It can have a variable number of agruments. The implementation of variadic arguments in C does not specify how to know the number of arguments used, so each function implementation needs to handle it itself.

With printf, the number of arguments is determined by the format specifier:
```c
printf("Hello %s! Your score is: %d", name, score);
```

## Example

Take a quick look to see if you can identify the vulnerability in this code before you start this example.
```c
fgets(input, 512, stdin);
printf("Hello ");
printf(input);
```

The bug here is that the user controls the format string. If the user sets input to `%d` for example, printf will attempt to read the next argument to printf as an integer. On `x86_64`, that will be the value in `rsi`. Format strings can also directly specify which argument to print by using a `$`: `%4$d`. Since arguments are passed on the stack after the registers are used, a user defined format string will be able to leak the stack.

```
What is your name?
%lx
Hello 7ffe9fb25870
```

In this case, 7ffe9fb25870 is the value in rsi. This can be checked in gdb if you are curious.

We can get passed the first check using this approach.
```c
char input[512];
int stackvar;
randint(&stackvar);

// Basic Format String to Leak Stack Variable
printf("What is your name?\n");
fgets(input, 512, stdin);
printf("Hello ");
printf(input);
```

We will need to first findd the offset from the stack where printf is called to our `stackvar`.
One way to do that is to use GDB and a semi-burte force approach, with a format string of `%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p`. The alternative would be to break in GDB and do some math, taking into account the calling convention and current stack pointer.

When we run in gdb, we get an output of:
```
Hello
0x7fffffff8f80.(nil).0x7ffff7ef7bd3.0x7fffffffb5f0.(nil).0x7fffffffb7e0.0xd6ae2baaf7fd771c.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e70252e7025.0x252e70252e70252e.0xa70252e70.0x1.0x7ffff7ffe6f8
```
We can print stackvar, and find it in our input
```
gef> p stackvar
$1 = 0xd6ae2baa
```
It is the first 4 bytes of the 7th argument: 0xd6ae2baaf7fd771c.

We can print this directly, then do the conversion to pass the check with:
```
What is your name?
%7$p
Hello 0xd4e04f6065b0271c
3571470176
```

### Part 2: Using Printf to leak and write to an arbitrary adress

The first example shows printf being used to leak a value that is already on the stack. But what if we want to read an address not in the stack, like somewhere in the GOT? If our input is on the stack, we can access our own input with our format specifiers, and use one like `%s` which will dereference the address given and print it as a string.

This explanation is incomplete. Watch the video on YouTube or read the solution script to continue.
