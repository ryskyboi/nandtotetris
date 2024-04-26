from Tokenizer import Tokenize
from CompilationEngine import Compiler

import argparse
from typing import Tuple
from pathlib import Path
from os import listdir


class Analyze:
    def __init__(self) -> None:
        self.tokenize = Tokenize()
        self.engine = Compiler()

    def _file_handler(self, file_from: str | Path) -> Tuple[list[Path], Path]:
        if isinstance(file_from, str): file_from = Path(file_from)
        is_file = file_from.is_file()
        if is_file: return_files = [file_from]
        else: return_files = [file_from / Path(x) for x in listdir(file_from) if x.find(".jack") != -1]
        return return_files, file_from.parent if is_file else file_from

    def main(self, file_from: Path | str):
        files, dir_to = self._file_handler(file_from)
        for file in files:
            if not file.name.endswith('.jack'): continue
            with open(file, "r") as f, open(dir_to / (file.name.strip('.jack') + ".vm"), "w") as output:
                lines = [line for line in f.read().splitlines() if line.strip() != '' and not line.startswith('//')]
                lines = self._remove_multiline_comments(lines)
                lines = [item for sublist in [line.split('//')[0].strip() for line in lines if line.strip()] for item in sublist.split(' ')]
                tokens = self.tokenize.main(lines)
                output.write(self.engine.main(tokens))

    def _remove_multiline_comments(self, lines: list[str]) -> list[str]:
        _value = []
        while lines:
            if lines[0].strip().startswith(r"/*"):
                while not lines[0].strip().endswith(r"*/"):
                    lines.pop(0)
                lines.pop(0)
            else:
                _value.append(lines.pop(0))
        return _value

    def parse_and_run(self):
        parser = argparse.ArgumentParser(description="Compile a Jack file or folder of files to VM code")
        parser.add_argument("file_from", type=str, help="The file to be compiled")
        args = parser.parse_args()
        self.main(args.file_from)


if __name__ == "__main__":
    Analyze().parse_and_run()
