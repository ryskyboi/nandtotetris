from itertools import count


from VMWriter import CodeWriter
from SymbolTable import Tables
from Tokens import Token, IntegerConstant, StringConstant, Identifier

RETURN_TYPE = tuple[str, list[Token]]
TYPES = ["int", "char", "boolean"]
OPS = ["+", "-", "*", "/", "&", "|", "<", ">", "="]
OP_MAP = {"+": "add", "-": "sub", "*": "call Math.multiply 2", "/": "call Math.divide 2", "&": "and", "|": "or", "<": "lt", ">": "gt", "=": "eq"}

class Compiler:
    def __init__(self) -> None:
        self.label = f"LABEL_{next(count())}"
        self.tables = Tables()
        self.writer = CodeWriter()

    def main(self, data: list[Token]) -> str:
        vm = self.CompileClass("", data)
        return vm

    def CompileClass(self, vm: str, data: list[Token]) -> str:
        assert data[0].value == "class", f"Not a class: {data[0].value}"
        assert isinstance(data[1], Identifier), f"Invalid class name: {data[1].value}"
        assert data[2].value == "{", f"Invalid class start: {data[2].value}"
        assert data[-1].value == "}", f"Invalid class end: {data[-1].value}"
        self.class_name = data[1].value
        data, final = data[3:-1], data[-1]
        while data[0].value == "field" or data[0].value == "static": vm, data = self.CompileClassVarDec(vm, data)
        while data[0].value == "constructor" or data[0].value == "function" or data[0].value == "method":
            vm, data = self.CompileSubroutine(vm, data)
            if len(data) == 0: break
        self.tables.reset_class_table()
        return vm + f"{final}\n </class> \n"

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
        if data[0].value == "method": self.tables.add_entry("this", self.class_name, "arg")  # Need to add this to the table
        vm += f"<subroutineDec>\n {data[0]}\n {data[1]}\n {self._table_caller(data[2])}\n {data[3]}\n"
        vm, data = self.CompileParameterList(vm, data[4:])
        assert data[0].value == ")", f"Invalid subroutine end: {data[0].value}"
        assert data[1].value == "{", f"Invalid subroutine start: {data[1].value}"
        vm += f"{data[0]}\n <subroutineBody>\n {data[1]}\n"
        data = data[2:]
        while data[0].value == "var": vm, data = self.CompileVarDec(vm, data)
        while data[0].value in ["do", "let", "while", "if", "return"]: vm, data = self.CompileStatements(vm, data)
        assert data[0].value == "}", f"Invalid subroutine end: {data[0].value}"
        self.tables.reset_subroutine_table()
        return vm + f" {data[0]} \n</subroutineBody> \n</subroutineDec> \n", data[1:]

    def CompileParameterList(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        vm += "<parameterList>\n"
        while data[0].value in TYPES:
            assert data[0].value in TYPES, f"Invalid parameter type: {data[0].value}"
            assert isinstance(data[1], Identifier), f"Invalid parameter name: {data[1].value}"
            self.tables.add_entry(data[1].value, str(data[0].value), "arg")
            vm += f"{data[0]}\n {self._table_caller(data[1])}\n"
            data = data[2:]
            if data[0].value == ",":
                vm += f"{data[0]}\n"
                data = data[1:]
        return vm + "</parameterList>\n", data

    def CompileVarDec(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        assert data[0].value == "var", f"Not a var dec: {data[0].value}"
        assert data[1].value in TYPES or isinstance(data[1], Identifier), f"Invalid var dec type: {data[1].value}"
        assert isinstance(data[2], Identifier), f"Invalid var dec name: {data[2].value}"
        _type = str(data[1].value)
        self.tables.add_entry(data[2].value, _type, "var")
        vm = f"{vm} <varDec>\n {data[0]}\n {data[1]}\n {self._table_caller(data[2])}\n"
        data = data[3:]
        while data[0].value == ",":
            assert isinstance(data[1], Identifier), f"Invalid var dec name: {data[1].value}"
            self.tables.add_entry(data[1].value, _type, "var")
            vm += f"{data[0]}\n {data[1]}\n"
            data = data[2:]
        assert data[0].value == ";", f"Invalid var dec end: {data[0].value}"
        return vm + f"{data[0]}\n </varDec> \n", data[1:]

    def CompileStatements(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        vm += "<statements>\n"
        while data[0].value in ["let", "if", "while", "do", "return"]:
            if data[0].value == "let": vm, data = self.CompileLet(vm, data)
            elif data[0].value == "if": vm, data = self.CompileIf(vm, data)
            elif data[0].value == "while": vm, data = self.CompileWhile(vm, data)
            elif data[0].value == "do": vm, data = self.CompileDo(vm, data)
            elif data[0].value == "return": vm, data = self.CompileReturn(vm, data)
        return vm + "</statements>\n", data

    def CompileDo(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "do", f"Not a do: {data[0].value}"
        assert isinstance(data[1], Identifier), f"Invalid do name: {data[1].value}"
        vm += f"<doStatement>\n {data[0]}\n {self._table_caller(data[1])}\n"
        if data[2].value == ".":
            assert isinstance(data[3], Identifier), f"Invalid do name: {data[3].value}"
            vm += f"{data[2]}\n {self._table_caller(data[3])}\n"
            data = data[4:]
        else: data = data[2:]
        assert data[0].value == "(", f"Invalid do start: {data[0].value}"
        vm += f"{data[0]}\n"
        vm, data, num = self.CompileExpressionList(vm, data[1:])
        assert data[0].value == ")", f"Invalid do end: {data[0].value}"
        assert data[1].value == ";", f"Invalid do end: {data[1].value}"
        return vm + f"{data[0]}\n {data[1]}\n </doStatement> \n", data[2:]

    def CompileLet(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "let", f"Not a let: {data[0].value}"
        assert isinstance(data[1], Identifier), f"Invalid let name: {data[1].value}"
        id = data[1]
        if data[2].value == "[":
            vm, data = self.CompileExpression(vm, data[3:])
            assert data[0].value == "]", f"Invalid let end: {data[0].value}"
            add_to_stack = ""  # ! Need to handle adding to arrays
            data = data[1:]
        else:
            data = data[2:]
            add_to_stack = self.writer.write_push(*self._table_caller(id)) + "\n"
        assert data[0].value == "=", f"Let requires an equality: {data[0].value}"
        vm, data = self.CompileExpression(vm, data[1:])
        assert data[0].value == ";", f"Invalid let end: {data[0].value}"
        return vm + add_to_stack, data[1:]

    def CompileWhile(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "while", f"Not a while: {data[0].value}"
        assert data[1].value == "(", f"Invalid while expression start: {data[1].value}"
        vm += f"<whileStatement>\n {data[0]}\n {data[1]}\n"
        vm, data = self.CompileExpression(vm, data[2:])
        assert data[0].value == ")", f"Invalid while expression end: {data[0].value}"
        assert data[1].value == "{", f"Invalid while start: {data[1].value}"
        vm += f"{data[0]}\n {data[1]}\n"
        vm, data = self.CompileStatements(vm, data[2:])
        assert data[0].value == "}", f"Invalid while end: {data[0].value}"
        return vm + f"{data[0]}\n </whileStatement> \n", data[1:]

    def CompileReturn(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "return", f"Not a return: {data[0].value}"
        vm += f"<returnStatement>\n {data[0]}\n"
        if data[1].value != ";":
            vm, data = self.CompileExpression(vm, data[1:])
        else: data = data[1:]
        assert data[0].value == ";", f"Invalid return end: {data[0].value}"
        return vm + f"{data[0]}\n </returnStatement> \n", data[1:]

    def CompileIf(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "if", f"Not an if: {data[0].value}"
        assert data[1].value == "(", f"Invalid if expression start: {data[1].value}"
        vm, data = self.CompileExpression(vm, data[2:])
        assert data[0].value == ")", f"Invalid if expression end: {data[0].value}"
        assert data[1].value == "{", f"Invalid if start: {data[1].value}"
        vm += self.writer.write_arithmetic("not") + "\n"
        L1 = self.label
        vm += self.writer.write_if(L1) + "\n"
        vm, data = self.CompileStatements(vm, data[2:])
        assert data[0].value == "}", f"Invalid if end: {data[0].value}"
        data = data[1:]
        if data[0].value == "else":
            vm += f"{data[0]}\n"
            assert data[1].value == "{", f"Invalid else start: {data[1].value}"
            vm += f"{data[1]}\n"
            vm, data = self.CompileStatements(vm, data[2:])
            assert data[0].value == "}", f"Invalid if end: {data[0].value}"
            vm += f"{data[0]}\n"
            data = data[1:]
        return vm + "</ifStatement> \n", data

    def CompileExpression(self, vm: str, data: list[Token]) -> RETURN_TYPE:
        vm, data = self.CompileTerm(vm, data)
        while data[0].value in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            op = OP_MAP[data[0].value]  # type: ignore
            vm, data = self.CompileTerm(vm, data[1:])
            vm += op + "\n"
        return vm, data

    def CompileTerm(self, vm: str, data: list[Token])  -> RETURN_TYPE:
        if isinstance(data[0], IntegerConstant):
            # ? what do we do with not integer constants
            return vm + f"push {data[0].value}\n", data[1:]
        elif isinstance(data[0], StringConstant):
            # ! Need to handle string constants
            return vm, data[1:]
        elif data[0].value == "this":
            return "push pointer 0\n", data[1:]  # This is the base address of the current object
        elif data[0].value == "true":
            return "push constant 0\nnot\n", data[1:]
        elif data[0].value == "false" or data[0].value == "null":
            return "push constant 0\n", data[1:]
        elif isinstance(data[0], Identifier):
            if data[1].value == "[":
                # ? what do we do with arrays
                _value = data[0].value
                vm += f"{data[1]}\n"
                vm, data = self.CompileExpression(vm, data[2:])
                assert data[0].value == "]", f"Invalid term end: {data[0].value}"  # type: ignore
                vm += f"{data[0]}\n"
            elif data[1].value == "(":
                # ! This is a method call, need to push extra argument
                # set the base address of the this segment to the argument 0
                vm += "push argument 0\n"
                _value = str(data[0].value)
                vm, data, num = self.CompileExpressionList(vm, data[2:])
                vm += self.writer.write_call(self.class_name, _value, num + 1) + "\n"
                assert data[0].value == ")", f"Invalid term end: {data[0].value}"  # type: ignore
            elif data[1].value == ".":
                vm += self.writer.write_pop(*self._table_caller(data[0])) + "\n"   # type: ignore
                assert isinstance(data[2], Identifier), f"Invalid subroutine name: {data[2].value}"
                assert data[3].value == "(", f"Invalid subroutine start: {data[3].value}"
                vm, data, num = self.CompileExpressionList(vm, data[4:])
                vm += self.writer.write_call(str(data[0].value), str(data[2].value), num) + "\n"
                assert data[0].value == ")", f"Invalid term end: {data[0].value}"  # type: ignore
            else:
                vm += self.writer.write_push(*self._table_caller(data[0])) + "\n" # type: ignore
            return vm + "</term>\n", data[1:]
        elif data[0].value == "(":
            # ! Insure that operator priority holds
            vm, data = self.CompileExpression(vm, data[1:])
            assert data[0].value == ")", f"Invalid term end: {data[0].value}"
            return vm, data[1:]
        elif data[0].value in ["-", "~"]:
            op = OP_MAP[data[0].value]  # type: ignore
            vm, data = self.CompileTerm(vm, data[1:])
            return vm + f"{op}\n", data
        else:
            raise ValueError(f"Invalid term: {data[0].value}")

    def CompileExpressionList(self, vm: str, data: list[Token])  -> tuple[str, list[Token], int]:
        vm += "<expressionList>\n"
        num = 0
        while data[0].value != ")":
            vm, data = self.CompileExpression(vm, data)
            if data[0].value == ",":
                vm += f"{data[0]}\n"
                data = data[1:]
            num += 1
        return vm + "</expressionList>\n", data, num

    def _table_caller(self, token: Identifier) -> tuple[str, int]:
        # ? Not sure where to put this
        assert isinstance(token, Identifier), f"Invalid token: {token}"
        name = token.value
        kind = self.tables.KindOf(name)
        index = self.tables.IndexOf(name)
        return kind, index
