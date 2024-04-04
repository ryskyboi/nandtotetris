//Push a constant value onto the stack
@3030
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// pops pointer value
@R0
M=M-1
A=M
D=M
@3
M=D

//Push a constant value onto the stack
@3040
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// pops pointer value
@R0
M=M-1
A=M
D=M
@4
M=D

//Push a constant value onto the stack
@32
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// popping a this segment
@3
D=M
@2
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

//Push a constant value onto the stack
@46
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
@6
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

// pushes pointer value
@3
D=M
@R0
M=M+1
A=M-1
M=D

// pushes pointer value
@4
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
// pushing a this segment
@3
D=M
@2
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// subtracts SP-1 from SP-2
@R0
A=M-1
D=M
A=A-1
M=M-D;
@R0
M=M-1
// pushing a that segment
@4
D=M
@6
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