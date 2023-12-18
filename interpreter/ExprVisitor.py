# Generated from Expr.g4 by ANTLR 4.13.0
import interpreter.ExprParser
import abc
from antlr4 import *

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
from interpreter.nodes.expressions.StrExpression import StrExpression
from interpreter.nodes.Program import Program
from interpreter.nodes.expressions.NotEqual import NotEqualExpression
from interpreter.nodes.expressions.EqualExpression import EqualExpression
from interpreter.nodes.expressions.LessExpression import LessExpression
from interpreter.nodes.expressions.MoreExp import MoreExpression
from interpreter.nodes.expressions.ArrayStatement import ArrayExpression
from interpreter.nodes.expressions.AccesByIndexExpression import AccessByIndexExpression


class ExprVisitor(ParseTreeVisitor):
    def visitProg(self, ctx):
        statements = []
        for statement in ctx.stmt():
            statements.append(self.visit(statement))
        return Program(statements)

    def visitStmt(self, ctx):
        if ctx.assign is not None:
            if ctx.index is not None:
                ident = AccessByIndexExpression(
                    ctx.ident.text, self.visit(ctx.index))
                return AssignStatement(ident, self.visit(ctx.assign))
            return AssignStatement(ctx.ident.text, self.visit(ctx.assign))
        elif ctx.if_condition is not None:
            statements = []
            for statement in ctx.stmt():
                statements.append(self.visit(statement))
            condition = self.visit(ctx.if_condition)
            return IfStatement(condition, statements)

        elif ctx.while_condition is not None:
            statements = []
            for statement in ctx.stmt():
                statements.append(statement)
            condition = self.visit(ctx.while_condition)
            return WhileStatement(condition, statements)
        else:
            return PrintStatement(self.visit(ctx.printexp))

    def visitExpr(self, ctx):
        if ctx.element is not None:
            elements = []
            for el in ctx.expr():
                elements.append(self.visit(el))
            return ArrayExpression(ctx.ident, elements)

        if ctx.array is not None:
            return AccessByIndexExpression(ctx.array.text, self.visit(ctx.index))

        if ctx.num is not None:
            return NumberExpression(ctx.num.text)

        if ctx.bool_ is not None:
            return BoolExpression(ctx.bool_.text)

        if ctx.exp is not None:
            return BraceExpression(self.visit(ctx.exp))

        if ctx.string is not None:
            return StrExpression(ctx.string.text[1:-1])

        if ctx.ident is not None:
            return IdentExpression(ctx.ident.text)

        if ctx.op.text == '/':
            return DivExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '*':
            return MulExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '+':
            return AddExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '-':
            return SubExpression(self.visit(ctx.left), self.visit(ctx.right))

        elif ctx.op.text == '>':
            return MoreExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '<':
            return LessExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '==':
            return EqualExpression(self.visit(ctx.left), self.visit(ctx.right))
        elif ctx.op.text == '!=':
            return NotEqualExpression(self.visit(ctx.left), self.visit(ctx.right))
