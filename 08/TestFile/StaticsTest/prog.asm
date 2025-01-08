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
(Class1.set)
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
@SP   // pop static 0
M=M-1
A=M
D=M
@Class1.0
M=D
@1   // push argument 1
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
@SP   // pop static 1
M=M-1
A=M
D=M
@Class1.1
M=D
@0   // push constant 0
D=A
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
(Class1.get)
@0
D=A
@Class1.0   // push static 0
D=M
@SP
A=M
M=D
@SP
M=M+1
@Class1.1   // push static 1
D=M
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
(Class2.set)
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
@SP   // pop static 0
M=M-1
A=M
D=M
@Class2.0
M=D
@1   // push argument 1
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
@SP   // pop static 1
M=M-1
A=M
D=M
@Class2.1
M=D
@0   // push constant 0
D=A
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
(Class2.get)
@0
D=A
@Class2.0   // push static 0
D=M
@SP
A=M
M=D
@SP
M=M+1
@Class2.1   // push static 1
D=M
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
@6   // push constant 6
D=A
@SP
A=M
M=D
@SP
M=M+1
@8   // push constant 8
D=A
@SP
A=M
M=D
@SP
M=M+1
// push retAddrLabel
@Sys.Class1.set$ret.0
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
@2
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class1.set
0;JMP
(Sys.Class1.set$ret.0)
@SP   // pop temp 0
M=M-1
A=M
D=M
@5
M=D
@23   // push constant 23
D=A
@SP
A=M
M=D
@SP
M=M+1
@15   // push constant 15
D=A
@SP
A=M
M=D
@SP
M=M+1
// push retAddrLabel
@Sys.Class2.set$ret.1
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
@2
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class2.set
0;JMP
(Sys.Class2.set$ret.1)
@SP   // pop temp 0
M=M-1
A=M
D=M
@5
M=D
// push retAddrLabel
@Sys.Class1.get$ret.2
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
@Class1.get
0;JMP
(Sys.Class1.get$ret.2)
// push retAddrLabel
@Sys.Class2.get$ret.3
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
@Class2.get
0;JMP
(Sys.Class2.get$ret.3)
(Sys.Sys.init$END)
@Sys.Sys.init$END
0;JMP
