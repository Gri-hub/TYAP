import interpreter.ExprParser
import abc
from antlr4 import *

from interpreter.nodes.Program import Program
from interpreter.nodes.expressions.AddExpression import AddExpression
from interpreter.nodes.expressions.BraceExpression import BraceExpression
from interpreter.nodes.expressions.DivExpression import DivExpression
from interpreter.nodes.expressions.IdentExpression import IdentExpression
from interpreter.nodes.expressions.MulExpression import MulExpression

from interpreter.nodes.expressions.NumberExpression import NumberExpression
from interpreter.nodes.expressions.BoolExpression import BoolExpression
from interpreter.nodes.expressions.SubExpression import SubExpression
from interpreter.nodes.statements.AssignStatement import AssignStatement
from interpreter.nodes.statements.PrintStatement import PrintStatement
from interpreter.nodes.statements.IfStatement import IfStatement
from interpreter.nodes.statements.WhileStatement import WhileStatement
from interpreter.ExprVisitor import ExprVisitor
from interpreter.visitors.Visitor import Visitor
from interpreter.nodes.expressions.MoreExp import MoreExpression
from interpreter.nodes.expressions.LessExpression import LessExpression
from interpreter.nodes.expressions.EqualExpression import EqualExpression
from interpreter.nodes.expressions.NotEqual import NotEqualExpression
from interpreter.ExprVisitor import ExprVisitor
from interpreter.nodes.expressions.ArrayStatement import ArrayExpression
from interpreter.nodes.expressions.AccesByIndexExpression import AccessByIndexExpression


class PrintVisitor(ParseTreeVisitor):
    def __init__(self):
        self.counter = 0
        self.str = ""

    def Print(self, s: str):
        self.str +=  "    " * self.counter + s + '\n'

    def visit_number_expression(self, expression: NumberExpression):
        self.Print(f"NumberExpression({expression.number})")

    def visit_string_expression(self, expression: NumberExpression):
        self.Print(f"StringExpression({expression.str})")

    def visit_bool_expression(self, expression: BoolExpression):
        self.Print(f"BooleanExpression({expression.bool})")

    def visit_add_expression(self, expression: AddExpression):
        self.Print(f"AddExpression")
        self.counter += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.counter -= 1

    def visit_sub_expression(self, expression: SubExpression):
        self.Print(f"SubExpression")
        self.counter += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.counter -= 1

    def visit_mul_expression(self, expression: MulExpression):
        self.Print("MulExpression")
        self.counter += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.counter -= 1

    def visit_div_expression(self, expression: DivExpression):
        self.Print("DivExxpression")
        self.counter += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.counter -= 1

    def visit_brace_expression(self, expression: BraceExpression):
        self.Print("BraceExpression")
        self.counter += 1
        expression.expression.accept(self)
        self.counter -= 1

    def visit_array_expression(self, expression: ArrayExpression):
        self.Print("ArrayExpression")
        self.counter += 1
        arr = []
        for element in expression.elements:
            arr.append(element.accept(self))
        self.counter -= 1


    def visit_more_expression(self, expression: MoreExpression):
         self.Print("MoreExpression")
         self.counter += 1
         expression.left.accept(self)
         expression.right.accept(self)
         self.counter -= 1

    def visit_less_expression(self, expression: LessExpression):
        self.Print("LessExpression")
        self.counter += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.counter -= 1

    def visit_equal_expression(self, expression: EqualExpression):
        self.Print("EqualExpression")
        self.counter += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.counter -= 1


    def visit_notequal_expression(self, expression: NotEqualExpression):
        self.Print("NotEqualExpression")
        self.counter += 1
        expression.left.accept(self)
        expression.right.accept(self)
        self.counter -= 1

    def visit_program(self, program: Program):
        self.Print("Prorgam\n")
        for expression in program.expressions:
            expression.accept(self)
            self.counter = 0
            self.Print("\n--------\n")

    def visit_assign_statement(self, statement: AssignStatement):
        self.Print("Assign")
        self.counter += 1
        self.Print(f"IdentExpression({statement.variable})")
        statement.expression.accept(self)
        self.counter -= 1

    def visit_print_statement(self, statement: PrintStatement):
        self.Print("PrintExpression")
        self.counter += 1
        statement.expression.accept(self)
        self.counter -= 1


    def visit_if_statement(self, statement: IfStatement):
        self.Print("IfStatement")
        self.counter += 1
        for expression in statement.expressions:
            expression.accept(self)
        self.counter -= 1

    def visit_while_statement(self, statement: WhileStatement):
        self.Print("WhileStatement")
        self.counter += 1
        for expression in statement.expressions:
            expression.accept(self)
        self.counter -= 1


    def visit_ident_expression(self, expression: IdentExpression):
        self.Print(f"IdentExpression({expression.name})")

    def visit_accessbyindex_expression(self, expression: AccessByIndexExpression):
        self.Print("AccessByIndexExpression")
        self.counter += 1
        self.Print(f"Ident({expression.name})")
        expression.index.accept(self)
        self.counter -= 1
