from interpreter.nodes.expressions.Expression import Expression


class PrintStatement:
    def __init__(self, expression: Expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_print_statement(self)
