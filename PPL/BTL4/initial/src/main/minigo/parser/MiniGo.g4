// 2252500

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {    
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}


// ============================== Lexer ==============================
// a. keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

// b. Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '==';
INEQ: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGNINIT: '=';
ASSIGNADD: '+=';
ASSIGNSUB: '-=';
ASSIGNMUL: '*=';
ASSIGNDIV: '/=';
ASSIGNMOD: '%=';
ASSIGN: ':=';
DOT: '.';

// c. Separator
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
LB: '{';
RB: '}';
CM: ',';
SC: ';';
CL: ':';

// d. Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// e. Literal
INT_LIT: DEC_INT | BIN_INT | OCT_INT | HEX_INT;
fragment DEC_INT: [0-9] | [1-9]+[0-9]*;
fragment BIN_INT: [0][bB][01]+;
fragment OCT_INT: [0][oO][0-7]+;
fragment HEX_INT: [0][xX][0-9a-fA-F]+ ;

FLOAT_LIT: DIGIT DOT [0-9]*(EXPO SIGN? DIGIT)?;
fragment DIGIT: [0-9]+[0-9]*;
fragment SIGN: [+-];
fragment EXPO: [eE];

STRING_LIT: '"' STR* '"';
fragment STR: ~([\n\\"]) | ESC_CHAR;
fragment ESC_CHAR: '\\'[ntr"\\];
fragment ESC_ILL: '\\' ~[ntr\\];


// f. Comments and Whitespace
NEWLINE: '\r'?'\n' {
    if (self.preType == self.ID) or (self.preType == self.INT) or (self.preType == self.FLOAT) or (self.preType == self.STRING) or (self.preType == self.BOOLEAN) or (self.preType == self.NIL) or (self.preType == self.INT_LIT) or (self.preType == self.FLOAT_LIT) or (self.preType == self.STRING_LIT) or (self.preType == self.RP) or (self.preType == self.RB) or (self.preType == self.RSB) or (self.preType == self.RETURN) or (self.preType == self.CONTINUE) or (self.preType == self.BREAK) or (self.preType == self.TRUE) or (self.preType == self.FALSE):
        self.text = ';' 
    else:
        self.skip()
};
WS: [ \t\f\r]+ -> skip; // skip spaces, tabs 
SINGLE_LINE_COMMENT: '//' ~[\n]* -> skip;
MULTIPLE_LINE_COMMENT: '/*' (MULTIPLE_LINE_COMMENT | .)*? '*/' -> skip;

// g. Error Handle
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: 
    UNCLOSE_1 {
        if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
            raise UncloseString(self.text[0:-2])
        elif (self.text[-1] == '\n'):
            raise UncloseString(self.text[0:-1])
        else:
            raise UncloseString(self.text[0:])
    }
    | UNCLOSE_2 {
        if (self.text[1] == '"'):
            raise UncloseString(self.text[1:-1])
    };
fragment UNCLOSE_1: '"' STR* ('\r\n' | '\n' | EOF);
fragment UNCLOSE_2: '"' '"' STR* '"';

ILLEGAL_ESCAPE: '"' STR* ESC_ILL {
	raise IllegalEscape(self.text[0:])
};

// ============================== End Lexer ==============================

// ============================== PARSER ==============================

end_statement1: SC NEWLINE* | NEWLINE+;
program: NEWLINE* list_declaration EOF;
list_declaration: declaration (declaration | NEWLINE)*;
data_type: 
    primitive_type
    | type_array
    | ID // struct object name
    ;

primitive_type: 
    INT 
    | FLOAT 
    | BOOLEAN 
    | STRING
    ;

literal:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
    | NIL
    | TRUE 
    | FALSE
	| array_literal
	| struct_literal
    | function_literal
    ;

declaration: 
    variable_declare 
    | const_declare
    | function_declare 
    | struct_declare 
    | method_declare 
    | interface_declare
    ;

block_statement: 
    const_declare 
    | variable_declare 
    | statement 
    ;

list_block_statement: block_statement list_block_statement?; // no need NEWLINE* since it is added in statement, const_declare and variable_declare in block_statement

const_declare: CONST ID ASSIGNINIT expression end_statement1;

variable_declare: var_decl1 | var_decl2 | var_decl3;
    var_decl1: VAR ID data_type end_statement1;
    var_decl2: VAR ID ASSIGNINIT expression end_statement1;
    var_decl3: VAR ID data_type ASSIGNINIT expression end_statement1;

function_declare: FUNC ID LP input_param? RP data_type? 
    LB 
        NEWLINE* 
            list_block_statement?
    RB
end_statement1;
    input_param: list_input_variable data_type CM input_param | list_input_variable data_type; 
        list_input_variable: ID CM list_input_variable | ID;     

struct_declare: TYPE ID STRUCT
    LB 
        NEWLINE* 
            list_struct_type 
    RB 
    end_statement1;
    
    list_struct_type: struct_type end_statement1 list_struct_type | struct_type end_statement1; 
        struct_type: ID data_type;


method_declare: FUNC (LP ID ID RP) ID LP input_param? RP data_type? 
    LB 
        NEWLINE*
            list_block_statement?
    RB
end_statement1;


// Interface
interface_declare: TYPE ID INTERFACE (LB (NEWLINE* list_interface_method) RB) end_statement1;
    list_interface_method: (interface_method end_statement1 list_interface_method) | (interface_method end_statement1);
        interface_method: ID (LP param_method_interface? RP) data_type?;
            param_method_interface: list_input_method data_type CM param_method_interface | list_input_method data_type;
                list_input_method: ID CM list_input_method | ID;
            

array_literal: type_array list_array;
    type_array: array_index (primitive_type | ID);
        array_index: LSB (INT_LIT | ID) RSB array_index?;
    list_array: LB list_array_block RB ;
        list_array_block: array_block CM list_array_block | array_block; 
            array_block: array_element | list_array;
                array_element: 
                    ID 
                    | INT_LIT 
                    | FLOAT_LIT 
                    | STRING_LIT 
                    | NIL 
                    | TRUE 
                    | FALSE 
                    | struct_literal 
                    | function_literal;

struct_literal: ID LB list_struct_element? RB;
    list_struct_element: struct_element CM list_struct_element | struct_element;
        struct_element: ID CL expression;

function_literal: ID LP list_expression? RP; // CALL FUNCTION

condition: expression;
statement: assign_statement | if_statement | for_statement | break_statement | continue_statement | return_statement | call_statement;
assign_statement: lhs_assign_statement assign_sign rhs_assign_statement end_statement1;
    lhs_assign_statement: lhs_assign_statement LSB expression RSB | lhs_assign_statement DOT ID | ID;
    assign_sign: ASSIGN | ASSIGNADD | ASSIGNSUB | ASSIGNMUL | ASSIGNDIV | ASSIGNMOD;
    rhs_assign_statement: expression;

if_statement: 
    IF LP condition RP
    LB 
        (NEWLINE*)
        (
            list_block_statement?
        )
    RB 
    (
        multiple_else_if?
        else_statement?
    )
    end_statement1;

multiple_else_if: else_if_statement multiple_else_if | else_if_statement;

else_if_statement: 
    ELSE IF LP condition RP
    LB
        (NEWLINE*)
        (
            list_block_statement?
        )
    RB;

else_statement:
    ELSE
    LB 
        (NEWLINE*)
        (
            list_block_statement?
        )
    RB;


assign_scalar: ID assign_sign rhs_assign_statement;
var_scalar: VAR ID data_type? ASSIGNINIT expression;

for_statement: 
    (
    for1
    | for2
    | for3
    | for4
    )
    end_statement1;

for1:
    FOR condition 
        LB 
            NEWLINE*
            (
                list_block_statement?
            )
        RB;

for2:
    FOR var_scalar end_statement1 condition end_statement1 assign_scalar
        LB 
            NEWLINE*
            (
                list_block_statement?
            )
        RB;

for3:
    FOR assign_scalar end_statement1 condition end_statement1 assign_scalar 
        LB 
            NEWLINE*
            (
                list_block_statement?
            )
        RB;



for4:
    FOR ID CM ID ASSIGN RANGE expression
        LB 
            NEWLINE*
            (
                list_block_statement?
            )
        RB;


break_statement: BREAK end_statement1;

continue_statement: CONTINUE end_statement1;

return_statement: RETURN expression? end_statement1;

call_statement: call_component end_statement1;
    call_component: call_component DOT ID | call_component DOT ID LP list_expression? RP | ID LP list_expression? RP | call_component LSB expression RSB | ID;

list_expression: expression CM list_expression | expression;
    expression: expression OR expression1 | expression1;
        expression1: expression1 AND expression2 | expression2;
            expression2: expression2 (EQ | INEQ | LT | LTE | GT | GTE) expression3 | expression3;
                expression3: expression3 (ADD | SUB) expression4 | expression4;
                    expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
                        expression5: (NOT | SUB) expression5 | expression6;
                            expression6: expression6 DOT ID | expression6 DOT ID LP list_expression? RP | expression6 LSB expression RSB | expression7;
                                expression7: ID | literal | LP expression RP;

// ============================== End PARSER ==============================

