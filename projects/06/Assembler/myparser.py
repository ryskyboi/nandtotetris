from typing import Union

from data import CCommand, ACommand

class Parser:
    def _parseC(self, command: str) -> CCommand:
        equals = command.find("=")
        if equals != -1:
            dest = command[0:equals]
            command = command[equals + 1:]
        else:
            dest = "NA"
        semi_colon = command.find(";")
        if semi_colon != -1:
            jump = command[semi_colon + 1:]
            command = command[:semi_colon]
        else:
            jump = "NA"
        return CCommand(dest, command, jump)

    def parse(self, file: str) -> list[Union[ACommand, CCommand]]:
        parsed_commands: list[Union[ACommand, CCommand]] = []
        commands = file.split("\n")
        commands = [command.strip() for command in commands]
        for command in commands:
            if not command.strip():
                continue
            if command[:2] == "//":
                continue
            if command[0] == "@":
                parsed_commands.append(ACommand(int(command[1:])))
            else:
                parsed_commands.append(self._parseC(command))
        return parsed_commands
