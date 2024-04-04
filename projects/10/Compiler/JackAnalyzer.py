import argparse
from typing import Tuple
from pathlib import Path
from os import listdir



class Analyze:
    ## ! This is very lazy programming, most of this code is copy-pasted from 08/VMTranslater/main.py
    def __init__(self)
    
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
    
    
    def parse_and_run(self):
        parser = argparse.ArgumentParser(description="Compile a Jack file or folder of files to VM code")
        parser.add_argument("file_from", type=str, help="The file to be compiled")
        parser.add_argument("file_to", type=str, nargs="?", default='none', help="The file to be written to")
        args = parser.parse_args()
        self.main(args.file_from, args.file_to)
