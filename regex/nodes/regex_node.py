from abc import abstractmethod

from regex.regex_visitors.visitor import Visitor


class RegexNode:
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

    def __hash__(self):
        return str(self).__hash__()

    def __eq__(self, other):
        return str(self) == str(other)
