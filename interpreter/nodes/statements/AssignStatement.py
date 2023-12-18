from interpreter.nodes.expressions.Expression import Expression


class AssignStatement:
    def __init__(self, variable: str, expression: Expression):
        self.variable = variable
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_assign_statement(self)
