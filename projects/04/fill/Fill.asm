// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//// Replace this comment with your code.

// Set complete to 8192 after the start of screen
@SCREEN
    D=A

@8192 // This comes from the 32 words by 256 rows
    D=D+A

@COMPLETE
    M = D

// comeback to the start and go again
(START) // if the keyboard is pressed val is = -1 else it is 0
    @KBD
    D=M
    @BLACK
    D; JNE

    @val
    M=0

(CONTINUE)
    // set address to the start of the screen memory map
    @SCREEN
    D=A
    @address
    M=D

(LOOP) // check if the address is out of bounds 
    @COMPLETE
    D=M
    @address
    D=M-D
    @START
    D; JGE

    @val
    D=M
    @address
    A=M
    M=D

    @address
    M=M+1

    @LOOP
    0; JMP

(BLACK)
    @val
    M=-1

@CONTINUE
    0; JMP
