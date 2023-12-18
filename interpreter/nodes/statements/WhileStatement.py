from interpreter.nodes.expressions.Expression import Expression


class WhileStatement:
    def __init__(self, condition: Expression, expressions: list[Expression]):
        self.condition = condition
        self.expressions = expressions

    def accept(self, visitor):
        return visitor.visit_while_statement(self)
