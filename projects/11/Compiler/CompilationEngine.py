from VMWriter import CodeWriter
from SymbolTable import Tables
from Tokens import Token, IntegerConstant, StringConstant, Identifier

RETURN_TYPE = tuple[str, list[Token]]
TYPES = ["int", "char", "boolean"]
OPS = ["+", "-", "*", "/", "&", "|", "<", ">", "="]
OP_MAP = {"+": "add", "-": "sub", "*": "call Math.multiply 2", "/": "call Math.divide 2", "&": "and", "|": "or", "<": "lt", ">": "gt", "=": "eq"}


class Compiler:
    def __init__(self) -> None:
        self.tables = Tables()
        self.writer = CodeWriter()
        self.label = 0

    def main(self, data: list[Token]) -> str:
        vm = self.CompileClass("", data)
        return vm

    def CompileClass(self, vm: str, data: list[Token]) -> str:
        assert data[0].value == "class", f"Not a class: {data[0].value}"
        assert isinstance(data[1], Identifier), f"Invalid class name: {data[1].value}"
        assert data[2].value == "{", f"Invalid class start: {data[2].value}"
        assert data[-1].value == "}", f"Invalid class end: {data[-1].value}"
        self.class_name = data[1].value
        data = data[3:-1]
        while data[0].value == "field" or data[0].value == "static": vm, data = self.CompileClassVarDec(vm, data)
        while data[0].value == "constructor" or data[0].value == "function" or data[0].value == "method":
            vm, data = self.CompileSubroutine(vm, data)
            if len(data) == 0: break
        self.tables.reset_class_table()
        return vm

    def CompileClassVarDec(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        assert data[0].value == "field" or data[0].value == "static", f"Not a class var dec: {data[0].value}"
        assert data[1].value in TYPES or isinstance(data[1], Identifier), f"Invalid class var dec type: {data[1].value}"
        assert isinstance(data[2], Identifier), f"Invalid class var dec name: {data[2].value}"
        _kind, _type = str(data[0].value), str(data[1].value)
        self.tables.add_entry(data[2].value, _type, _kind)
        data = data[3:]
        while data[0].value == ",":
            assert isinstance(data[1], Identifier), f"Invalid class var dec name: {data[1].value}"
            self.tables.add_entry(data[1].value, _type, _kind)
            data = data[2:]
        assert data[0].value == ";", f"Invalid class var dec end: {data[0].value}"
        return vm, data[1:]

    def CompileSubroutine(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        assert data[0].value in ["constructor", "function", "method"], f"Not a subroutine: {data[0].value}"
        assert data[1].value in TYPES + ["void"] or isinstance(data[1], Identifier), f"Invalid subroutine return type: {data[1].value}"
        assert isinstance(data[2], Identifier), f"Invalid subroutine name: {data[2].value}"
        assert data[3].value == "(", f"Invalid subroutine start: {data[3].value}"
        _kind, _name = data[0].value, str(data[2].value)
        if _kind == "method": self.tables.add_entry("this", self.class_name, "arg")
        vm, data = self.CompileParameterList(vm, data[4:])
        assert data[0].value == ")", f"Invalid subroutine end: {data[0].value}"
        assert data[1].value == "{", f"Invalid subroutine start: {data[1].value}"
        data = data[2:]
        while data[0].value == "var": vm, data = self.CompileVarDec(vm, data)
        num = self.tables.get_var_count("var")
        if _kind == "constructor":
            vm += self.writer.write_function(self.class_name, _name, num)
            vm += self.writer.write_push("constant", self.tables.get_var_count("field")) + self.writer.write_call("Memory", "alloc", 1) + self.writer.write_pop("pointer", 0)
        elif _kind == "method":
            vm += self.writer.write_function(self.class_name, _name, num) + self.writer.write_push("argument", 0) + self.writer.write_pop("pointer", 0)
        else:
            vm += self.writer.write_function(self.class_name, _name, num)
        while data[0].value in ["do", "let", "while", "if", "return"]: vm, data = self.CompileStatements(vm, data)
        assert data[0].value == "}", f"Invalid subroutine end: {data[0].value}"
        self.tables.reset_subroutine_table()
        return vm, data[1:]

    def CompileParameterList(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        while data[0].value in TYPES or isinstance(data[0], Identifier):
            assert data[0].value in TYPES or isinstance(data[0], Identifier), f"Invalid parameter type: {data[0].value}"
            assert isinstance(data[1], Identifier), f"Invalid parameter name: {data[1].value}"
            self.tables.add_entry(data[1].value, str(data[0].value), "arg")
            data = data[2:]
            if data[0].value == ",":
                data = data[1:]
        return vm,  data

    def CompileVarDec(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        assert data[0].value == "var", f"Not a var dec: {data[0].value}"
        assert data[1].value in TYPES or isinstance(data[1], Identifier), f"Invalid var dec type: {data[1].value}"
        assert isinstance(data[2], Identifier), f"Invalid var dec name: {data[2].value}"
        _type = str(data[1].value)
        self.tables.add_entry(data[2].value, _type, "var")
        data = data[3:]
        while data[0].value == ",":
            assert isinstance(data[1], Identifier), f"Invalid var dec name: {data[1].value}"
            self.tables.add_entry(data[1].value, _type, "var")
            data = data[2:]
        assert data[0].value == ";", f"Invalid var dec end: {data[0].value}"
        return vm, data[1:]

    def CompileStatements(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        while data[0].value in ["let", "if", "while", "do", "return"]:
            if data[0].value == "let": vm, data = self.CompileLet(vm, data)
            elif data[0].value == "if": vm, data = self.CompileIf(vm, data)
            elif data[0].value == "while": vm, data = self.CompileWhile(vm, data)
            elif data[0].value == "do": vm, data = self.CompileDo(vm, data)
            elif data[0].value == "return": vm, data = self.CompileReturn(vm, data)
        return vm, data

    def CompileDo(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "do", f"Not a do: {data[0].value}"
        assert isinstance(data[1], Identifier), f"Invalid do name: {data[1].value}"
        name = data[1].value
        if data[2].value == ".":
            assert isinstance(data[3], Identifier), f"Invalid do name: {data[3].value}"
            _class, _func = name, data[3].value
            _add = 0
            if self.tables.KindOf(name) != "none":
                _class = self.tables.TypeOf(name)
                _add = 1
                vm += self.writer.write_push(*self._table_caller(data[1]))
            data = data[4:]
        else:
            _class = self.class_name
            _func = name; data = data[2:]
            vm += self.writer.write_push("pointer", 0)
            _add = 1
        assert data[0].value == "(", f"Invalid do start: {data[0].value}"
        vm, data, num = self.CompileExpressionList(vm, data[1:])
        assert data[0].value == ")", f"Invalid do end: {data[0].value}"
        assert data[1].value == ";", f"Invalid do end: {data[1].value}"
        return vm + self.writer.write_call(_class, _func, num + _add ) + self.writer.write_pop("temp", 0), data[2:]

    def CompileLet(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "let", f"Not a let: {data[0].value}"
        assert isinstance(data[1], Identifier), f"Invalid let name: {data[1].value}"
        id = data[1]
        if data[2].value == "[":
            vm, data = self.CompileExpression(vm, data[3:])
            assert data[0].value == "]", f"Invalid let end: {data[0].value}"
            vm += self.writer.write_push(*self._table_caller(id)) + self.writer.write_arithmetic("add")
            add_to_stack = self.writer.write_pop("temp", 0) + self.writer.write_pop("pointer", 1) + self.writer.write_push("temp", 0) + self.writer.write_pop("that", 0)
            data = data[1:]
        else:
            data = data[2:]
            add_to_stack = self.writer.write_pop(*self._table_caller(id))
        assert data[0].value == "=", f"Let requires an equality: {data[0].value}"
        vm, data = self.CompileExpression(vm, data[1:])
        assert data[0].value == ";", f"Invalid let end: {data[0].value}"
        return vm + add_to_stack, data[1:]

    def CompileWhile(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "while", f"Not a while: {data[0].value}"
        assert data[1].value == "(", f"Invalid while expression start: {data[1].value}"
        l1, l2 = f"LABEL_{self.label}", f"LABEL_{self.label + 1}"
        self.label += 2
        vm += self.writer.write_label(l1)
        vm, data = self.CompileExpression(vm, data[2:])
        assert data[0].value == ")", f"Invalid while expression end: {data[0].value}"
        assert data[1].value == "{", f"Invalid while start: {data[1].value}"
        vm += self.writer.write_arithmetic("not") + self.writer.write_if(l2)
        vm, data = self.CompileStatements(vm, data[2:])
        vm += self.writer.write_goto(l1) + self.writer.write_label(l2)
        assert data[0].value == "}", f"Invalid while end: {data[0].value}"
        return vm, data[1:]

    def CompileReturn(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "return", f"Not a return: {data[0].value}"
        self.writer.write_push("pointer", 0)
        if data[1].value != ";":
            if data[1].value == "this":
                vm += self.writer.write_push("pointer", 0)
                data = data[2:]
            else: vm, data = self.CompileExpression(vm, data[1:])
        else:
            data = data[1:]
            vm += self.writer.write_push("constant", 0)
        assert data[0].value == ";", f"Invalid return end: {data[0].value}"
        return vm + self.writer.write_return(), data[1:]

    def CompileIf(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "if", f"Not an if: {data[0].value}"
        assert data[1].value == "(", f"Invalid if expression start: {data[1].value}"
        vm, data = self.CompileExpression(vm, data[2:])
        assert data[0].value == ")", f"Invalid if expression end: {data[0].value}"
        assert data[1].value == "{", f"Invalid if start: {data[1].value}"
        l1, l2 = f"LABEL_{self.label}", f"LABEL_{self.label + 1}"
        self.label += 2
        vm += self.writer.write_if(l1) + self.writer.write_goto(l2) + self.writer.write_label(l1)
        vm, data = self.CompileStatements(vm, data[2:])
        assert data[0].value == "}", f"Invalid if end: {data[0].value}"
        data = data[1:]
        if data[0].value == "else":
            l3 = f"LABEL_{self.label}"
            self.label += 1
            vm += self.writer.write_goto(l3) + self.writer.write_label(l2)
            assert data[1].value == "{", f"Invalid else start: {data[1].value}"
            vm, data = self.CompileStatements(vm, data[2:])
            assert data[0].value == "}", f"Invalid if end: {data[0].value}"
            data = data[1:]
            vm += self.writer.write_label(l3)
        else: vm += self.writer.write_label(l2)
        return vm, data

    def CompileExpression(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        vm, data = self.CompileTerm(vm, data)
        while data[0].value in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            op = OP_MAP[data[0].value]  # type: ignore
            vm, data = self.CompileTerm(vm, data[1:])
            vm += self.writer.write_arithmetic(op)
        return vm, data

    def CompileTerm(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        if isinstance(data[0], IntegerConstant): return vm + self.writer.write_push("constant", data[0].value), data[1:]
        elif isinstance(data[0], StringConstant):
            vm += f"push constant {len(data[0].value)}\ncall String.new 1\n" + "".join(f"push constant {ord(char)}\ncall String.appendChar 2\n" for char in data[0].value)
            return vm, data[1:]
        elif data[0].value == "this": return vm + "push pointer 0\n", data[1:]  # This is the base address of the current object
        elif data[0].value == "true": return vm +"push constant 0\nnot\n", data[1:]
        elif data[0].value == "false" or data[0].value == "null": return vm + "push constant 0\n", data[1:]
        elif isinstance(data[0], Identifier):
            if data[1].value == "[":
                vm += self.writer.write_push(*self._table_caller(data[0]))
                vm, data = self.CompileExpression(vm, data[2:])
                vm += self.writer.write_arithmetic("add") + self.writer.write_pop("pointer", 1) + self.writer.write_push("that", 0)
                assert data[0].value == "]", f"Invalid term end: {data[0].value}"  # type: ignore
            elif data[1].value == "(":
                vm += self.writer.write_push("pointer", 0)
                _value = str(data[0].value)
                vm, data, num = self.CompileExpressionList(vm, data[2:])
                print(str(self.class_name), str(data[2].value), num, 0)
                vm += self.writer.write_call(self.class_name, _value, num)
                assert data[0].value == ")", f"Invalid term end: {data[0].value}"  # type: ignore
            elif data[1].value == ".":
                assert isinstance(data[2], Identifier), f"Invalid subroutine name: {data[2].value}"
                assert data[3].value == "(", f"Invalid subroutine start: {data[3].value}"
                _object, _func_name = self.tables.KindOf(str(data[0].value)), str(data[2].value)
                if _object == "none":
                    _add = 0
                    class_name = data[0].value
                else:
                    _add = 1
                    vm += self.writer.write_push(*self._table_caller(data[0]))   # type: ignore
                    class_name = self.tables.TypeOf(str(data[0].value))
                vm, data, num = self.CompileExpressionList(vm, data[4:])
                vm += self.writer.write_call(str(class_name), _func_name, num + _add)
                assert data[0].value == ")", f"Invalid term end: {data[0].value}"  # type: ignore
            else:
                vm += self.writer.write_push(*self._table_caller(data[0])) # type: ignore
            return vm, data[1:]
        elif data[0].value == "(":
            vm, data = self.CompileExpression(vm, data[1:])
            assert data[0].value == ")", f"Invalid term end: {data[0].value}"
            return vm, data[1:]
        elif data[0].value in ["-", "~"]:
            op = {"~": "not", "-": "neg"}[data[0].value]  # type: ignore
            vm, data = self.CompileTerm(vm, data[1:])
            return vm + self.writer.write_arithmetic(op), data
        else:
            raise ValueError(f"Invalid term: {data[0].value}")

    def CompileExpressionList(self, vm: str, data: list[Token])  -> tuple[str, list[Token], int]:
        num = 0
        while data[0].value != ")":
            vm, data = self.CompileExpression(vm, data)
            if data[0].value == ",":
                data = data[1:]
            num += 1
        return vm, data, num

    def _table_caller(self, token: Identifier) -> tuple[str, int]:
        # ? Not sure where to put this
        assert isinstance(token, Identifier), f"Invalid token: {token}"
        name = token.value
        kind = self.tables.KindOf(name)
        index = self.tables.IndexOf(name)
        return kind, index
