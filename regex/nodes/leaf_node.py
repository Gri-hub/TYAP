from regex.nodes.regex_node import RegexNode
from regex.regex_visitors.visitor import Visitor


class LeafNode(RegexNode):
    def __init__(self, letter: str = None):
        self.letter = letter

    def accept(self, visitor: Visitor):
        return visitor.visit(self)

    def __str__(self):
        return self.letter
