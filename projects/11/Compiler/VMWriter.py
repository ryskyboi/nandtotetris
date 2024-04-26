SEGMENTS = ['constant', 'argument', 'local', 'static', 'this', 'that', 'pointer', 'temp']
COMMANDS = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not', 'call Math.multiply 2', 'call Math.divide 2']


class CodeWriter:
    def _write_push_pop(self, push: bool, segment: str, index: int) -> str:
        if segment == "field": segment = "local"
        if segment == "var": segment = "local"
        assert segment in SEGMENTS, f"Invalid segment {segment}"
        return f"{'push' if push else 'pop'} {segment} {index} \n"

    def write_push(self, segment: str, index: int) -> str:
        return self._write_push_pop(True, segment, index)

    def write_pop(self, segment: str, index: int) -> str:
        return self._write_push_pop(False, segment, index)

    def write_arithmetic(self, command: str) -> str:
        assert command in COMMANDS, f"Invalid command {command}"
        return command + "\n"

    def write_label(self, label: str) -> str:
        return f"label {label} \n"

    def write_goto(self, label: str) -> str:
        return f"goto {label} \n"

    def write_if(self, label: str) -> str:
        return f"if-goto {label} \n"

    def write_call(self, class_name: str, name: str, n_args: int) -> str:
        return f"call {class_name}.{name} {n_args} \n"

    def write_function(self, class_name: str, name: str, n_locals: int) -> str:
        return f"function {class_name}.{name} {n_locals} \n"

    def write_return(self) -> str:
        return "return \n"
