from enum import Enum

from regex.nodes.regex_node import RegexNode
from regex.regex_visitors.visitor import Visitor


class RegexOperations(Enum):
    CONCAT = "X"
    UNITE = "+"
    CLOSURE = "*"


class BinaryNode(RegexNode):
    def __init__(self, left: RegexNode, right: RegexNode, operation: RegexOperations):
        self.exp1 = left
        self.exp2 = right
        self.operation = operation

    def __str__(self):
        if self.operation == RegexOperations.CLOSURE:
            return f'({self.exp1})*'
        if self.operation == RegexOperations.CONCAT:
            return f'{self.exp1}{self.exp2}'
        if self.operation == RegexOperations.UNITE:
            return f'{self.exp1}+{self.exp2}'

    def accept(self, visitor: Visitor):
        return visitor.visit(self)
