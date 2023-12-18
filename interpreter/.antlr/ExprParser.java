// Generated from /home/dan/Desktop/dev/mipt/my-lang/interpreter/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, SPACES=20, LINE_COMMENT=21, COMMENT=22, FUN=23, MAIN=24, 
		NEWLINE=25, INT=26, BOOL=27, STRING=28, IDENT=29;
	public static final int
		RULE_prog = 0, RULE_stmt = 1, RULE_expr = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stmt", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'print'", "'if'", "'while'", "'['", 
			"']'", "'='", "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", "'=='", "'!='", 
			"','", null, null, null, "'fun'", "'main'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "SPACES", "LINE_COMMENT", 
			"COMMENT", "FUN", "MAIN", "NEWLINE", "INT", "BOOL", "STRING", "IDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public TerminalNode FUN() { return getToken(ExprParser.FUN, 0); }
		public TerminalNode MAIN() { return getToken(ExprParser.MAIN, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(ExprParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ExprParser.NEWLINE, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(6);
			match(FUN);
			setState(7);
			match(MAIN);
			setState(8);
			match(T__0);
			setState(9);
			match(T__1);
			setState(10);
			match(T__2);
			setState(11);
			match(NEWLINE);
			{
			setState(17);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 536871136L) != 0)) {
				{
				{
				setState(12);
				stmt();
				setState(13);
				match(NEWLINE);
				}
				}
				setState(19);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(20);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtContext extends ParserRuleContext {
		public ExprContext printexp;
		public ExprContext if_condition;
		public ExprContext while_condition;
		public Token ident;
		public ExprContext index;
		public ExprContext assign;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(ExprParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ExprParser.NEWLINE, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public TerminalNode IDENT() { return getToken(ExprParser.IDENT, 0); }
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stmt);
		int _la;
		try {
			setState(65);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				enterOuterAlt(_localctx, 1);
				{
				setState(22);
				match(T__4);
				setState(23);
				match(T__0);
				setState(24);
				((StmtContext)_localctx).printexp = expr(0);
				setState(25);
				match(T__1);
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				match(T__5);
				setState(28);
				((StmtContext)_localctx).if_condition = expr(0);
				setState(29);
				match(T__2);
				setState(30);
				match(NEWLINE);
				{
				setState(36);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 536871136L) != 0)) {
					{
					{
					setState(31);
					stmt();
					setState(32);
					match(NEWLINE);
					}
					}
					setState(38);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				setState(39);
				match(T__3);
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 3);
				{
				setState(41);
				match(T__6);
				setState(42);
				((StmtContext)_localctx).while_condition = expr(0);
				setState(43);
				match(T__2);
				setState(44);
				match(NEWLINE);
				{
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 536871136L) != 0)) {
					{
					{
					setState(45);
					stmt();
					setState(46);
					match(NEWLINE);
					}
					}
					setState(52);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				setState(53);
				match(T__3);
				}
				break;
			case IDENT:
				enterOuterAlt(_localctx, 4);
				{
				setState(61);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
				case 1:
					{
					setState(55);
					((StmtContext)_localctx).ident = match(IDENT);
					}
					break;
				case 2:
					{
					setState(56);
					((StmtContext)_localctx).ident = match(IDENT);
					setState(57);
					match(T__7);
					setState(58);
					((StmtContext)_localctx).index = expr(0);
					setState(59);
					match(T__8);
					}
					break;
				}
				{
				setState(63);
				match(T__9);
				}
				setState(64);
				((StmtContext)_localctx).assign = expr(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext left;
		public Token num;
		public ExprContext element;
		public Token array;
		public ExprContext index;
		public Token bool;
		public Token string;
		public ExprContext exp;
		public Token ident;
		public Token op;
		public ExprContext right;
		public TerminalNode INT() { return getToken(ExprParser.INT, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode IDENT() { return getToken(ExprParser.IDENT, 0); }
		public TerminalNode BOOL() { return getToken(ExprParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(ExprParser.STRING, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(68);
				((ExprContext)_localctx).num = match(INT);
				}
				break;
			case 2:
				{
				setState(69);
				match(T__7);
				setState(75);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1006633218L) != 0)) {
					{
					{
					setState(70);
					((ExprContext)_localctx).element = expr(0);
					setState(71);
					match(T__18);
					}
					}
					setState(77);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(78);
				match(T__8);
				}
				break;
			case 3:
				{
				setState(79);
				((ExprContext)_localctx).array = match(IDENT);
				setState(80);
				match(T__7);
				setState(81);
				((ExprContext)_localctx).index = expr(0);
				setState(82);
				match(T__8);
				}
				break;
			case 4:
				{
				setState(84);
				((ExprContext)_localctx).bool = match(BOOL);
				}
				break;
			case 5:
				{
				setState(85);
				((ExprContext)_localctx).string = match(STRING);
				}
				break;
			case 6:
				{
				setState(86);
				match(T__0);
				setState(87);
				((ExprContext)_localctx).exp = expr(0);
				setState(88);
				match(T__1);
				}
				break;
			case 7:
				{
				setState(90);
				((ExprContext)_localctx).ident = match(IDENT);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(104);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(102);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(93);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(94);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__10 || _la==T__11) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(95);
						((ExprContext)_localctx).right = expr(11);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(96);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(97);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__12 || _la==T__13) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(98);
						((ExprContext)_localctx).right = expr(10);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(99);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(100);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 491520L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(101);
						((ExprContext)_localctx).right = expr(9);
						}
						break;
					}
					} 
				}
				setState(106);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 10);
		case 1:
			return precpred(_ctx, 9);
		case 2:
			return precpred(_ctx, 8);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001dl\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u0010"+
		"\b\u0000\n\u0000\f\u0000\u0013\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001"+
		"#\b\u0001\n\u0001\f\u0001&\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0005\u00011\b\u0001\n\u0001\f\u00014\t\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001>\b\u0001\u0001\u0001\u0001\u0001\u0003\u0001B\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005"+
		"\u0002J\b\u0002\n\u0002\f\u0002M\t\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002\\\b"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002g\b\u0002\n\u0002"+
		"\f\u0002j\t\u0002\u0001\u0002\u0000\u0001\u0004\u0003\u0000\u0002\u0004"+
		"\u0000\u0003\u0001\u0000\u000b\f\u0001\u0000\r\u000e\u0001\u0000\u000f"+
		"\u0012y\u0000\u0006\u0001\u0000\u0000\u0000\u0002A\u0001\u0000\u0000\u0000"+
		"\u0004[\u0001\u0000\u0000\u0000\u0006\u0007\u0005\u0017\u0000\u0000\u0007"+
		"\b\u0005\u0018\u0000\u0000\b\t\u0005\u0001\u0000\u0000\t\n\u0005\u0002"+
		"\u0000\u0000\n\u000b\u0005\u0003\u0000\u0000\u000b\u0011\u0005\u0019\u0000"+
		"\u0000\f\r\u0003\u0002\u0001\u0000\r\u000e\u0005\u0019\u0000\u0000\u000e"+
		"\u0010\u0001\u0000\u0000\u0000\u000f\f\u0001\u0000\u0000\u0000\u0010\u0013"+
		"\u0001\u0000\u0000\u0000\u0011\u000f\u0001\u0000\u0000\u0000\u0011\u0012"+
		"\u0001\u0000\u0000\u0000\u0012\u0014\u0001\u0000\u0000\u0000\u0013\u0011"+
		"\u0001\u0000\u0000\u0000\u0014\u0015\u0005\u0004\u0000\u0000\u0015\u0001"+
		"\u0001\u0000\u0000\u0000\u0016\u0017\u0005\u0005\u0000\u0000\u0017\u0018"+
		"\u0005\u0001\u0000\u0000\u0018\u0019\u0003\u0004\u0002\u0000\u0019\u001a"+
		"\u0005\u0002\u0000\u0000\u001aB\u0001\u0000\u0000\u0000\u001b\u001c\u0005"+
		"\u0006\u0000\u0000\u001c\u001d\u0003\u0004\u0002\u0000\u001d\u001e\u0005"+
		"\u0003\u0000\u0000\u001e$\u0005\u0019\u0000\u0000\u001f \u0003\u0002\u0001"+
		"\u0000 !\u0005\u0019\u0000\u0000!#\u0001\u0000\u0000\u0000\"\u001f\u0001"+
		"\u0000\u0000\u0000#&\u0001\u0000\u0000\u0000$\"\u0001\u0000\u0000\u0000"+
		"$%\u0001\u0000\u0000\u0000%\'\u0001\u0000\u0000\u0000&$\u0001\u0000\u0000"+
		"\u0000\'(\u0005\u0004\u0000\u0000(B\u0001\u0000\u0000\u0000)*\u0005\u0007"+
		"\u0000\u0000*+\u0003\u0004\u0002\u0000+,\u0005\u0003\u0000\u0000,2\u0005"+
		"\u0019\u0000\u0000-.\u0003\u0002\u0001\u0000./\u0005\u0019\u0000\u0000"+
		"/1\u0001\u0000\u0000\u00000-\u0001\u0000\u0000\u000014\u0001\u0000\u0000"+
		"\u000020\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u000035\u0001\u0000"+
		"\u0000\u000042\u0001\u0000\u0000\u000056\u0005\u0004\u0000\u00006B\u0001"+
		"\u0000\u0000\u00007>\u0005\u001d\u0000\u000089\u0005\u001d\u0000\u0000"+
		"9:\u0005\b\u0000\u0000:;\u0003\u0004\u0002\u0000;<\u0005\t\u0000\u0000"+
		"<>\u0001\u0000\u0000\u0000=7\u0001\u0000\u0000\u0000=8\u0001\u0000\u0000"+
		"\u0000>?\u0001\u0000\u0000\u0000?@\u0005\n\u0000\u0000@B\u0003\u0004\u0002"+
		"\u0000A\u0016\u0001\u0000\u0000\u0000A\u001b\u0001\u0000\u0000\u0000A"+
		")\u0001\u0000\u0000\u0000A=\u0001\u0000\u0000\u0000B\u0003\u0001\u0000"+
		"\u0000\u0000CD\u0006\u0002\uffff\uffff\u0000D\\\u0005\u001a\u0000\u0000"+
		"EK\u0005\b\u0000\u0000FG\u0003\u0004\u0002\u0000GH\u0005\u0013\u0000\u0000"+
		"HJ\u0001\u0000\u0000\u0000IF\u0001\u0000\u0000\u0000JM\u0001\u0000\u0000"+
		"\u0000KI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LN\u0001\u0000"+
		"\u0000\u0000MK\u0001\u0000\u0000\u0000N\\\u0005\t\u0000\u0000OP\u0005"+
		"\u001d\u0000\u0000PQ\u0005\b\u0000\u0000QR\u0003\u0004\u0002\u0000RS\u0005"+
		"\t\u0000\u0000S\\\u0001\u0000\u0000\u0000T\\\u0005\u001b\u0000\u0000U"+
		"\\\u0005\u001c\u0000\u0000VW\u0005\u0001\u0000\u0000WX\u0003\u0004\u0002"+
		"\u0000XY\u0005\u0002\u0000\u0000Y\\\u0001\u0000\u0000\u0000Z\\\u0005\u001d"+
		"\u0000\u0000[C\u0001\u0000\u0000\u0000[E\u0001\u0000\u0000\u0000[O\u0001"+
		"\u0000\u0000\u0000[T\u0001\u0000\u0000\u0000[U\u0001\u0000\u0000\u0000"+
		"[V\u0001\u0000\u0000\u0000[Z\u0001\u0000\u0000\u0000\\h\u0001\u0000\u0000"+
		"\u0000]^\n\n\u0000\u0000^_\u0007\u0000\u0000\u0000_g\u0003\u0004\u0002"+
		"\u000b`a\n\t\u0000\u0000ab\u0007\u0001\u0000\u0000bg\u0003\u0004\u0002"+
		"\ncd\n\b\u0000\u0000de\u0007\u0002\u0000\u0000eg\u0003\u0004\u0002\tf"+
		"]\u0001\u0000\u0000\u0000f`\u0001\u0000\u0000\u0000fc\u0001\u0000\u0000"+
		"\u0000gj\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001\u0000"+
		"\u0000\u0000i\u0005\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000"+
		"\t\u0011$2=AK[fh";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}