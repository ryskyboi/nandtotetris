from typing import Union
from commands import C_POP, C_PUSH

MEMORY_TYPES = Union[C_POP, C_PUSH]


class Memory:
    def access(self, comm: MEMORY_TYPES):
        if comm.arg1 == 'constant': return self._constant(comm)
        else: raise NotImplementedError("Non constant memory is not yet implemented")

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
