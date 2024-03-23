import argparse
from typing import Tuple
from pathlib import Path
from os import listdir

from myparser import Parser
from codewriter import Compile


class Main:
    def __init__(self):
        self.parser = Parser()
        self.codewriter = Compile()

    def _file_handler(self, file_from: str | Path, file_to: str | Path) -> Tuple[list[Path], Path]:
        if isinstance(file_from, str): file_from = Path(file_from)
        is_file = file_from.is_file()
        if is_file:
            name = file_from.name
            return_files = [file_from]
        else:
            name = file_from.name
            return_files = [file_from / Path(x) for x in listdir(file_from) if x.find(".vm") != -1]
        if file_to == "none": file_to = (file_from.parent if is_file else file_from) / (name.strip('.vm') + ".asm")
        elif isinstance(file_to, str): file_to = Path(file_to)
        return return_files, file_to

    def main(self, file_from: str | Path, file_to: str | Path):
        _file_from, _file_to = self._file_handler(file_from, file_to)
        all_parsed = []
        if len(_file_from) != 1: all_parsed.append(self.codewriter.initializer())
        with open(_file_to, 'w') as output:
            for _file in _file_from:
                with open(_file, 'r') as file:
                    commands = self.parser.parse(file.read())
                    all_parsed.append(self.codewriter.run(commands, _file.name.strip('.vm')))
            output.write("\n".join(all_parsed))

    def parse_and_run(self):
        parser = argparse.ArgumentParser(description="Complier from Stack language to Hack machine code")
        parser.add_argument("file_from", type=str, help="The file to be compiled")
        parser.add_argument("file_to", type=str, nargs="?", default='none', help="The file to be written to")
        args = parser.parse_args()
        self.main(args.file_from, args.file_to)

if __name__ == "__main__":
    Main().parse_and_run()
