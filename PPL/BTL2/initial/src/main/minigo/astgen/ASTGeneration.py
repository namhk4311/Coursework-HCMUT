from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    # Visit a parse tree produced by MiniGoParser#end_statement1.
    def visitEnd_statement1(self, ctx:MiniGoParser.End_statement1Context):
        return self.visitChildren(ctx)


    # program: NEWLINE* list_declaration EOF;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.list_declaration()))


    # list_declaration: declaration (declaration | NEWLINE)*;
    def visitList_declaration(self, ctx:MiniGoParser.List_declarationContext):
        return [self.visit(dec) for dec in ctx.declaration()]   

    # data_type: 
    # primitive_type
    # | type_array
    # | ID // struct object name
    # ;
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        if ctx.type_array():
            return ArrayType(*self.visit(ctx.type_array()))
        return Id(ctx.ID().getText())

    # primitive_type: INT | FLOAT | BOOLEAN | STRING;
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        return StringType()

    # literal: INT_LIT	| FLOAT_LIT | STRING_LIT | NIL | TRUE | FALSE | array_literal | struct_literal | function_literal;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        if ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText())
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        if ctx.function_literal():
            return self.visit(ctx.function_literal())
        if ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        return NilLiteral()

    # declaration: 
    # variable_declare 
    # | const_declare
    # | function_declare 
    # | struct_declare 
    # | method_declare 
    # | interface_declare
    # ;
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    # block_statement: 
    # const_declare 
    # | variable_declare 
    # | statement 
    # ;
    def visitBlock_statement(self, ctx:MiniGoParser.Block_statementContext):
        return self.visit(ctx.getChild(0))

    # list_block_statement: block_statement list_block_statement?;
    def visitList_block_statement(self, ctx:MiniGoParser.List_block_statementContext):
        if ctx.list_block_statement():
            return [self.visit(ctx.block_statement())] + self.visit(ctx.list_block_statement())
        return [self.visit(ctx.block_statement())]


    # const_declare: CONST ID ASSIGNINIT expression end_statement1;
    def visitConst_declare(self, ctx:MiniGoParser.Const_declareContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))

    # variable_declare: var_decl1 | var_decl2 | var_decl3;
    def visitVariable_declare(self, ctx:MiniGoParser.Variable_declareContext):
        return self.visit(ctx.getChild(0))

    # var_decl1: VAR ID data_type end_statement1;
    def visitVar_decl1(self, ctx:MiniGoParser.Var_decl1Context):
        return VarDecl(ctx.ID().getText(), self.visit(ctx.data_type()), None)


    # var_decl2: VAR ID ASSIGNINIT expression end_statement1;
    def visitVar_decl2(self, ctx:MiniGoParser.Var_decl2Context):
        return VarDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


    # var_decl3: VAR ID data_type ASSIGNINIT expression end_statement1;
    def visitVar_decl3(self, ctx:MiniGoParser.Var_decl3Context):
        return VarDecl(ctx.ID().getText(), self.visit(ctx.data_type()), self.visit(ctx.expression()))

    # function_declare: FUNC ID LP input_param? RP data_type? 
    # LB 
    #     (NEWLINE* 
    #         list_block_statement?
    #     ) 
    # RB
    # end_statement1;
    def visitFunction_declare(self, ctx:MiniGoParser.Function_declareContext):
        return FuncDecl(ctx.ID().getText(), self.visit(ctx.input_param()) if ctx.input_param() else [], self.visit(ctx.data_type()) if ctx.data_type() else VoidType(), Block(self.visit(ctx.list_block_statement())) if ctx.list_block_statement() else Block([])) 

    # input_param: list_input_variable data_type CM input_param | (list_input_variable data_type); 
    def visitInput_param(self, ctx:MiniGoParser.Input_paramContext):
        list_variable = self.visit(ctx.list_input_variable())
        all_list = [ParamDecl(variable, self.visit(ctx.data_type())) for variable in list_variable]
        if ctx.input_param():
            return all_list + self.visit(ctx.input_param())
        return all_list
        
    # list_input_variable: ID CM list_input_variable | ID;  
    def visitList_input_variable(self, ctx:MiniGoParser.List_input_variableContext):
        if ctx.list_input_variable():
            return [ctx.ID().getText()] + self.visit(ctx.list_input_variable())
        return [ctx.ID().getText()]

    # struct_declare: TYPE ID STRUCT (LB (NEWLINE* list_struct_type) RB) end_statement1;
    def visitStruct_declare(self, ctx:MiniGoParser.Struct_declareContext):
        return StructType(ctx.ID().getText(), self.visit(ctx.list_struct_type()), [])

    # list_struct_type: struct_type end_statement1 list_struct_type | struct_type end_statement1; 
    def visitList_struct_type(self, ctx:MiniGoParser.List_struct_typeContext):
        if ctx.list_struct_type():
            return [self.visit(ctx.struct_type())] + self.visit(ctx.list_struct_type())
        return [self.visit(ctx.struct_type())]

    # struct_type: ID data_type;
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return (ctx.ID().getText(), self.visit(ctx.data_type()))


    # method_declare: FUNC (LP ID ID RP) ID LP input_param? RP data_type? 
    # LB 
    #     (NEWLINE*
    #         list_block_statement?
    #     ) 
    # RB
    # end_statement1;
    def visitMethod_declare(self, ctx:MiniGoParser.Method_declareContext):
        return MethodDecl(ctx.ID(0).getText(), Id(ctx.ID(1).getText()), FuncDecl(ctx.ID(2).getText(), self.visit(ctx.input_param()) if ctx.input_param() else [], self.visit(ctx.data_type()) if ctx.data_type() else VoidType(), Block(self.visit(ctx.list_block_statement())) if ctx.list_block_statement() else Block([])))


    # Vinterface_declare: TYPE ID INTERFACE (LB (NEWLINE* list_interface_method) RB) end_statement1;
    def visitInterface_declare(self, ctx:MiniGoParser.Interface_declareContext):
        return InterfaceType(ctx.ID().getText(), self.visit(ctx.list_interface_method()))


    # list_interface_method: (interface_method end_statement1 list_interface_method) | (interface_method end_statement1);
    def visitList_interface_method(self, ctx:MiniGoParser.List_interface_methodContext):
        if ctx.list_interface_method():
            return [self.visit(ctx.interface_method())] + self.visit(ctx.list_interface_method())
        return [self.visit(ctx.interface_method())]


    # interface_method: ID (LP param_method_interface? RP) data_type?;
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        return Prototype(ctx.ID().getText(), self.visit(ctx.param_method_interface()) if ctx.param_method_interface() else [], self.visit(ctx.data_type()) if ctx.data_type() else VoidType())
    
    # param_method_interface: list_input_method data_type CM param_method_interface | list_input_method data_type;
    def visitParam_method_interface(self, ctx:MiniGoParser.Param_method_interfaceContext):
        list_input = self.visit(ctx.list_input_method())
        list_data_type = [self.visit(ctx.data_type()) for _ in list_input]
        if ctx.param_method_interface():
            return list_data_type + self.visit(ctx.param_method_interface())
        return list_data_type


    # list_input_method: ID CM list_input_method | ID;
    def visitList_input_method(self, ctx:MiniGoParser.List_input_methodContext):
        if ctx.list_input_method():
            return [ctx.ID().getText()] + self.visit(ctx.list_input_method())
        return [ctx.ID().getText()]


    # array_literal: type_array list_array;
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return ArrayLiteral(*self.visit(ctx.type_array()), self.visit(ctx.list_array()))

    # type_array: array_index (primitive_type | ID);
    def visitType_array(self, ctx:MiniGoParser.Type_arrayContext):
        return (self.visit(ctx.array_index()), self.visit(ctx.primitive_type()) if ctx.primitive_type() else Id(ctx.ID().getText()))


    # array_index: LSB (INT_LIT | ID) RSB array_index?;
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        if ctx.array_index():
            return [IntLiteral(ctx.INT_LIT().getText()) if ctx.INT_LIT() else Id(ctx.ID().getText())] + self.visit(ctx.array_index())
        return [IntLiteral(ctx.INT_LIT().getText()) if ctx.INT_LIT() else Id(ctx.ID().getText())]

    # list_array: LB list_array_block RB ;
    def visitList_array(self, ctx:MiniGoParser.List_arrayContext):
        return self.visit(ctx.list_array_block())

    # list_array_block: array_block CM list_array_block | array_block; 
    def visitList_array_block(self, ctx:MiniGoParser.List_array_blockContext):
        if ctx.list_array_block():
            return [self.visit(ctx.array_block())] + self.visit(ctx.list_array_block())
        return [self.visit(ctx.array_block())]

    # array_block: array_element | list_array;
    def visitArray_block(self, ctx:MiniGoParser.Array_blockContext):
        return self.visit(ctx.getChild(0))

    # array_element: 
    # ID 
    # | INT_LIT 
    # | FLOAT_LIT 
    # | STRING_LIT 
    # | NIL 
    # | TRUE 
    # | FALSE 
    # | struct_literal 
    # | function_literal;
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        if ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText())
        if ctx.function_literal():
            return self.visit(ctx.function_literal())
        if ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        return NilLiteral()

    # struct_literal: ID LB list_struct_element? RB;
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return StructLiteral(ctx.ID().getText(), self.visit(ctx.list_struct_element()) if ctx.list_struct_element() else [])

    # list_struct_element: struct_element CM list_struct_element | struct_element;
    def visitList_struct_element(self, ctx:MiniGoParser.List_struct_elementContext):
        if ctx.list_struct_element():
            return [self.visit(ctx.struct_element())] + self.visit(ctx.list_struct_element())
        return [self.visit(ctx.struct_element())]

    # struct_element: ID CL expression;
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        return (ctx.ID().getText(), self.visit(ctx.expression()))

    # function_literal: ID LP list_expression? RP;
    def visitFunction_literal(self, ctx:MiniGoParser.Function_literalContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])

    # condition: expression;
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visit(ctx.expression())

    # statement: assign_statement | if_statement | for_statement | break_statement | continue_statement | return_statement | call_statement;
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visit(ctx.getChild(0))

    # assign_statement: lhs_assign_statement assign_sign rhs_assign_statement;
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        op = self.visit(ctx.assign_sign())
        if op == ":":
            return Assign(self.visit(ctx.lhs_assign_statement()), self.visit(ctx.rhs_assign_statement()))
        return Assign(self.visit(ctx.lhs_assign_statement()), BinaryOp(op, self.visit(ctx.lhs_assign_statement()), self.visit(ctx.rhs_assign_statement())))

    # lhs_assign_statement: lhs_assign_statement DOT ID | lhs_assign_statement LSB expression RSB | ID;
    def visitLhs_assign_statement(self, ctx:MiniGoParser.Lhs_assign_statementContext):
        if ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.lhs_assign_statement()), ctx.ID().getText())
        if ctx.getChildCount() == 4:
            array = self.visit(ctx.lhs_assign_statement())
            if type(array) == ArrayCell:
                return ArrayCell(array.arr, array.idx + [self.visit(ctx.expression())])
            return ArrayCell(self.visit(ctx.lhs_assign_statement()), [self.visit(ctx.expression())])
        return Id(ctx.ID().getText())

    # assign_sign: ASSIGN | ASSIGNADD | ASSIGNSUB | ASSIGNMUL | ASSIGNDIV | ASSIGNMOD;
    def visitAssign_sign(self, ctx:MiniGoParser.Assign_signContext):
        if ctx.ASSIGNADD():
            return "+"
        if ctx.ASSIGNSUB():
            return "-"
        if ctx.ASSIGNMUL():
            return "*"
        if ctx.ASSIGNDIV():
            return "/"
        if ctx.ASSIGNMOD():
            return "%"
        return ":"
        
    # rhs_assign_statement: expression;
    def visitRhs_assign_statement(self, ctx:MiniGoParser.Rhs_assign_statementContext):
        return self.visit(ctx.expression())

    # if_statement: 
    # IF LP condition RP
    # LB 
    #     (NEWLINE*)
    #     (
    #         list_block_statement?
    #     )
    # RB 
    # (
    #     multiple_else_if?
    #     else_statement?
    # )
    # end_statement1;
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        def else_if(list_else_if: List[tuple[Expr,Block]], else_statement: Block):
            if len(list_else_if) == 0:
                return else_statement
            exp, block = list_else_if[0]
            return If(exp, block, else_if(list_else_if[1:], else_statement))
        return If(self.visit(ctx.condition()), Block(self.visit(ctx.list_block_statement())) if ctx.list_block_statement() else Block([]), else_if(self.visit(ctx.multiple_else_if()) if ctx.multiple_else_if() else [], self.visit(ctx.else_statement()) if ctx.else_statement() else None))

    # multiple_else_if: else_if_statement multiple_else_if | else_if_statement;
    def visitMultiple_else_if(self, ctx:MiniGoParser.Multiple_else_ifContext):
        if ctx.multiple_else_if():
            return [self.visit(ctx.else_if_statement())] + self.visit(ctx.multiple_else_if())
        return [self.visit(ctx.else_if_statement())]

    # else_if_statement: 
    # ELSE IF LP condition RP
    # LB
    #     (NEWLINE*)
    #     (
    #         list_block_statement?
    #     )
    # RB;
    def visitElse_if_statement(self, ctx:MiniGoParser.Else_if_statementContext):
        return (self.visit(ctx.condition()), Block(self.visit(ctx.list_block_statement())) if ctx.list_block_statement() else Block([]))


    # else_statement:
    # ELSE
    # LB 
    #     (NEWLINE*)
    #     (
    #         list_block_statement?
    #     )
    # RB;
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return Block(self.visit(ctx.list_block_statement())) if ctx.list_block_statement() else Block([])

    # for_statement: 
    # (
    # for1
    # | for2
    # | for3
    # | for4
    # )
    # end_statement1;
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        if ctx.for1():
            return self.visit(ctx.for1())
        if ctx.for2():
            return self.visit(ctx.for2())
        if ctx.for3():
            return self.visit(ctx.for3())
        return self.visit(ctx.for4())

    # assign_scalar: ID assign_sign rhs_assign_statement;
    def visitAssign_scalar(self, ctx:MiniGoParser.Assign_scalarContext):
        op = self.visit(ctx.assign_sign())
        if op == ":":
            return Assign(Id(ctx.ID().getText()), self.visit(ctx.rhs_assign_statement()))
        return Assign(Id(ctx.ID().getText()), BinaryOp(op, Id(ctx.ID().getText()), self.visit(ctx.rhs_assign_statement())))

    # var_scalar: VAR ID data_type? ASSIGNINIT expression;
    def visitVar_scalar(self, ctx:MiniGoParser.Var_scalarContext):
        return VarDecl(ctx.ID().getText(), self.visit(ctx.data_type()) if ctx.data_type() else None, self.visit(ctx.expression()))


    # for1:
    # FOR condition 
    #     LB 
    #         NEWLINE*
    #         (
    #             list_block_statement?
    #         )
    #     RB;
    def visitFor1(self, ctx:MiniGoParser.For1Context):
        return ForBasic(self.visit(ctx.condition()), Block(self.visit(ctx.list_block_statement())) if ctx.list_block_statement() else Block([]))


    # for2:
    # FOR var_scalar end_statement1 condition end_statement1 assign_scalar
    #     LB 
    #         NEWLINE*
    #         (
    #             list_block_statement?
    #         )
    #     RB;
    def visitFor2(self, ctx:MiniGoParser.For2Context):
        return ForStep(self.visit(ctx.var_scalar()), self.visit(ctx.condition()), self.visit(ctx.assign_scalar()), Block(self.visit(ctx.list_block_statement())) if ctx.list_block_statement() else Block([]))


    # for3:
    # FOR assign_scalar end_statement1 condition end_statement1 assign_scalar 
    #     LB 
    #         NEWLINE*
    #         (
    #             list_block_statement?
    #         )
    #     RB;
    def visitFor3(self, ctx:MiniGoParser.For3Context):
        return ForStep(self.visit(ctx.assign_scalar(0)), self.visit(ctx.condition()), self.visit(ctx.assign_scalar(1)), Block(self.visit(ctx.list_block_statement())) if ctx.list_block_statement() else Block([]))


    # for4:
    # FOR ID CM ID ASSIGN RANGE expression
    #     LB 
    #         NEWLINE*
    #         (
    #             list_block_statement?
    #         )
    #     RB;
    def visitFor4(self, ctx:MiniGoParser.For4Context):
        return ForEach(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), self.visit(ctx.expression()), Block(self.visit(ctx.list_block_statement())) if ctx.list_block_statement() else Block([]))

    # break_statement: BREAK end_statement1;
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()

    # continue_statement: CONTINUE end_statement1;
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()

    # return_statement: RETURN expression? end_statement1;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return Return(self.visit(ctx.expression()) if ctx.expression() else None)


    # call_component end_statement1;
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visit(ctx.call_component())


    # call_component: call_component DOT ID | call_component DOT ID LP list_expression? RP | ID LP list_expression? RP | call_component LSB expression RSB | ID;
    def visitCall_component(self, ctx:MiniGoParser.Call_componentContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        if ctx.getChildCount() == 3 and ctx.DOT():
            return FieldAccess(self.visit(ctx.call_component()), ctx.ID().getText())
        if ctx.LSB() and ctx.RSB():
            array = self.visit(ctx.call_component())
            if type(array) == ArrayCell:
                return ArrayCell(array.arr, array.idx + [self.visit(ctx.expression())])
            return ArrayCell(self.visit(ctx.call_component()), [self.visit(ctx.expression())])
        if ctx.DOT() and ctx.ID() and ctx.LP() and ctx.RP():
            return MethCall(self.visit(ctx.call_component()), ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])
        return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])


    # list_expression: expression CM list_expression | expression;
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        if ctx.list_expression():
            return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())
        return [self.visit(ctx.expression())]        


    # expression: expression OR expression1 | expression1;
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        
        op = ctx.OR().getText()
        left = self.visit(ctx.expression())
        right = self.visit(ctx.expression1())
        return BinaryOp(op, left, right)


    # expression1: expression1 AND expression2 | expression2;
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2())
        
        op = ctx.AND().getText()
        left = self.visit(ctx.expression1())
        right = self.visit(ctx.expression2())
        return BinaryOp(op, left, right)


    # expression2: expression2 (EQ | INEQ | LT | LTE | GT | GTE) expression3 | expression3;
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        
        op = ''
        if ctx.EQ():
            op = ctx.EQ().getText()
        elif ctx.INEQ():
            op = ctx.INEQ().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.LTE():
            op = ctx.LTE().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.GTE():
            op = ctx.GTE().getText()

        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())
        return BinaryOp(op, left, right)


    # expression3: expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        
        op = ''
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()

        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinaryOp(op, left, right)


    # expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        
        op = ''
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()

        left = self.visit(ctx.expression4())
        right = self.visit(ctx.expression5())
        return BinaryOp(op, left, right)


    # expression5: (NOT | SUB) expression5 | expression6;
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        
        op = ''
        if ctx.NOT():
            op = ctx.NOT().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        return UnaryOp(op, self.visit(ctx.expression5()))


    # expression6: expression6 DOT ID | expression6 DOT ID LP list_expression? RP | expression6 LSB expression RSB | expression7;
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        if ctx.getChildCount() == 3 and ctx.DOT():
            return FieldAccess(self.visit(ctx.expression6()), ctx.ID().getText())
        if ctx.LSB() and ctx.RSB():
            array = self.visit(ctx.expression6())
            if type(array) == ArrayCell:
                return ArrayCell(array.arr, array.idx + [self.visit(ctx.expression())])
            return ArrayCell(array, [self.visit(ctx.expression())])
        return MethCall(self.visit(ctx.expression6()), ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])


    # expression7: ID | literal | LP expression RP;
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.literal():
            return self.visit(ctx.literal())
        return self.visit(ctx.expression())