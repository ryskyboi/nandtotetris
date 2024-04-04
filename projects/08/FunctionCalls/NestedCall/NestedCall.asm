// Creating a function
(Sys.init)

//Push a constant value onto the stack
@4000
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
@5000
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

//Staring function call 
//Push the return address onto the stack
@Sys.main$0
D=A
@R0
M=M+1
A=M-1
M=D
//Pushing local onto the stack
@1
D=M
@R0
M=M+1
A=M-1
M=D
//Pushing argument onto the stack
@2
D=M
@R0
M=M+1
A=M-1
M=D
//Pushing this onto the stack
@3
D=M
@R0
M=M+1
A=M-1
M=D
//Pushing that onto the stack
@4
D=M
@R0
M=M+1
A=M-1
M=D
// Resetting arg and local
@5
D=A
@R0
D=M-D
@2
M=D
@R0
D=M
@1
M=D
// Goto Sys.main
@Sys.main
0;JMP

(Sys.main$0)
// popping temp variable 1
@R0
M=M-1
A=M
D=M
@6
M=D

// creates a label
(LOOP)

// Goto LOOP
@LOOP
0;JMP

// Creating a function
(Sys.main)
// pushing local 0 onto the stack
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0

//Push a constant value onto the stack
@4001
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
@5001
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
@200
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
@1
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
@40
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

//Push a constant value onto the stack
@6
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
@3
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
@123
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Staring function call 
//Push the return address onto the stack
@Sys.add12$1
D=A
@R0
M=M+1
A=M-1
M=D
//Pushing local onto the stack
@1
D=M
@R0
M=M+1
A=M-1
M=D
//Pushing argument onto the stack
@2
D=M
@R0
M=M+1
A=M-1
M=D
//Pushing this onto the stack
@3
D=M
@R0
M=M+1
A=M-1
M=D
//Pushing that onto the stack
@4
D=M
@R0
M=M+1
A=M-1
M=D
// Resetting arg and local
@6
D=A
@R0
D=M-D
@2
M=D
@R0
D=M
@1
M=D
// Goto Sys.add12
@Sys.add12
0;JMP

(Sys.add12$1)
// popping temp variable 0
@R0
M=M-1
A=M
D=M
@5
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

// pushing a local segment
@1
D=M
@1
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// pushing a local segment
@1
D=M
@2
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// pushing a local segment
@1
D=M
@3
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D

// pushing a local segment
@1
D=M
@4
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
// adds the top 2 values on the stack
@R0
A=M-1
D=M
A=A-1
M=D+M
@R0
M=M-1
// adds the top 2 values on the stack
@R0
A=M-1
D=M
A=A-1
M=D+M
@R0
M=M-1
// adds the top 2 values on the stack
@R0
A=M-1
D=M
A=A-1
M=D+M
@R0
M=M-1
// Storing local in a temp variable
@1
D=M
@13 // Using temp 9 and 9 as Nested call assumes that we can use the lowest temp registers?
M=D
//Store the return address in a temp variable
@5
A=D-A
D=M
@14
M=D
//return the value
@R0
A=M-1
D=M
@2
A=M
M=D
//Restore the stack pointer of the caller
@2
D=M+1
@R0
M=D
// Restore that
@13
AM=M-1
D=M
@4
M=D
// Restore this
@13
AM=M-1
D=M
@3
M=D
// Restore argument
@13
AM=M-1
D=M
@2
M=D
// Restore local
@13
AM=M-1
D=M
@1
M=D

@14
A=M
0; JMP

// Creating a function
(Sys.add12)

//Push a constant value onto the stack
@4002
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
@5002
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
@12
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
// Storing local in a temp variable
@1
D=M
@13 // Using temp 9 and 9 as Nested call assumes that we can use the lowest temp registers?
M=D
//Store the return address in a temp variable
@5
A=D-A
D=M
@14
M=D
//return the value
@R0
A=M-1
D=M
@2
A=M
M=D
//Restore the stack pointer of the caller
@2
D=M+1
@R0
M=D
// Restore that
@13
AM=M-1
D=M
@4
M=D
// Restore this
@13
AM=M-1
D=M
@3
M=D
// Restore argument
@13
AM=M-1
D=M
@2
M=D
// Restore local
@13
AM=M-1
D=M
@1
M=D

@14
A=M
0; JMP
