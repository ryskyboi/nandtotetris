//Push a constant value onto the stack
@10
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

//Push a constant value onto the stack
@21
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@22
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// popping a argument segment
@2
D=M
@2
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

// popping a argument segment
@2
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

//Push a constant value onto the stack
@36
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
@6
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

//Push a constant value onto the stack
@42
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@45
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
@5
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

// popping a that segment
@4
D=M
@2
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

//Push a constant value onto the stack
@510
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// popping temp variable 6
@R0
M=M-1
A=M
D=M
@11
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

// pushing a that segment
@4
D=M
@5
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

// subtracts SP-1 from SP-2
@R0
A=M-1
D=M
A=A-1
M=M-D;
@R0
M=M-1
// pushing a this segment
@3
D=M
@6
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// pushing a this segment
@3
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
// subtracts SP-1 from SP-2
@R0
A=M-1
D=M
A=A-1
M=M-D;
@R0
M=M-1
// pushing temp variable 6
@11
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