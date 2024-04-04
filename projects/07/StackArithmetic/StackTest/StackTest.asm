//Push a constant value onto the stack
@17
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@17
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// checking for equality
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@EQUAL_0
D;JEQ
@R0
A=M-1
M=0
@END_0
0;JMP
(EQUAL_0)
@R0
A=M-1
M=-1
(END_0)

//Push a constant value onto the stack
@17
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@16
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// checking for equality
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@EQUAL_1
D;JEQ
@R0
A=M-1
M=0
@END_1
0;JMP
(EQUAL_1)
@R0
A=M-1
M=-1
(END_1)

//Push a constant value onto the stack
@16
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@17
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// checking for equality
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@EQUAL_2
D;JEQ
@R0
A=M-1
M=0
@END_2
0;JMP
(EQUAL_2)
@R0
A=M-1
M=-1
(END_2)

//Push a constant value onto the stack
@892
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@891
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
@END_3
0;JMP
(LT_0)
@R0
A=M-1
M=-1
(END_3)

//Push a constant value onto the stack
@891
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@892
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
@LT_1
D;JLT
@R0
A=M-1
M=0
@END_4
0;JMP
(LT_1)
@R0
A=M-1
M=-1
(END_4)

//Push a constant value onto the stack
@891
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@891
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
@LT_2
D;JLT
@R0
A=M-1
M=0
@END_5
0;JMP
(LT_2)
@R0
A=M-1
M=-1
(END_5)

//Push a constant value onto the stack
@32767
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@32766
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// checking greater than
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@GT_0
D;JGT
@R0
A=M-1
M=0
@END_6
0;JMP
(GT_0)
@R0
A=M-1
M=-1
(END_6)

//Push a constant value onto the stack
@32766
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@32767
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// checking greater than
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@GT_1
D;JGT
@R0
A=M-1
M=0
@END_7
0;JMP
(GT_1)
@R0
A=M-1
M=-1
(END_7)

//Push a constant value onto the stack
@32766
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@32766
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// checking greater than
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@GT_2
D;JGT
@R0
A=M-1
M=0
@END_8
0;JMP
(GT_2)
@R0
A=M-1
M=-1
(END_8)

//Push a constant value onto the stack
@57
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@31
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
//Push a constant value onto the stack
@53
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
//Push a constant value onto the stack
@112
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
// gets the negative of the value at the top of the stack
@R0
A=M-1
M=-M

// bitwise and
@R0
M=M-1
A=M
D=M
A=A-1
M=D&M
//Push a constant value onto the stack
@82
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1
// bitwise or
@R0
M=M-1
A=M
D=M
A=A-1
M=D|M
// bitwise not
@R0
A=M-1
M=!M
