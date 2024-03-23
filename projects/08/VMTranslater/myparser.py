from commands import C_RETURN, C_ARITHMETIC, C_PUSH, C_POP, C_IF_GOTO, C_CALL, \
    C_GOTO, C_LABEL, C_FUNCTION, Command, ARITHMETIC_COMMANDS


class Parser:
    def parse(self, file: str) -> list[Command]:
        lines = [line for line in file.splitlines() if line.strip() != '' and not line.startswith('//')]
        lines = [line.split('//')[0].strip() for line in lines if line.strip()]
        return [self.single(line) for line in lines if line.strip()]

    def single(self, line: str) -> Command:
        values = line.split(" ")
        if len(values) == 1: return self.lenOne(values[0])
        elif len(values) == 2: return self.lenTwo(values[0], values[1])
        elif len(values) == 3: return self.lenThree(values[0], values[1], int(values[2]))
        else: raise NotImplementedError(f"No Functions of length greater than 3 have been implemented: {' '.join(values)}")

    def lenOne(self, arg1: str) -> Command:
        arg1 = arg1.strip()
        if arg1 == "return": return C_RETURN()
        elif arg1 in ARITHMETIC_COMMANDS: return C_ARITHMETIC(arg1)
        else: raise NotImplementedError(f"Function of length 1 not implemented {arg1}")

    def lenTwo(self, arg1: str, arg2: str) -> Command:
        if arg1 == "label": return C_LABEL(arg2)
        elif arg1 == "goto": return C_GOTO(arg2)
        elif arg1 == "if-goto": return C_IF_GOTO(arg2)
        else: raise NotImplementedError(f"Function of length 2 not implemented: {arg1} {arg2}")

    def lenThree(self, arg1: str, arg2: str, arg3: int) -> Command:
        if arg1 == "push": return C_PUSH(arg2, arg3)
        elif arg1 == "pop": return C_POP(arg2, arg3)
        elif arg1 == "function": return C_FUNCTION(arg2, arg3)
        elif arg1 == "call": return C_CALL(arg2, arg3)
        else: raise NotImplementedError(f"Function of length 2 not implemented: {arg1} {arg2} {arg3}")
