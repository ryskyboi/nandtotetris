from commands import C_GOTO, C_FUNCTION, C_CALL, C_IF_GOTO, C_LABEL
from assembler_commands.memory_access import BASIC_SEGMENT_MAP


class Branching:
    def __init__(self):
        self.inc = 0

    def label(self, comm: C_LABEL) -> str:
        return f"""// creates a label
({comm.arg1})
"""

    def goto(self, comm: C_GOTO) -> str:
        return f"""// Goto {comm.arg1}
@{comm.arg1}
0;JMP
"""

    def if_goto(self, comm: C_IF_GOTO) -> str:
        return f"""// Conditional Goto {comm.arg1}
@R0
M=M-1
A=M
D=M
@{comm.arg1}
D;JNE
"""
    def call(self, comm: C_CALL):
        value = "//Staring function call \n"
        value += f"""//Push the return address onto the stack
@{comm.arg1}${str(self.inc)}
D=A
@R0
M=M+1
A=M-1
M=D
"""
        for name, location in BASIC_SEGMENT_MAP.items():
            value += f"""//Pushing {name} onto the stack
@{str(location)}
D=M
@R0
M=M+1
A=M-1
M=D
"""
        value += f"""// Resetting arg and local
@{str(comm.arg2 + 5)}
D=A
@R0
D=M-D
@{BASIC_SEGMENT_MAP["argument"]}
M=D
@R0
D=M
@{BASIC_SEGMENT_MAP["local"]}
M=D
"""
        value += self.goto(C_GOTO(comm.arg1))
        value += f"""
({comm.arg1}${str(self.inc)})"""
        self.inc += 1
        return value

    def function(self, comm: C_FUNCTION) -> str:
        function_name = f"""// Creating a function
({str(comm.arg1)})
"""
        push_locals_string = """// pushing local 0 onto the stack
"""
        push_locals = """@R0
M=M+1
A=M-1
M=0
"""
        return function_name + push_locals_string * min(1, comm.arg2) + push_locals * comm.arg2

    def return_value(self) -> str:
        value = f"""// Storing local in a temp variable
@{str(BASIC_SEGMENT_MAP["local"])}
D=M
@{str(5 + 8)} // Using temp 9 and 9 as Nested call assumes that we can use the lowest temp registers?
M=D
//Store the return address in a temp variable
@5
A=D-A
D=M
@{str( 5 + 9 )}
M=D
//return the value
@R0
A=M-1
D=M
@{str(BASIC_SEGMENT_MAP["argument"])}
A=M
M=D
//Restore the stack pointer of the caller
@{str(BASIC_SEGMENT_MAP["argument"])}
D=M+1
@R0
M=D
"""
        for _value, _position in reversed(BASIC_SEGMENT_MAP.items()):
            value += f"""// Restore {_value}
@{str(5 + 8)}
AM=M-1
D=M
@{str(_position)}
M=D
"""
        value += f"""
@{str( 5 + 9 )}
A=M
0; JMP
"""

        return value
