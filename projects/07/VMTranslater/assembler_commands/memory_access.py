from typing import Union
from commands import C_POP, C_PUSH

MEMORY_TYPES = Union[C_POP, C_PUSH]

BASIC_SEGMENT_MAP = {'local': 1, 'argument': 2, 'this': 3, 'that': 4}
THIS_THAT = {0: 3, 1: 4}  # 0 maps to this and 1 maps to that

class Memory:
    def __init__(self):
        self.index = 0

    def access(self, comm: MEMORY_TYPES, file_name: str):
        if comm.arg1 == 'constant': return self._constant(comm)
        elif comm.arg1 in BASIC_SEGMENT_MAP.keys(): return self._basic_segments(comm)
        elif comm.arg1 == "temp": return self._temp(comm)
        elif comm.arg1 == "pointer": return self._pointer(comm)
        elif comm.arg1 == "static": return self._static(comm, file_name)
        else: raise NotImplementedError(f"Memory Type {comm.arg1} is not yet implemented")

    def _constant(self, comm: MEMORY_TYPES) -> str:
        if isinstance(comm, C_POP): raise AttributeError("Command pop is not available on the constant memory section")
        return f'''//Push a constant value onto the stack
@{str(comm.arg2)}
D=A
@R0
A=M
M=D
//Advance the stack pointer
@R0
M=M+1'''

    def _basic_segments(self, comm: MEMORY_TYPES) -> str:
        segment = BASIC_SEGMENT_MAP[comm.arg1]
        if isinstance(comm, C_POP): value = f'''// popping a {comm.arg1} segment
@{str(segment)}
D=M
@{comm.arg2}
D=D+A
@addr_{self.index}
M=D
//moves back the stack pointer
@R0
M=M-1
A=M
D=M
@addr_{self.index}
A=M
M=D
'''
        else: value =  f'''// pushing a {comm.arg1} segment
@{str(segment)}
D=M
@{comm.arg2}
A=D+A
D=M
@R0
M=M+1
A=M-1
M=D
'''
        self.index += 1
        return value

    def _temp(self, comm: MEMORY_TYPES) -> str:
        arg_str = str(comm.arg2 + 5)
        if isinstance(comm, C_POP): return f"""// popping temp variable {str(comm.arg2)}
@R0
M=M-1
A=M
D=M
@{arg_str}
M=D
"""
        else: return f"""// pushing temp variable {str(comm.arg2)}
@{arg_str}
D=M
@R0
M=M+1
A=M-1
M=D
"""

    def _pointer(self, comm:  MEMORY_TYPES):
        if comm.arg2 not in [0, 1]: raise ValueError('pointer must be 0 or 1')
        this_that = THIS_THAT[comm.arg2]
        if isinstance(comm, C_POP): return f'''// pops pointer value
@R0
M=M-1
A=M
D=M
@{this_that}
M=D
'''
        else: return f'''// pushes pointer value
@{this_that}
D=M
@R0
M=M+1
A=M-1
M=D
'''

    def _static(self, comm: MEMORY_TYPES, file_name: str):
        if isinstance(comm, C_POP): return f"""//Popping static variable
@R0
M=M-1
A=M
D=M
@{file_name}.{str(comm.arg2)}
M=D
"""
        else: return f"""//Pushing static Variable
@{file_name}.{str(comm.arg2)}
D=M
@R0
M=M+1
A=M-1
M=D
"""
