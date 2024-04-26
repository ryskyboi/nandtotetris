from dataclasses import dataclass


TABLE_TYPES = ["static", "field", "arg", "var"]
MAP = {"arg": "argument", "var": "local", "static": "static", "field": "this"}


@dataclass
class TableEntry:
    type: str
    kind: str
    index: int


class Tables:
    def __init__(self) -> None:
        self.class_table: dict[str, TableEntry] = {}
        self.subroutine_table: dict[str, TableEntry] = {}
        self.var_count = {x: 0 for x in TABLE_TYPES}

    def reset_subroutine_table(self) -> None:
        self.subroutine_table = {}
        self.var_count["arg"] = 0
        self.var_count["var"] = 0

    def reset_class_table(self) -> None:
        self.class_table = {}
        self.var_count["static"] = 0
        self.var_count["field"] = 0

    def add_entry(self, name: str, type: str, kind: str) -> None:
        if kind not in TABLE_TYPES: raise ValueError(f"Invalid kind {kind}")
        if kind == "static" or kind == "field":
            self.class_table[name] = TableEntry(type, kind, self.var_count[kind])
        else:
            self.subroutine_table[name] = TableEntry(type, kind, self.var_count[kind])
        self.var_count[kind] += 1

    def get_var_count(self, kind: str) -> int:
        if kind not in TABLE_TYPES: raise ValueError(f"Invalid kind {kind}")
        return self.var_count[kind]

    def KindOf(self, name: str) -> str:
        if name in self.subroutine_table:
            return MAP[self.subroutine_table[name].kind]
        elif name in self.class_table:
            return MAP[self.class_table[name].kind]
        return "none"

    def TypeOf(self, name: str) -> str:
        if name in self.subroutine_table:
            return self.subroutine_table[name].type
        elif name in self.class_table:
            return self.class_table[name].type
        return "none"

    def IndexOf(self, name: str) -> int:
        if name in self.subroutine_table:
            return self.subroutine_table[name].index
        elif name in self.class_table:
            return self.class_table[name].index
        return -1

    def push_pop(self, name: str, push: bool) -> str:
        return f"{'push' if push else 'pop'} {self.KindOf(name)} {self.IndexOf(name)}"
