import argparse
from typing import Tuple
from pathlib import Path

from myparser import Parser
from codewriter import Compile


class Main:
    def __init__(self):
        self.parser = Parser()
        self.codewriter = Compile()

    def _file_handler(self, file_from: str | Path, file_to: str | Path) -> Tuple[Path, Path]:
        if isinstance(file_from, str):
            file_from = Path(file_from)
        if file_from.is_file():
            name = file_from.name
        else:
            raise FileNotFoundError(f"{file_from} is not a file")
        if file_to == "none":
            file_to = file_from.parent / (name.strip('vm') + "asm")
        elif isinstance(file_to, str):
            file_to = Path(file_to)
        return file_from, file_to

    def main(self, file_from: str | Path, file_to: str | Path):
        file_from, file_to = self._file_handler(file_from, file_to)
        with open(file_from, 'r') as file, open(file_to, 'w') as output:
            commands = self.parser.parse(file.read())
            parsed = self.codewriter.run(commands)
            output.write(parsed)

    def parse_and_run(self):
        parser = argparse.ArgumentParser(description="Complier from Stack language to Hack machine code")
        parser.add_argument("file_from", type=str, help="The file to be compiled")
        parser.add_argument("file_to", type=str, nargs="?", default='none', help="The file to be written to")
        args = parser.parse_args()
        self.main(args.file_from, args.file_to)

if __name__ == "__main__":
    Main().parse_and_run()
