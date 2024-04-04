from dataclasses import dataclass

KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', "do", 'if', 'else', 'while', 'return']
SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']


@dataclass
class Keyword:
    value: str

    def __post__init__(self):
        assert self.value in KEYWORDS, f"Invalid keyword {self.value}"

    def __str__(self):
        return f"<keyword> {self.value} </keyword>"


@dataclass
class Symbol:
    value: str

    def __post__init__(self):
        assert self.value in SYMBOLS, f"Invalid symbol {self.value}"

    def __str__(self):
        return f"<symbol> {self.value} </symbol>"


@dataclass
class Identifier:
    value: str

    def __post__init__(self):
        assert self.value.replace("_", "").isalnum(), f"Invalid identifier {self.value}"
        assert not self.value[0].isnumeric(), f"Invalid identifier {self.value} cannot start with a number"

    def __str__(self):
        return f"<identifier> {self.value} </identifier>"


@dataclass
class IntegerConstant:
    value: int

    def __post__init__(self):
        assert isinstance(self.value, int), f"Invalid integer {self.value}"
        assert 0 <= self.value <= 32767, f"Invalid integer {self.value}, integer must be between 0 and 32767"

    def __str__(self):
        return f"<integerConstant> {self.value} </integerConstant>"


@dataclass
class StringConstant:
    value: str

    def __post__init__(self):
        assert isinstance(self.value, str), f"Invalid string {self.value}"
        assert self.value.find('"') == -1, f"Invalid string {self.value}, string cannot contain double quotes"
        assert self.value.find('\n') == -1, f"Invalid string {self.value}, string cannot contain newline characters"

    def __str__(self):
        return f"<stringConstant> {self.value} </stringConstant>"
