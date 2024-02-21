import argparse
from typing import Tuple
from pathlib import Path

from code import CodeGen
from myparser import Parser

class Main:
    def _file_handler(self, file_from: str | Path, file_to: str | Path) -> Tuple[Path, Path]:
        if isinstance(file_from, str):
            file_from = Path(file_from)
        if file_from.is_file():
            name = file_from.name
        else:
            raise FileNotFoundError(f"{file_from} is not a file")
        if file_to == "none":
            file_to = Path(__name__).parent / "Myassemblyfiles" / (name[:-4] + ".hack")
        elif isinstance(file_to, str):
            file_to = Path(file_to)
        return file_from, file_to

    def main(self, file_from: str | Path, file_to: str | Path):
        file_from, file_to = self._file_handler(file_from, file_to)
        with open(file_from, 'r') as file, open(file_to, 'w') as output:
            lines = [line for line in file if line.strip()]
            data = ''.join(lines)
            parsed = Parser().parse(data)
            code = CodeGen().generate_all(parsed)
            output.write(code)

    def parse_and_run(self):
        parser = argparse.ArgumentParser(description="Assembler for Hack Assembly Language")
        parser.add_argument("file_from", type=str, help="The file to be assembled")
        parser.add_argument("file_to", type=str, nargs="?", default='none', help="The file to be written to")
        args = parser.parse_args()
        self.main(args.file_from, args.file_to)

if __name__ == "__main__":
    Main().parse_and_run()
