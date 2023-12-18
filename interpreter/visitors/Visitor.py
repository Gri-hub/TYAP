from abc import ABC, abstractmethod
from interpreter.nodes.expressions.BraceExpression import BraceExpression
from interpreter.nodes.Program import Program
from interpreter.nodes.expressions.AddExpression import AddExpression
from interpreter.nodes.expressions.DivExpression import DivExpression
from interpreter.nodes.expressions.MulExpression import MulExpression
from interpreter.nodes.expressions.IdentExpression import IdentExpression

from interpreter.nodes.expressions.NumberExpression import NumberExpression
from interpreter.nodes.expressions.SubExpression import SubExpression
from interpreter.nodes.statements.AssignStatement import AssignStatement
from interpreter.nodes.statements.PrintStatement import PrintStatement


class Visitor(ABC):

    @abstractmethod
    def visit_number_expression(self, expression: NumberExpression):
        pass

    @abstractmethod
    def visit_add_expression(self, expression: AddExpression):
        pass

    @abstractmethod
    def visit_sub_expression(self, expression: SubExpression):
        pass

    @abstractmethod
    def visit_mul_expression(self, expression: MulExpression):
        pass

    @abstractmethod
    def visit_div_expression(self, expression: DivExpression):
        pass

    @abstractmethod
    def visit_brace_expression(self, expression: BraceExpression):
        pass

    @abstractmethod
    def visit_program(self, program: Program):
        pass

    @abstractmethod
    def visit_assign_statement(self, statement: AssignStatement):
        pass

    @abstractmethod
    def visit_print_statement(self, statement: PrintStatement):
        pass

    @abstractmethod
    def visit_ident_expression(self, expression: IdentExpression):
        pass
