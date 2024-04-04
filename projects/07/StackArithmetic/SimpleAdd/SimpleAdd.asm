//Push a constant value onto the stack
@7
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@8
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// adds the top 2 values on the stack
@R0
A=M-1
D=M
A=A-1
M=D+M
@R0
M=M-1