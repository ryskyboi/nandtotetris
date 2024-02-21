SYMBOL_TABLE = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}

class Symbols:
    def _first_pass(self, data: str) -> str:
        offset = 0
        split_data = data.split("\n")
        data_2 = split_data.copy()
        for i, data in enumerate(split_data):
            if not data.strip():
                continue
            if data[0] == "(":
                SYMBOL_TABLE[data[1: data.find(")")]] = i - offset
                data_2 = data_2[:i - offset] + data_2[i - offset + 1:]
                offset += 1
        return "\n".join(data_2)

    def _secound_pass(self, data: str) -> str:
        split_data = data.split("\n")
        new_data: list[str] = []
        running_count = 16
        for line in split_data:
            if line[0] != "@":
                new_data.append(line)
                continue
            symbol = line[1:]
            if symbol.isdigit():
                new_data.append(line)
                continue
            if symbol not in SYMBOL_TABLE:
                SYMBOL_TABLE[symbol] = running_count
                running_count += 1
            new_data.append(line.replace(symbol, str(SYMBOL_TABLE[symbol])))
        return "\n".join(new_data)

    def run(self, data: str) -> str:
        data = self._first_pass(data)
        data = self._secound_pass(data)
        return data
