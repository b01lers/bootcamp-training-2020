# b01lers Bootcamp 2020 Training

# Table of Contents
1. [General](#general)
2. [How To Learn](#howto)
3. [Web Exploitation](#web)
4. [Reverse Engineering](#re)
5. [Cryptography](#crypto)
6. [Binary Exploitation](#pwn)
7. [Hardware Hacking + RF](#hardware)
8. [Penetration Testing](#pentesting)
9. [Resources + Practice](#resources)
10. [Tools](#tools)

## General <a name="general" />

This repository is the master repo for the b01lers CTF team's training materials. The intent of this material is to teach our team's new members how to play CTF by teaching in as short a time as possible the basics of every category of challenge typically seen. 

***Disclaimer***: Some of the materials contained within *may* be harmful if misused. b01lers does not endorse using any of this information for evil, it is provided _ONLY_ for educational purposes.


## How To Learn <a name="howto" />

The best way to learn CTF is to practice. To this end, we have provided a self-contained [docker](https://www.docker.com/) container to remove the environment setup barrier of entry. A docker container is similar to a virtual machine and will allow you to run our customized pre-setup machine to go through all the training with.

That docker container's source can be found [here](https://github.com/b01lers/bootcamp-docker-2020) along with installation instructions. Our youtube channel has install instructions for MacOS, Linux, and Windows [here](https://www.youtube.com/watch?v=a66mwylcXVU&list=PLdGU-K4Khkr_vuAVPbIBPgDfi9jq3PuYl).

The content in this repository was designed to be used alongside a presenter. You can find the video training sessions [here](https://www.youtube.com/playlist?list=PLdGU-K4Khkr8iqzOdjKKj1QLmJJnks5fO)

Our recommendation if you want to learn to play CTF is this:
- Watch and work along with all of the bootcamp training sessions.
- Identify which category you are most interested in based on what you've learned.
- Focusing on that category, use the resources and practice to learn and *play* as much as possible.

Ultimately, the way to become a `1337` hacker is to play CTF as much as possible, but we hope this is a good introduction. Please feel free to make an issue for any recommendations, edits, etc.

## Web Exploitation <a name="web" />

#### [Day 1](https://www.youtube.com/watch?v=FvSDpqVoeNQ):
- Basic developer tools:
    - Inspect Element
    - JS Console
    - Builtin Debugger
    - Network and storage
- Javascript + client side validation
- HTML + CSS
- HTTP methods and internet infrastructure
- CURL + Postman

#### [Day 2](https://www.youtube.com/watch?v=k962ILypsvM):
- PHP
- Sessions
- Hashing and type confusion
- Databases and SQL Injection
- Cross-Site Scripting (XSS)
    - Persistent
    - Reflected
    - DOM
- Burp Suite

#### Extras:
- [Burp Suite Demo](https://www.youtube.com/watch?v=F_CuwnTUc54)
- [PHP XSS Demo](https://www.youtube.com/watch?v=RStTjA32f8A)

## Reverse Engineering <a name="re" />

#### [Day 1](https://www.youtube.com/watch?v=j6nj3uMp-dg) `rev/day_1/slides`:
- Hardware and Data Representations
- Language Types `rev/day_1/01-language-types`
    - Compiled
    - Intepreted
    - JIT
    - Bytecode compiled
- Compiled languages
- The C compiler `rev/day_1/02-compilation-steps`
- ELF format `rev/day_1/03-readelf-sections`
- Linux system calls + how programs are run `rev/day_1/04-running-programs-on-linux`
- Introduction to GDB and debugging
- The dynamic loader (interpreter) `rev/day_1/05-dynamic-call`
- Program images in memory
- Introduction to assembly language `rev/day_1/06-dynamic-call-asm`
- Important x86-64 instructions
- Stack and Heap
- Stack frames + function calls
- Calling convention + ABI
- High level RE process
- Assembly construct: selection `rev/day_1/07-selection-challenge`

#### [Day 2](https://www.youtube.com/watch?v=9zhFV-j8VyE):
- Assembly construct: selection (review) `rev/day_2/00-selection`
- Assembly construct: iteration `rev/day_2/02-iteration`
- Structures `rev/day_2/03-data-structures`
- Parameter passing `rev/day_2/01-function-calls`
- Advanced Ghidra features
    - Decompilation
    - Struct editor
    - CFG
- Obfuscation, stripping, optimization

## Cryptography <a name="crypto" />

## Binary Exploitation <a name="pwn" />


## Hardware Hacking + RF <a name="hardware" />


## Penetration Testing <a name="pentesting" />



## Resources + Practice <a name="resources" />

### General
- [Awesome CTF](https://github.com/apsdehal/awesome-ctf)

### Web Exploitation 
- [https://xss-game.appspot.com/](https://xss-game.appspot.com/)
- [https://www.hackthebox.eu/](https://www.hackthebox.eu/)
- [https://www.hackthissite.org/](https://www.hackthissite.org/)
- [http://www.dvwa.co.uk/](http://www.dvwa.co.uk/)
- [https://tryhackme.com/](https://tryhackme.com/)

### Reverse Engineering

REcommended Reading:
- Hacking: The Art of Exploitation, by Jon Erickson
- Reversing: Secrets of Reverse Engineering, by Eldad Eilam
- Assembly Language for Intel-Based Computers, by Kip R. Irvine
- Practical Reverse Engineering: x86, x64, ARM, Windows Kernel, Reversing Tools, and Obfuscation, by Dang, Gazet, Bachaalany
- Practical Binary Analysis, by Dennis Andriesse
- The Ghidra Book, by Chris Eagle and Kara Nance
- Just look through [here](https://nostarch.com/catalog/security) really.

REcommended Tutorials + References:
- [Azeria ARM Tutorial](https://azeria-labs.com/writing-arm-assembly-part-1/)
- [x86 Instruction Reference](https://www.felixcloutier.com/x86/)
- [Intel Official x86 Reference](https://software.intel.com/content/www/us/en/develop/articles/intel-sdm.html)
- [RPISEC Malware Analysis](https://github.com/RPISEC/Malware)
- [RPISEC MBE](https://github.com/RPISEC/MBE)

REcommended Practice:
- [Challenges.re](https://challenges.re/)
- [Crackmes.one](https://crackmes.one/)
- [Microcorruption](https://microcorruption.com/)
- [Reversing.kr](https://reversing.kr/challenge.php)
- [OSX Crackme](https://reverse.put.as/crackmes/)
- [Pwnable.XYZ](https://pwnable.xyz/challenges/)
- [W3Challs.com](https://w3challs.com/challenges/list/reversing)
- [io.netgarage.org](http://io.netgarage.org/)
- [Crackme Forum](https://0x00sec.org/c/reverse-engineering/challenges/13)

### Cryptography

### Binary Exploitation

- [Pwn College](https://pwn.college/)

## Tools <a name="tools" />
