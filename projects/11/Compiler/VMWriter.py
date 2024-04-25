from Tokens import Identifier

from SymbolTable import Table

SEGMENTS = ['CONST', 'ARG', 'LOCAL', 'STATIC', 'THIS', 'THAT', 'POINTER', 'TEMP']
COMMANDS = ['ADD', 'SUB', 'NEG', 'EQ', 'GT', 'LT', 'AND', 'OR', 'NOT']


class CodeWriter:
    def _write_push_pop(self, push: bool, segment: str, index: int) -> str:
        assert segment in SEGMENTS, f"Invalid segment {segment}"
        return f"{'push' if push else 'pop'} {segment} {index}"

    def write_push(self, segment: str, index: int) -> str:
        return self._write_push_pop(True, segment, index)

    def write_pop(self, segment: str, index: int) -> str:
        return self._write_push_pop(False, segment, index)

    def write_arithmetic(self, command: str) -> str:
        assert command in COMMANDS, f"Invalid command {command}"
        return command

    def write_label(self, label: str) -> str:
        return f"label {label}"

    def write_goto(self, label: str) -> str:
        return f"goto {label}"

    def write_if(self, label: str) -> str:
        return f"if-goto {label}"

    def write_call(self, class_name: str, name: str, n_args: int) -> str:
        return f"call {class_name}.{name} {n_args}"

    def write_function(self, class_name: str, name: str, n_locals: int) -> str:
        return f"function {class_name}.{name} {n_locals}"

    def write_return(self) -> str:
        return "return"
