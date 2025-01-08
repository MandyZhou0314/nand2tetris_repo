(Sys.init)
@0
D=A
@4000   // push constant 4000
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP   // pop pointer 0
M=M-1
A=M
D=M
@THIS
M=D
@5000   // push constant 5000
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP   // pop pointer 1
M=M-1
A=M
D=M
@THAT
M=D
// push retAddrLabel
@Sys.main$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP 每 5 每 nArgs
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Sys.main
0;JMP
(Sys.main$ret.0)
@SP   // pop temp 1
M=M-1
A=M
D=M
@6
M=D
(LOOP)
@LOOP
0;JMP
(Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
M=D
@SP
M=M+1
@4001   // push constant 4001
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP   // pop pointer 0
M=M-1
A=M
D=M
@THIS
M=D
@5001   // push constant 5001
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP   // pop pointer 1
M=M-1
A=M
D=M
@THAT
M=D
@200   // push constant 200
D=A
@SP
A=M
M=D
@SP
M=M+1
@1   // pop local 1
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@40   // push constant 40
D=A
@SP
A=M
M=D
@SP
M=M+1
@2   // pop local 2
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@6   // push constant 6
D=A
@SP
A=M
M=D
@SP
M=M+1
@3   // pop local 3
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@123   // push constant 123
D=A
@SP
A=M
M=D
@SP
M=M+1
// push retAddrLabel
@Sys.add12$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP 每 5 每 nArgs
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Sys.add12
0;JMP
(Sys.add12$ret.1)
@SP   // pop temp 0
M=M-1
A=M
D=M
@5
M=D
@0   // push local 0
D=A
@LCL
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1   // push local 1
D=A
@LCL
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2   // push local 2
D=A
@LCL
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@3   // push local 3
D=A
@LCL
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@4   // push local 4
D=A
@LCL
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP  // add
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
D=D+M
@SP
A=M
M=D
@SP
M=M+1
@SP  // add
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
D=D+M
@SP
A=M
M=D
@SP
M=M+1
@SP  // add
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
D=D+M
@SP
A=M
M=D
@SP
M=M+1
@SP  // add
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
D=D+M
@SP
A=M
M=D
@SP
M=M+1
// endFrame = LCL
@LCL
D=M
@R14
M=D
// retAddr = *(endFrame每5)
@R14
D=M
@5
D=D-A
A=D
D=M
@R15
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M+1
@SP
M=D
// THAT = *(endFrame每1)
@R14
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
// THIS = *(endFrame每2)
@R14
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
// ARG = *(endFrame每3)
@R14
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
// LCL = *(endFrame每4)
@R14
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
// goto retAddr
@R15
A=M
0;JMP
(Sys.add12)
@0
D=A
@4002   // push constant 4002
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP   // pop pointer 0
M=M-1
A=M
D=M
@THIS
M=D
@5002   // push constant 5002
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP   // pop pointer 1
M=M-1
A=M
D=M
@THAT
M=D
@0   // push argument 0
D=A
@ARG
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@12   // push constant 12
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP  // add
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
D=D+M
@SP
A=M
M=D
@SP
M=M+1
// endFrame = LCL
@LCL
D=M
@R14
M=D
// retAddr = *(endFrame每5)
@R14
D=M
@5
D=D-A
A=D
D=M
@R15
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M+1
@SP
M=D
// THAT = *(endFrame每1)
@R14
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
// THIS = *(endFrame每2)
@R14
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
// ARG = *(endFrame每3)
@R14
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
// LCL = *(endFrame每4)
@R14
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
// goto retAddr
@R15
A=M
0;JMP
