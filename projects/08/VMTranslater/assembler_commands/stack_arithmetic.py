from commands import C_ARITHMETIC


class Arithmetic:
    def __init__(self):
        self.LT, self.GT, self.EQ, self.END = 0, 0, 0, 0

    def operate(self, command: C_ARITHMETIC) -> str:
        return getattr(self, f'_{command.arg1}')()

    def _add(self) -> str:
        return '''// adds the top 2 values on the stack
@R0
A=M-1
D=M
A=A-1
M=D+M
@R0
M=M-1'''

    def _sub(self) -> str:
        return '''// subtracts SP-1 from SP-2
@R0
A=M-1
D=M
A=A-1
M=M-D;
@R0
M=M-1'''

    def _neg(self) -> str:
        return '''// gets the negative of the value at the top of the stack
@R0
A=M-1
M=-M
'''

    def _eq(self) -> str:
        result = f'''// checking for equality
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@EQUAL_{self.EQ}
D;JEQ
@R0
A=M-1
M=0
@END_{self.END}
0;JMP
(EQUAL_{self.EQ})
@R0
A=M-1
M=-1
(END_{self.END})
'''
        self.EQ += 1
        self.END += 1
        return result

    def _gt(self) -> str:
        result = f'''// checking greater than
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@GT_{self.GT}
D;JGT
@R0
A=M-1
M=0
@END_{self.END}
0;JMP
(GT_{self.GT})
@R0
A=M-1
M=-1
(END_{self.END})
'''
        self.GT += 1
        self.END += 1
        return result

    def _lt(self) -> str:
        result = f'''// checking less than
@R0
M=M-1
A=M
D=M
A=A-1
D=M-D
@LT_{self.LT}
D;JLT
@R0
A=M-1
M=0
@END_{self.END}
0;JMP
(LT_{self.LT})
@R0
A=M-1
M=-1
(END_{self.END})
'''
        self.LT += 1
        self.END += 1
        return result

    def _and(self) -> str:
        return '''// bitwise and
@R0
M=M-1
A=M
D=M
A=A-1
M=D&M'''

    def _or(self) -> str:
        return '''// bitwise or
@R0
M=M-1
A=M
D=M
A=A-1
M=D|M'''

    def _not(self) -> str:
        return '''// bitwise not
@R0
A=M-1
M=!M
'''
