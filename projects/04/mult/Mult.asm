//Multiplier

//Set R2=0
    @0
    D=A
    @R2
    M=D

    @i
    M=0


//New code to handle negative numbers
    @R1
    D=M

    @LESS // if R1 < 0 Jump else all good
    D; JLT

(CONTINUE)
(LOOP)
    @i
    D=M
    @R1
    D=D-M
    @END
    D;JGE

    @R0
    D=M
    @R2
    M=M+D

    @i
    M=M+1 // i=i+1
    @LOOP
    0;JMP

(LESS)
    @R0
    D=M

    @0 // D=0
    D=A

    @R0 // R0 = 0-R0
    M=D-M

    @R1 // R1 = 0-R1
    M=D-M

    @CONTINUE
    0; JMP

@CONTINUE
    0;JMP

(END)
    @END
    0;JMP

