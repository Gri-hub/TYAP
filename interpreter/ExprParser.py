# Generated from Expr.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,108,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,49,8,1,10,1,12,1,52,9,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,1,1,1,3,1,66,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,74,8,2,10,2,12,2,77,9,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,92,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,5,2,103,8,2,10,2,12,2,106,9,2,1,2,0,1,4,3,0,2,4,0,3,1,
        0,11,12,1,0,13,14,1,0,15,18,121,0,6,1,0,0,0,2,65,1,0,0,0,4,91,1,
        0,0,0,6,7,5,23,0,0,7,8,5,24,0,0,8,9,5,1,0,0,9,10,5,2,0,0,10,11,5,
        3,0,0,11,17,5,25,0,0,12,13,3,2,1,0,13,14,5,25,0,0,14,16,1,0,0,0,
        15,12,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,
        0,0,0,19,17,1,0,0,0,20,21,5,4,0,0,21,1,1,0,0,0,22,23,5,5,0,0,23,
        24,5,1,0,0,24,25,3,4,2,0,25,26,5,2,0,0,26,66,1,0,0,0,27,28,5,6,0,
        0,28,29,3,4,2,0,29,30,5,3,0,0,30,36,5,25,0,0,31,32,3,2,1,0,32,33,
        5,25,0,0,33,35,1,0,0,0,34,31,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,
        36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,40,5,4,0,0,40,66,1,
        0,0,0,41,42,5,7,0,0,42,43,3,4,2,0,43,44,5,3,0,0,44,50,5,25,0,0,45,
        46,3,2,1,0,46,47,5,25,0,0,47,49,1,0,0,0,48,45,1,0,0,0,49,52,1,0,
        0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,
        5,4,0,0,54,66,1,0,0,0,55,62,5,29,0,0,56,57,5,29,0,0,57,58,5,8,0,
        0,58,59,3,4,2,0,59,60,5,9,0,0,60,62,1,0,0,0,61,55,1,0,0,0,61,56,
        1,0,0,0,62,63,1,0,0,0,63,64,5,10,0,0,64,66,3,4,2,0,65,22,1,0,0,0,
        65,27,1,0,0,0,65,41,1,0,0,0,65,61,1,0,0,0,66,3,1,0,0,0,67,68,6,2,
        -1,0,68,92,5,26,0,0,69,75,5,8,0,0,70,71,3,4,2,0,71,72,5,19,0,0,72,
        74,1,0,0,0,73,70,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,
        0,76,78,1,0,0,0,77,75,1,0,0,0,78,92,5,9,0,0,79,80,5,29,0,0,80,81,
        5,8,0,0,81,82,3,4,2,0,82,83,5,9,0,0,83,92,1,0,0,0,84,92,5,27,0,0,
        85,92,5,28,0,0,86,87,5,1,0,0,87,88,3,4,2,0,88,89,5,2,0,0,89,92,1,
        0,0,0,90,92,5,29,0,0,91,67,1,0,0,0,91,69,1,0,0,0,91,79,1,0,0,0,91,
        84,1,0,0,0,91,85,1,0,0,0,91,86,1,0,0,0,91,90,1,0,0,0,92,104,1,0,
        0,0,93,94,10,10,0,0,94,95,7,0,0,0,95,103,3,4,2,11,96,97,10,9,0,0,
        97,98,7,1,0,0,98,103,3,4,2,10,99,100,10,8,0,0,100,101,7,2,0,0,101,
        103,3,4,2,9,102,93,1,0,0,0,102,96,1,0,0,0,102,99,1,0,0,0,103,106,
        1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,5,1,0,0,0,106,104,1,
        0,0,0,9,17,36,50,61,65,75,91,102,104
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'print'", 
                     "'if'", "'while'", "'['", "']'", "'='", "'*'", "'/'", 
                     "'+'", "'-'", "'<'", "'>'", "'=='", "'!='", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'fun'", "'main'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SPACES", "LINE_COMMENT", "COMMENT", "FUN", "MAIN", 
                      "NEWLINE", "INT", "BOOL", "STRING", "IDENT" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    SPACES=20
    LINE_COMMENT=21
    COMMENT=22
    FUN=23
    MAIN=24
    NEWLINE=25
    INT=26
    BOOL=27
    STRING=28
    IDENT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(ExprParser.FUN, 0)

        def MAIN(self):
            return self.getToken(ExprParser.MAIN, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)


    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(ExprParser.FUN)
            self.state = 7
            self.match(ExprParser.MAIN)
            self.state = 8
            self.match(ExprParser.T__0)
            self.state = 9
            self.match(ExprParser.T__1)
            self.state = 10
            self.match(ExprParser.T__2)
            self.state = 11
            self.match(ExprParser.NEWLINE)

            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536871136) != 0):
                self.state = 12
                self.stmt()
                self.state = 13
                self.match(ExprParser.NEWLINE)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.printexp = None # ExprContext
            self.if_condition = None # ExprContext
            self.while_condition = None # ExprContext
            self.ident = None # Token
            self.index = None # ExprContext
            self.assign = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def IDENT(self):
            return self.getToken(ExprParser.IDENT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmt"):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)


    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(ExprParser.T__4)
                self.state = 23
                self.match(ExprParser.T__0)
                self.state = 24
                localctx.printexp = self.expr(0)
                self.state = 25
                self.match(ExprParser.T__1)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(ExprParser.T__5)
                self.state = 28
                localctx.if_condition = self.expr(0)
                self.state = 29
                self.match(ExprParser.T__2)
                self.state = 30
                self.match(ExprParser.NEWLINE)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536871136) != 0):
                    self.state = 31
                    self.stmt()
                    self.state = 32
                    self.match(ExprParser.NEWLINE)
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 39
                self.match(ExprParser.T__3)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(ExprParser.T__6)
                self.state = 42
                localctx.while_condition = self.expr(0)
                self.state = 43
                self.match(ExprParser.T__2)
                self.state = 44
                self.match(ExprParser.NEWLINE)

                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536871136) != 0):
                    self.state = 45
                    self.stmt()
                    self.state = 46
                    self.match(ExprParser.NEWLINE)
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 53
                self.match(ExprParser.T__3)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 55
                    localctx.ident = self.match(ExprParser.IDENT)
                    pass

                elif la_ == 2:
                    self.state = 56
                    localctx.ident = self.match(ExprParser.IDENT)
                    self.state = 57
                    self.match(ExprParser.T__7)
                    self.state = 58
                    localctx.index = self.expr(0)
                    self.state = 59
                    self.match(ExprParser.T__8)
                    pass


                self.state = 63
                self.match(ExprParser.T__9)
                self.state = 64
                localctx.assign = self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.num = None # Token
            self.element = None # ExprContext
            self.array = None # Token
            self.index = None # ExprContext
            self.bool_ = None # Token
            self.string = None # Token
            self.exp = None # ExprContext
            self.ident = None # Token
            self.op = None # Token
            self.right = None # ExprContext

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def IDENT(self):
            return self.getToken(ExprParser.IDENT, 0)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr"):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)


    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 68
                localctx.num = self.match(ExprParser.INT)
                pass

            elif la_ == 2:
                self.state = 69
                self.match(ExprParser.T__7)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1006633218) != 0):
                    self.state = 70
                    localctx.element = self.expr(0)
                    self.state = 71
                    self.match(ExprParser.T__18)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 78
                self.match(ExprParser.T__8)
                pass

            elif la_ == 3:
                self.state = 79
                localctx.array = self.match(ExprParser.IDENT)
                self.state = 80
                self.match(ExprParser.T__7)
                self.state = 81
                localctx.index = self.expr(0)
                self.state = 82
                self.match(ExprParser.T__8)
                pass

            elif la_ == 4:
                self.state = 84
                localctx.bool_ = self.match(ExprParser.BOOL)
                pass

            elif la_ == 5:
                self.state = 85
                localctx.string = self.match(ExprParser.STRING)
                pass

            elif la_ == 6:
                self.state = 86
                self.match(ExprParser.T__0)
                self.state = 87
                localctx.exp = self.expr(0)
                self.state = 88
                self.match(ExprParser.T__1)
                pass

            elif la_ == 7:
                self.state = 90
                localctx.ident = self.match(ExprParser.IDENT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 102
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 94
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 95
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 97
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 98
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 100
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 101
                        localctx.right = self.expr(9)
                        pass

             
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




