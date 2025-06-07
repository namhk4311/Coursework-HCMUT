# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#end_statement1.
    def visitEnd_statement1(self, ctx:MiniGoParser.End_statement1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_declaration.
    def visitList_declaration(self, ctx:MiniGoParser.List_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_type.
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_statement.
    def visitBlock_statement(self, ctx:MiniGoParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_block_statement.
    def visitList_block_statement(self, ctx:MiniGoParser.List_block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_declare.
    def visitConst_declare(self, ctx:MiniGoParser.Const_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variable_declare.
    def visitVariable_declare(self, ctx:MiniGoParser.Variable_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl1.
    def visitVar_decl1(self, ctx:MiniGoParser.Var_decl1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl2.
    def visitVar_decl2(self, ctx:MiniGoParser.Var_decl2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl3.
    def visitVar_decl3(self, ctx:MiniGoParser.Var_decl3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_declare.
    def visitFunction_declare(self, ctx:MiniGoParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#input_param.
    def visitInput_param(self, ctx:MiniGoParser.Input_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_input_variable.
    def visitList_input_variable(self, ctx:MiniGoParser.List_input_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declare.
    def visitStruct_declare(self, ctx:MiniGoParser.Struct_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_type.
    def visitList_struct_type(self, ctx:MiniGoParser.List_struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declare.
    def visitMethod_declare(self, ctx:MiniGoParser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declare.
    def visitInterface_declare(self, ctx:MiniGoParser.Interface_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_interface_method.
    def visitList_interface_method(self, ctx:MiniGoParser.List_interface_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_method_interface.
    def visitParam_method_interface(self, ctx:MiniGoParser.Param_method_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_input_method.
    def visitList_input_method(self, ctx:MiniGoParser.List_input_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_array.
    def visitType_array(self, ctx:MiniGoParser.Type_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_index.
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array.
    def visitList_array(self, ctx:MiniGoParser.List_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_block.
    def visitList_array_block(self, ctx:MiniGoParser.List_array_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_block.
    def visitArray_block(self, ctx:MiniGoParser.Array_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_element.
    def visitList_struct_element(self, ctx:MiniGoParser.List_struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_element.
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_literal.
    def visitFunction_literal(self, ctx:MiniGoParser.Function_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs_assign_statement.
    def visitLhs_assign_statement(self, ctx:MiniGoParser.Lhs_assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_sign.
    def visitAssign_sign(self, ctx:MiniGoParser.Assign_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rhs_assign_statement.
    def visitRhs_assign_statement(self, ctx:MiniGoParser.Rhs_assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiple_else_if.
    def visitMultiple_else_if(self, ctx:MiniGoParser.Multiple_else_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_statement.
    def visitElse_if_statement(self, ctx:MiniGoParser.Else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_scalar.
    def visitAssign_scalar(self, ctx:MiniGoParser.Assign_scalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_scalar.
    def visitVar_scalar(self, ctx:MiniGoParser.Var_scalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for1.
    def visitFor1(self, ctx:MiniGoParser.For1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for2.
    def visitFor2(self, ctx:MiniGoParser.For2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for3.
    def visitFor3(self, ctx:MiniGoParser.For3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for4.
    def visitFor4(self, ctx:MiniGoParser.For4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_component.
    def visitCall_component(self, ctx:MiniGoParser.Call_componentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)



del MiniGoParser