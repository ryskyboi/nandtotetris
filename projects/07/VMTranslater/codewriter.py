from commands import C_ARITHMETIC, C_CALL, C_FUNCTION, C_GOTO, C_IF_GOTO, \
    C_LABEL, C_POP, C_PUSH, C_RETURN, Command

from assembler_commands.memory_access import Memory
from assembler_commands.stack_arithmetic import Arithmetic


class Compile:
    def __init__(self):
        self.memory = Memory()
        self.arithmetic = Arithmetic()

    def _single_execution(self, command: Command) -> str:
        if isinstance(command, C_POP) or isinstance(command, C_PUSH): return self.memory.access(command)
        elif isinstance(command, C_ARITHMETIC): return self.arithmetic.operate(command)
        else: raise NotImplementedError()

    def run(self, commands: list[Command]) -> str:
        return '\n'.join([self._single_execution(comm) for comm in commands])
