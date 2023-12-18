from interpreter.nodes.expressions.BoolExpression import BoolExpression
from interpreter.nodes.expressions.Expression import Expression


class IfStatement:
    def __init__(self, condition: BoolExpression, expressions: list[Expression]):
        self.condition = condition
        self.expressions = expressions

    def accept(self, visitor):
        return visitor.visit_if_statement(self)
