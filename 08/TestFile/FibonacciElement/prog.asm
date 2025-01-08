@256
D=A
@SP
M=D
// push retAddrLabel
@aa.Sys.init$ret.0
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
@Sys.init
0;JMP
(aa.Sys.init$ret.0)
(Main.fibonacci)
@0
D=A
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
@2   // push constant 2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP  // lt
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
D=D-M
@TRUE0
D;JLT
D=0
@CONTINUE0
0;JMP
(TRUE0)
D=-1
(CONTINUE0)
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@Main.Main.fibonacci$N_LT_2
D;JNE
@Main.Main.fibonacci$N_GE_2
0;JMP
(Main.Main.fibonacci$N_LT_2)
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
(Main.Main.fibonacci$N_GE_2)
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
@2   // push constant 2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP  // sub
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
D=D-M
@SP
A=M
M=D
@SP
M=M+1
// push retAddrLabel
@Main.Main.fibonacci$ret.0
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
@Main.fibonacci
0;JMP
(Main.Main.fibonacci$ret.0)
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
@1   // push constant 1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP  // sub
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
D=D-M
@SP
A=M
M=D
@SP
M=M+1
// push retAddrLabel
@Main.Main.fibonacci$ret.1
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
@Main.fibonacci
0;JMP
(Main.Main.fibonacci$ret.1)
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
(Sys.init)
@0
D=A
@4   // push constant 4
D=A
@SP
A=M
M=D
@SP
M=M+1
// push retAddrLabel
@Sys.Main.fibonacci$ret.0
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
@Main.fibonacci
0;JMP
(Sys.Main.fibonacci$ret.0)
(Sys.Sys.init$END)
@Sys.Sys.init$END
0;JMP
