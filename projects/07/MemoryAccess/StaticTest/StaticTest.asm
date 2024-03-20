//Push a constant value onto the stack
@111
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@333
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@888
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Popping static variable
@R0
M=M-1
A=M
D=M
@StaticTest.8
M=D

//Popping static variable
@R0
M=M-1
A=M
D=M
@StaticTest.3
M=D

//Popping static variable
@R0
M=M-1
A=M
D=M
@StaticTest.1
M=D

//Pushing static Variable
@StaticTest.3
D=M
@R0
M=M+1
A=M-1
M=D

//Pushing static Variable
@StaticTest.1
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
//Pushing static Variable
@StaticTest.8
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