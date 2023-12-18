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
from interpreter.visitors.Visitor import Visitor
from interpreter.nodes.expressions.MoreExp import MoreExpression
from interpreter.nodes.expressions.LessExpression import LessExpression
from interpreter.nodes.expressions.EqualExpression import EqualExpression
from interpreter.nodes.expressions.NotEqual import NotEqualExpression
from interpreter.ExprVisitor import ExprVisitor
from interpreter.nodes.expressions.ArrayStatement import ArrayExpression
from interpreter.nodes.expressions.AccesByIndexExpression import AccessByIndexExpression


class InterpreterVisitor(Visitor):
    def __init__(self):
        self.variables = {}

    def visit_number_expression(self, expression: NumberExpression):
        return expression.number

    def visit_string_expression(self, expression: NumberExpression):
        return expression.str

    def visit_bool_expression(self, expression: BoolExpression):
        return expression.bool

    def visit_add_expression(self, expression: AddExpression):
        return expression.left.accept(self) + expression.right.accept(self)

    def visit_sub_expression(self, expression: SubExpression):
        return expression.left.accept(self) - expression.right.accept(self)

    def visit_mul_expression(self, expression: MulExpression):
        return expression.left.accept(self) * expression.right.accept(self)

    def visit_div_expression(self, expression: DivExpression):
        return expression.left.accept(self) // expression.right.accept(self)

    def visit_brace_expression(self, expression: BraceExpression):
        return expression.expression.accept(self)

    def visit_array_expression(self, expression: ArrayExpression):
        arr = []  
        for element in expression.elements:
            arr.append(element.accept(self))
        return arr

    def visit_more_expression(self, expression: MoreExpression):
        return expression.left.accept(self) > expression.right.accept(self)

    def visit_less_expression(self, expression: LessExpression):
        return expression.left.accept(self) < expression.right.accept(self)

    def visit_equal_expression(self, expression: EqualExpression):
        return expression.left.accept(self) == expression.right.accept(self)

    def visit_notequal_expression(self, expression: NotEqualExpression):
        return expression.left.accept(self) != expression.right.accept(self)

    def visit_program(self, program: Program):
        for expression in program.expressions:
            expression.accept(self)

    def visit_assign_statement(self, statement: AssignStatement):
        if isinstance(statement.variable, AccessByIndexExpression):
            self.variables[statement.variable.name][statement.variable.index.accept(self)] = statement.expression.accept(
                self)
        else:
            self.variables[statement.variable] = statement.expression.accept(self)

    def visit_print_statement(self, statement: PrintStatement):
        print(statement.expression.accept(self))

    def visit_if_statement(self, statement: IfStatement):
        if isinstance(statement.condition, IdentExpression):
            if self.visit_ident_expression(statement.condition):
                for expression in statement.expressions:
                    expression.accept(self)
        elif statement.condition.accept(self):
            for expression in statement.expressions:
                expression.accept(self)

    def visit_while_statement(self, statement: WhileStatement):
        while statement.condition.accept(self):
            for expression in statement.expressions:
                exp = ExprVisitor().visit(expression)
                exp.accept(self)

    def visit_ident_expression(self, expression: IdentExpression):
        if expression.name not in self.variables:
            raise ValueError(f'Variable {expression.name} not found')
        return self.variables[expression.name]

    def visit_accessbyindex_expression(self, expression: AccessByIndexExpression):
        if expression.name not in self.variables:
            raise ValueError(f'Array {expression.name} not found')
        return self.variables[expression.name][expression.index.accept(self)]
