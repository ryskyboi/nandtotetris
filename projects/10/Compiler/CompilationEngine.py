from Tokens import Token, IntegerConstant, StringConstant, Identifier

RETURN_TYPE = tuple[str, list[Token]]
TYPES = ["int", "char", "boolean"]

class Compiler:
    def main(self, data: list[Token]) -> str:
        xml = self.CompileClass("", data)
        return xml

    def CompileClass(self, xml: str, data: list[Token]) -> str:
        assert data[0].value == "class", f"Not a class: {data[0].value}"
        assert isinstance(data[1], Identifier), f"Invalid class name: {data[1].value}"
        assert data[2].value == "{", f"Invalid class start: {data[2].value}"
        assert data[-1].value == "}", f"Invalid class end: {data[-1].value}"
        xml += f"<class> \n{data[0]} \n{data[1]} \n{data[2]} \n"
        data, final = data[3:-1], data[-1]
        while data[0].value == "field" or data[0].value == "static": xml, data = self.CompileClassVarDec(xml, data)
        while data[0].value == "constructor" or data[0].value == "function" or data[0].value == "method":
            xml, data = self.CompileSubroutine(xml, data)
            if len(data) == 0: break
        return xml + f"{final}\n </class> \n"

    def CompileClassVarDec(self, xml: str, data: list[Token]) -> RETURN_TYPE:
        assert data[0].value == "field" or data[0].value == "static", f"Not a class var dec: {data[0].value}"
        assert data[1].value in TYPES or isinstance(data[1], Identifier), f"Invalid class var dec type: {data[1].value}"
        assert isinstance(data[2], Identifier), f"Invalid class var dec name: {data[2].value}"
        xml = f"{xml} <classVarDec>\n {data[0]}\n {data[1]}\n {data[2]}\n"
        data = data[3:]
        while data[0].value == ",":
            assert isinstance(data[1], Identifier), f"Invalid class var dec name: {data[1].value}"
            xml += f"{data[0]}\n {data[1]}\n"
            data = data[2:]
        assert data[0].value == ";", f"Invalid class var dec end: {data[0].value}"
        return xml + f"{data[0]}\n </classVarDec> \n", data[1:]

    def CompileSubroutine(self, xml: str, data: list[Token]) -> RETURN_TYPE:
        assert data[0].value in ["constructor", "function", "method"], f"Not a subroutine: {data[0].value}"
        assert data[1].value in TYPES + ["void"] or isinstance(data[1], Identifier), f"Invalid subroutine return type: {data[1].value}"
        assert isinstance(data[2], Identifier), f"Invalid subroutine name: {data[2].value}"
        assert data[3].value == "(", f"Invalid subroutine start: {data[3].value}"
        xml += f"<subroutineDec>\n {data[0]}\n {data[1]}\n {data[2]}\n {data[3]}\n"
        xml, data = self.CompileParameterList(xml, data[4:])
        assert data[0].value == ")", f"Invalid subroutine end: {data[0].value}"
        assert data[1].value == "{", f"Invalid subroutine start: {data[1].value}"
        xml += f"{data[0]}\n <subroutineBody>\n {data[1]}\n"
        data = data[2:]
        while data[0].value == "var": xml, data = self.CompileVarDec(xml, data)
        while data[0].value in ["do", "let", "while", "if", "return"]: xml, data = self.CompileStatements(xml, data)
        assert data[0].value == "}", f"Invalid subroutine end: {data[0].value}"
        return xml + f" {data[0]} \n</subroutineBody> \n</subroutineDec> \n", data[1:]

    def CompileParameterList(self, xml: str, data: list[Token]) -> RETURN_TYPE:
        xml += "<parameterList>\n"
        while data[0].value in TYPES:
            assert data[0].value in TYPES, f"Invalid parameter type: {data[0].value}"
            assert isinstance(data[1], Identifier), f"Invalid parameter name: {data[1].value}"
            xml += f"{data[0]}\n {data[1]}\n"
            data = data[2:]
            if data[0].value == ",":
                xml += f"{data[0]}\n"
                data = data[1:]
        return xml + "</parameterList>\n", data

    def CompileVarDec(self, xml: str, data: list[Token]) -> RETURN_TYPE:
        assert data[0].value == "var", f"Not a var dec: {data[0].value}"
        assert data[1].value in TYPES or isinstance(data[1], Identifier), f"Invalid var dec type: {data[1].value}"
        assert isinstance(data[2], Identifier), f"Invalid var dec name: {data[2].value}"
        xml = f"{xml} <varDec>\n {data[0]}\n {data[1]}\n {data[2]}\n"
        data = data[3:]
        while data[0].value == ",":
            assert isinstance(data[1], Identifier), f"Invalid var dec name: {data[1].value}"
            xml += f"{data[0]}\n {data[1]}\n"
            data = data[2:]
        assert data[0].value == ";", f"Invalid var dec end: {data[0].value}"
        return xml + f"{data[0]}\n </varDec> \n", data[1:]

    def CompileStatements(self, xml: str, data: list[Token]) -> RETURN_TYPE:
        xml += "<statements>\n"
        while data[0].value in ["let", "if", "while", "do", "return"]:
            if data[0].value == "let": xml, data = self.CompileLet(xml, data)
            elif data[0].value == "if": xml, data = self.CompileIf(xml, data)
            elif data[0].value == "while": xml, data = self.CompileWhile(xml, data)
            elif data[0].value == "do": xml, data = self.CompileDo(xml, data)
            elif data[0].value == "return": xml, data = self.CompileReturn(xml, data)
        return xml + "</statements>\n", data

    def CompileDo(self, xml: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "do", f"Not a do: {data[0].value}"
        assert isinstance(data[1], Identifier), f"Invalid do name: {data[1].value}"
        xml += f"<doStatement>\n {data[0]}\n {data[1]}\n"
        if data[2].value == ".":
            assert isinstance(data[3], Identifier), f"Invalid do name: {data[3].value}"
            xml += f"{data[2]}\n {data[3]}\n"
            data = data[4:]
        else: data = data[2:]
        assert data[0].value == "(", f"Invalid do start: {data[0].value}"
        xml += f"{data[0]}\n"
        xml, data = self.CompileExpressionList(xml, data[1:])
        assert data[0].value == ")", f"Invalid do end: {data[0].value}"
        assert data[1].value == ";", f"Invalid do end: {data[1].value}"
        return xml + f"{data[0]}\n {data[1]}\n </doStatement> \n", data[2:]

    def CompileLet(self, xml: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "let", f"Not a let: {data[0].value}"
        assert isinstance(data[1], Identifier), f"Invalid let name: {data[1].value}"
        xml = f"{xml} <letStatement>\n {data[0]}\n {data[1]}\n"
        if data[2].value == "[":
            xml += f"{data[2]}\n"
            xml, data = self.CompileExpression(xml, data[3:])
            assert data[0].value == "]", f"Invalid let end: {data[0].value}"
            xml += f"{data[0]}\n"
            data = data[1:]
        else: data = data[2:]
        assert data[0].value == "=", f"Let requires an equality: {data[0].value}"
        xml += f"{data[0]}\n"
        xml, data = self.CompileExpression(xml, data[1:])
        assert data[0].value == ";", f"Invalid let end: {data[0].value}"
        return xml + f"{data[0]}\n </letStatement> \n", data[1:]

    def CompileWhile(self, xml: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "while", f"Not a while: {data[0].value}"
        assert data[1].value == "(", f"Invalid while expression start: {data[1].value}"
        xml += f"<whileStatement>\n {data[0]}\n {data[1]}\n"
        xml, data = self.CompileExpression(xml, data[2:])
        assert data[0].value == ")", f"Invalid while expression end: {data[0].value}"
        assert data[1].value == "{", f"Invalid while start: {data[1].value}"
        xml += f"{data[0]}\n {data[1]}\n"
        xml, data = self.CompileStatements(xml, data[2:])
        assert data[0].value == "}", f"Invalid while end: {data[0].value}"
        return xml + f"{data[0]}\n </whileStatement> \n", data[1:]

    def CompileReturn(self, xml: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "return", f"Not a return: {data[0].value}"
        xml += f"<returnStatement>\n {data[0]}\n"
        if data[1].value != ";":
            xml, data = self.CompileExpression(xml, data[1:])
        else: data = data[1:]
        assert data[0].value == ";", f"Invalid return end: {data[0].value}"
        return xml + f"{data[0]}\n </returnStatement> \n", data[1:]

    def CompileIf(self, xml: str, data: list[Token])  -> RETURN_TYPE:
        assert data[0].value == "if", f"Not an if: {data[0].value}"
        assert data[1].value == "(", f"Invalid if expression start: {data[1].value}"
        xml += f"<ifStatement>\n {data[0]}\n {data[1]}\n"
        xml, data = self.CompileExpression(xml, data[2:])
        assert data[0].value == ")", f"Invalid if expression end: {data[0].value}"
        assert data[1].value == "{", f"Invalid if start: {data[1].value}"
        xml += f"{data[0]}\n {data[1]}\n"
        xml, data = self.CompileStatements(xml, data[2:])
        assert data[0].value == "}", f"Invalid if end: {data[0].value}"
        xml += f"{data[0]}\n"
        data = data[1:]
        if data[0].value == "else":
            xml += f"{data[0]}\n"
            assert data[1].value == "{", f"Invalid else start: {data[1].value}"
            xml += f"{data[1]}\n"
            xml, data = self.CompileStatements(xml, data[2:])
            assert data[0].value == "}", f"Invalid if end: {data[0].value}"
            xml += f"{data[0]}\n"
            data = data[1:]
        return xml + "</ifStatement> \n", data

    def CompileExpression(self, xml: str, data: list[Token]) -> RETURN_TYPE:
        xml += "<expression>\n"
        xml, data = self.CompileTerm(xml, data)
        while data[0].value in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            xml += f"{data[0]}\n"
            xml, data = self.CompileTerm(xml, data[1:])
        return xml + "</expression>\n", data

    def CompileTerm(self, xml: str, data: list[Token])  -> RETURN_TYPE:
        xml += "<term>\n"
        if isinstance(data[0], IntegerConstant) or isinstance(data[0], StringConstant) or data[0].value in ["true", "false", "null", "this"]:
            xml += f"{data[0]}\n"
            return xml + "</term>\n", data[1:]
        if isinstance(data[0], Identifier):
            xml += f"{data[0]}\n"
            if data[1].value == "[":
                xml += f"{data[1]}\n"
                xml, data = self.CompileExpression(xml, data[2:])
                assert data[0].value == "]", f"Invalid term end: {data[0].value}"  # type: ignore
                xml += f"{data[0]}\n"
            if data[1].value == "(":
                xml += f"{data[1]}\n"
                xml, data = self.CompileExpressionList(xml, data[2:])
                assert data[0].value == "(", f"Invalid term end: {data[0].value}"  # type: ignore
                xml += f"{data[0]}\n"
            elif data[1].value == ".":
                xml += f"{data[1]}\n"
                assert isinstance(data[2], Identifier), f"Invalid subroutine name: {data[2].value}"
                xml += f"{data[2]}\n"
                xml += f"{data[3]}\n"
                xml, data = self.CompileExpressionList(xml, data[4:])
                xml += f"{data[0]}\n"
            return xml + "</term>\n", data[1:]
        elif data[0].value == "(":
            xml += f"{data[0]}\n"
            xml, data = self.CompileExpression(xml, data[1:])
            assert data[0].value == ")", f"Invalid term end: {data[0].value}"
            xml += f"{data[0]}\n"
            return xml + "</term>\n", data[1:]
        elif data[0].value in ["-", "~"]:
            xml += f"{data[0]}\n"
            xml, data = self.CompileTerm(xml, data[1:])
            return xml + "</term>\n", data
        else:
            raise ValueError(f"Invalid term: {data[0].value}")

    def CompileExpressionList(self, xml: str, data: list[Token])  -> RETURN_TYPE:
        xml += "<expressionList>\n"
        while data[0].value != ")":
            xml, data = self.CompileExpression(xml, data)
            if data[0].value == ",":
                xml += f"{data[0]}\n"
                data = data[1:]
        return xml + "</expressionList>\n", data
