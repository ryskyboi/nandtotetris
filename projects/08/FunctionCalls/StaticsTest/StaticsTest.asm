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
D=M
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
@6
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
//Staring function call 
//Push the return address onto the stack
@Class1.set$1
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
// Resetting arb and local
@7
D=M
@R0
D=M-D
@2
M=D
@R0
D=M
@1
M=D
// Goto Class1.set
@Class1.set
0;JMP

(Class1.set$1)
// popping temp variable 0
@R0
M=M-1
A=M
D=M
@5
M=D

//Push a constant value onto the stack
@23
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@15
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Staring function call 
//Push the return address onto the stack
@Class2.set$2
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
// Resetting arb and local
@7
D=M
@R0
D=M-D
@2
M=D
@R0
D=M
@1
M=D
// Goto Class2.set
@Class2.set
0;JMP

(Class2.set$2)
// popping temp variable 0
@R0
M=M-1
A=M
D=M
@5
M=D

//Staring function call 
//Push the return address onto the stack
@Class1.get$3
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
// Resetting arb and local
@5
D=M
@R0
D=M-D
@2
M=D
@R0
D=M
@1
M=D
// Goto Class1.get
@Class1.get
0;JMP

(Class1.get$3)
//Staring function call 
//Push the return address onto the stack
@Class2.get$4
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
// Resetting arb and local
@5
D=M
@R0
D=M-D
@2
M=D
@R0
D=M
@1
M=D
// Goto Class2.get
@Class2.get
0;JMP

(Class2.get$4)
// creates a label
(END)

// Goto END
@END
0;JMP

// Creating a function
(Class2.set)

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

//Popping static variable
@R0
M=M-1
A=M
D=M
@Class2.0
M=D

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

//Popping static variable
@R0
M=M-1
A=M
D=M
@Class2.1
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

// Creating a function
(Class2.get)

//Pushing static Variable
@Class2.0
D=M
@R0
M=M+1
A=M-1
M=D

//Pushing static Variable
@Class2.1
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
@7
M=D
//Store the return address in a temp variable
@5
A=D-A
D=M
@8
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
@7
AM=M-1
D=M
@4
M=D
// Restore this
@7
AM=M-1
D=M
@3
M=D
// Restore argument
@7
AM=M-1
D=M
@2
M=D
// Restore local
@7
AM=M-1
D=M
@1
M=D

@8
A=M
0; JMP

// Creating a function
(Class1.set)

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

//Popping static variable
@R0
M=M-1
A=M
D=M
@Class1.0
M=D

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

//Popping static variable
@R0
M=M-1
A=M
D=M
@Class1.1
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
// Storing local in a temp variable
@1
D=M
@9
M=D
//Store the return address in a temp variable
@5
A=D-A
D=M
@10
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
@9
AM=M-1
D=M
@4
M=D
// Restore this
@9
AM=M-1
D=M
@3
M=D
// Restore argument
@9
AM=M-1
D=M
@2
M=D
// Restore local
@9
AM=M-1
D=M
@1
M=D

@10
A=M
0; JMP

// Creating a function
(Class1.get)

//Pushing static Variable
@Class1.0
D=M
@R0
M=M+1
A=M-1
M=D

//Pushing static Variable
@Class1.1
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
@11
M=D
//Store the return address in a temp variable
@5
A=D-A
D=M
@12
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
@11
AM=M-1
D=M
@4
M=D
// Restore this
@11
AM=M-1
D=M
@3
M=D
// Restore argument
@11
AM=M-1
D=M
@2
M=D
// Restore local
@11
AM=M-1
D=M
@1
M=D

@12
A=M
0; JMP
