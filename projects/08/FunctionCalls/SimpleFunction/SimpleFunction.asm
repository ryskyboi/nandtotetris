// Creating a function
(SimpleFunction.test)
// pushing local 0 onto the stack
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0

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

// adds the top 2 values on the stack
@R0
A=M-1
D=M
A=A-1
M=D+M
@R0
M=M-1
// bitwise not
@R0
A=M-1
M=!M

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
// Storing local in a temp variable
@1
D=M
@5
M=D
//Store the return address in a temp variable
@5
A=D-A
D=M
@6
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
@5
AM=M-1
D=M
@4
M=D
// Restore this
@5
AM=M-1
D=M
@3
M=D
// Restore argument
@5
AM=M-1
D=M
@2
M=D
// Restore local
@5
AM=M-1
D=M
@1
M=D

@6
A=M
0; JMP
