// initializes the assembler
@256
D=A
@R0
M=D
//Staring function call 
//Push the return address onto the stack
@Sys.init$0
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
// Goto Sys.init
@Sys.init
0;JMP

(Sys.init$0)
// Creating a function
(Sys.init)

//Push a constant value onto the stack
@4
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Staring function call 
//Push the return address onto the stack
@Main.fibonacci$1
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
// Goto Main.fibonacci
@Main.fibonacci
0;JMP

(Main.fibonacci$1)
// creates a label
(END)

// Goto END
@END
0;JMP

// Creating a function
(Main.fibonacci)

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
// checking less than
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@LT_0
D;JLT
@R0
A=M-1
M=0
@END_0
0;JMP
(LT_0)
@R0
A=M-1
M=-1
(END_0)

// Conditional Goto N_LT_2
@R0
M=M-1
A=M
D=M
@N_LT_2
D;JNE

// Goto N_GE_2
@N_GE_2
0;JMP

// creates a label
(N_LT_2)

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

// creates a label
(N_GE_2)

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
//Staring function call 
//Push the return address onto the stack
@Main.fibonacci$2
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
// Goto Main.fibonacci
@Main.fibonacci
0;JMP

(Main.fibonacci$2)
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
//Staring function call 
//Push the return address onto the stack
@Main.fibonacci$3
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
// Goto Main.fibonacci
@Main.fibonacci
0;JMP

(Main.fibonacci$3)
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
