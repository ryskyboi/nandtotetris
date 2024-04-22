import re

from Tokens import Token, Keyword, Symbol, IntegerConstant, StringConstant, Identifier, KEYWORDS, SYMBOLS


class Tokenize():
    def main(self, data: list[str]) -> list[Token]:
        tokens: list[Token] = []
        pattern = '(' + '|'.join(map(re.escape, SYMBOLS)) + ')'
        data = [item for sublist in [re.split(pattern, item) for item in data] for item in sublist if item.strip()]
        data = self.string_handeler(data)
        for value in data:
            if value in KEYWORDS: tokens.append(Keyword(value))
            elif value in SYMBOLS: tokens.append(Symbol(value))
            elif value.isnumeric(): tokens.append(IntegerConstant(int(value)))
            elif value.startswith('"') and value.endswith('"'): tokens.append(StringConstant(value[1:-1]))
            else: tokens.append(Identifier(value))
        return tokens

    def string_handeler(self, data: list[str]):
        new_list: list[str] = []
        while data:
            if data[0].startswith('"'):
                _value = data.pop(0)
                while not data[0].endswith('"'):
                    _value += data.pop(0)
                _value += data.pop(0)
                new_list.append(_value)
            else:
                new_list.append(data.pop(0))
        return new_list
