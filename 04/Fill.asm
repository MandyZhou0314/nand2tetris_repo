// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.

(LOOP)
// init i, 32registers * 256rows
    @8159
    D=A
    @i
    M=D

    @KBD
    D=M

    @BLACKLOOP  
    D;JGT  //jump to white or black loop


// white
(WHITELOOP)
    @i
    D=M

    @LOOP
    D;JLT

    @SCREEN
    A=D+A  //let register at address p+i to be white
    M=0

    @i
    M=M-1

    @WHITELOOP
    0;JMP

// black
(BLACKLOOP)
    @i
    D=M

    @LOOP
    D;JLT

    @SCREEN
    A=D+A  //let register at address p+i to be black
    M=-1

    @i
    M=M-1

    @BLACKLOOP
    0;JMP