from interpreter.nodes.expressions.Expression import Expression


class ArrayExpression:
    def __init__(self, name: str, elements: list[Expression]):
        self.name = name
        self.elements = elements

    def accept(self, visitor):
        return visitor.visit_array_expression(self)
