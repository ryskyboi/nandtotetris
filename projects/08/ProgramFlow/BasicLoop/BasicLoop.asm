//Push a constant value onto the stack
@0
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// popping a local segment
@1
D=M
@0
D=D+A
@addr_0
M=D
//moves back the stack pointer
@R0
M=M-1
A=M
D=M
@addr_0
A=M
M=D

// creates a label
(LOOP)

// pushing a argument segment
@2
D=M
@0
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// pushing a local segment
@1
D=M
@0
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// adds the top 2 values on the stack
@R0
A=M-1
D=M
A=A-1
M=D+M
@R0
M=M-1
// popping a local segment
@1
D=M
@0
D=D+A
@addr_3
M=D
//moves back the stack pointer
@R0
M=M-1
A=M
D=M
@addr_3
A=M
M=D

// pushing a argument segment
@2
D=M
@0
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

//Push a constant value onto the stack
@1
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// subtracts SP-1 from SP-2
@R0
A=M-1
D=M
A=A-1
M=M-D;
@R0
M=M-1
// popping a argument segment
@2
D=M
@0
D=D+A
@addr_5
M=D
//moves back the stack pointer
@R0
M=M-1
A=M
D=M
@addr_5
A=M
M=D

// pushing a argument segment
@2
D=M
@0
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// Conditional Goto LOOP
@R0
M=M-1
A=M
D=M
@LOOP
D;JNE

// pushing a local segment
@1
D=M
@0
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D
