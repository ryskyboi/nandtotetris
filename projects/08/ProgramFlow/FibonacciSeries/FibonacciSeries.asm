// pushing a argument segment
@2
D=M
@1
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// pops pointer value
@R0
M=M-1
A=M
D=M
@4
M=D

//Push a constant value onto the stack
@0
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// popping a that segment
@4
D=M
@0
D=D+A
@addr_1
M=D
//moves back the stack pointer
@R0
M=M-1
A=M
D=M
@addr_1
A=M
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
// popping a that segment
@4
D=M
@1
D=D+A
@addr_2
M=D
//moves back the stack pointer
@R0
M=M-1
A=M
D=M
@addr_2
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
@2
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
@addr_4
M=D
//moves back the stack pointer
@R0
M=M-1
A=M
D=M
@addr_4
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

// Conditional Goto COMPUTE_ELEMENT
@R0
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE

// Goto END
@END
0;JMP

// creates a label
(COMPUTE_ELEMENT)

// pushing a that segment
@4
D=M
@0
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// pushing a that segment
@4
D=M
@1
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
// popping a that segment
@4
D=M
@2
D=D+A
@addr_8
M=D
//moves back the stack pointer
@R0
M=M-1
A=M
D=M
@addr_8
A=M
M=D

// pushes pointer value
@4
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
// adds the top 2 values on the stack
@R0
A=M-1
D=M
A=A-1
M=D+M
@R0
M=M-1
// pops pointer value
@R0
M=M-1
A=M
D=M
@4
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
@addr_10
M=D
//moves back the stack pointer
@R0
M=M-1
A=M
D=M
@addr_10
A=M
M=D

// Goto LOOP
@LOOP
0;JMP

// creates a label
(END)
