// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//// Replace this comment with your code.
// r2 = 0
// while r0 > 0:
//   r2 += r1
//   r0 -= 1


// initilization
    @R2
    M=0

(LOOP)
// check whether R0 is greater than 0
    @R0
    D=M
    @END
    D;JLE

// r2 += r1
    @R1
    D=M
    @R2
    M=D+M

// r0 -= 1
    @R0
    M=M-1

    @LOOP
    0;JMP


(END)
    @END
    0;JMP


