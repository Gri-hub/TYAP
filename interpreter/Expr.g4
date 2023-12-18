grammar Expr;
SPACES : [ \t] -> skip;
LINE_COMMENT: '//' .*? '\r'? '\n' -> skip;

MAIN: 'main';

NEWLINE : [\r\n]+ ;

INT     : [0-9]+ ;
BOOL : ('true'|'false');
STRING: '"' .*? '"';

IDENT   : [a-zA-Z]+ ;


prog:  'main' '(' ')' '{' NEWLINE ((stmt NEWLINE)*) '}'
    ;
stmt: 'print' '(' printexp=expr ')'
    | 'if' if_condition=expr '{' NEWLINE ((stmt NEWLINE)*) '}'
    | 'while' while_condition=expr '{' NEWLINE ((stmt NEWLINE)*) '}'
    | (ident=IDENT | ident=IDENT '[' index=expr ']') ('=') assign=expr
    ;
expr:   left=expr op=('*'|'/') right=expr // MulExpression | DivExpression
    |   left=expr op=('+'|'-') right=expr // AddExpression | SubExpression
    |   left=expr op=('<' | '>' | '==' | '!=') right=expr // MoreExp | LessExp | EqualExp | NotEqualExp
    |   num=INT // NumberExpression
    |   '[' (element=expr ',')* ']' // ArrayExpression
    |   array=IDENT '[' index=expr ']' // AccessByIndexExpression
    |   bool=BOOL // BoolExpression
    |   string=STRING // StrExpression
    |   '(' exp=expr ')' // BraceExpression
    |   ident=IDENT // IdentExpression
    ;