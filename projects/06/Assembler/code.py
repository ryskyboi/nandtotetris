from typing import Union

from data import ACommand, CCommand, COMPARE, JUMP, DEST


class CodeGen:
    def generate_all(self, parsed_commands: list[Union[ACommand, CCommand]]) -> str:
        output = []
        for i, value in enumerate(parsed_commands):
            if isinstance(value, CCommand):
                output.append(self._c(value))
            elif isinstance(value, ACommand):
                output.append(self._a(value))
            else:
                raise TypeError(f"Command does not have the required type { value }")
        return "\n".join(output)

    def _c(self, command: CCommand) -> str:
        c = COMPARE[command.comp]
        d = DEST[command.dest]
        j = JUMP[command.jump]
        return "111" + c + d + j

    def _a(self, command: ACommand) -> str:
        binary = bin(command.value).replace("0b", "")
        padding = 16 - len(binary)
        return padding * "0" + binary
