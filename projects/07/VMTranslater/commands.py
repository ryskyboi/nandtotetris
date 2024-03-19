from dataclasses import dataclass
from abc import ABC


class Command(ABC):
    ...


@dataclass
class _OneArg(Command):
    arg1: str


@dataclass
class _TwoArg(_OneArg):
    arg2: int


##Function Types
class C_RETURN(Command):
    ...


@dataclass
class C_ARITHMETIC(_OneArg):
    ...


@dataclass
class C_LABEL(_OneArg):
    ...


@dataclass
class C_GOTO(_OneArg):
    ...


@dataclass
class C_IF_GOTO(_OneArg):
    ...


@dataclass
class C_PUSH(_TwoArg):
    ...


@dataclass
class C_POP(_TwoArg):
    ...


@dataclass
class C_FUNCTION(_TwoArg):
    ...


@dataclass
class C_CALL(_TwoArg):
    ...


ARITHMETIC_COMMANDS = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]
