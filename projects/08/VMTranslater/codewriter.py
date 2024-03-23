from commands import C_ARITHMETIC, C_CALL, C_FUNCTION, C_GOTO, C_IF_GOTO, \
    C_LABEL, C_POP, C_PUSH, C_RETURN, Command

from assembler_commands.memory_access import Memory
from assembler_commands.stack_arithmetic import Arithmetic
from assembler_commands.branching import Branching


class Compile:
    def __init__(self):
        self.memory = Memory()
        self.arithmetic = Arithmetic()
        self.branching = Branching()

    def _single_execution(self, command: Command, file_name: str) -> str:
        if isinstance(command, C_POP) or isinstance(command, C_PUSH): return self.memory.access(command, file_name)
        elif isinstance(command, C_ARITHMETIC): return self.arithmetic.operate(command)
        elif isinstance(command, C_CALL): return self.branching.call(command)
        elif isinstance(command, C_RETURN): return self.branching.return_value()
        elif isinstance(command, C_GOTO): return self.branching.goto(command)
        elif isinstance(command, C_IF_GOTO): return self.branching.if_goto(command)
        elif isinstance(command, C_LABEL): return self.branching.label(command)
        elif isinstance(command, C_FUNCTION): return self.branching.function(command)
        else: raise NotImplementedError()

    def run(self, commands: list[Command], file_name: str) -> str:
        return '\n'.join([self._single_execution(comm, file_name) for comm in commands])

    def initializer(self) -> str:
        return '''// initializes the assembler
@256
D=A
@R0
M=D
''' + self.branching.call(C_CALL("Sys.init", 0))
