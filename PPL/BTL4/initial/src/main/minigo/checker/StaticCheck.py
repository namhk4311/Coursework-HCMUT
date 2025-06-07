"""
 * @author Ho Khanh Nam - 2252500
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import Tuple, List

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        self.list_type: list[Union[StructType, InterfaceType]] = []
        self.list_function: list[FuncDecl] = [
            FuncDecl("getInt", [], IntType(), Block([])),
            FuncDecl("putIntLn", [ParamDecl("i", IntType())], VoidType(), Block([])),
            FuncDecl("putInt", [ParamDecl("i", IntType())], VoidType(), Block([])),
            
            FuncDecl("getFloat", [], FloatType(), Block([])),
            FuncDecl("putFloat", [ParamDecl("f", FloatType())], VoidType(), Block([])),
            FuncDecl("putFloatLn", [ParamDecl("f", FloatType())], VoidType(), Block([])),
            
            FuncDecl("getBool", [], BoolType(), Block([])),
            FuncDecl("putBool", [ParamDecl("b", BoolType())], VoidType(), Block([])),
            FuncDecl("putBoolLn", [ParamDecl("b", BoolType())], VoidType(), Block([])),   

            FuncDecl("getString", [], StringType(), Block([])),
            FuncDecl("putString", [ParamDecl("s", StringType())], VoidType(), Block([])),
            FuncDecl("putStringLn", [ParamDecl("s", StringType())], VoidType(), Block([])),
            
            FuncDecl("putLn", [], VoidType(), Block([]))
        ]
        self.struct_current: StructType = None
        self.check_struct_interface_type: bool = False
        self.global_environment = [
            [
                Symbol("getInt",MType([],IntType())),
                Symbol("putIntLn",MType([IntType()],VoidType())),
                Symbol("putInt",MType([IntType()],VoidType())),
                
                Symbol("getFloat",MType([], FloatType())),
                Symbol("putFloat",MType([FloatType()], VoidType())),
                Symbol("putFloatLn",MType([FloatType()],VoidType())),
                
                Symbol("getBool",MType([BoolType()],BoolType())),
                Symbol("putBool",MType([BoolType()], VoidType())),
                Symbol("putBoolLn",MType([BoolType()],VoidType())),
                
                Symbol("getString",MType([],StringType())),
                Symbol("putString",MType([StringType()],VoidType())),
                Symbol("putStringLn",MType([StringType()],VoidType())),
                
                Symbol("putLn",MType([],VoidType()))
            ]
        ]
 
    
    def check(self):
        return self.visit(self.ast,self.global_environment)

    def evaluate_value(self, ast, c):
        if type(ast) == IntLiteral:
            return int(ast.value)
        elif type(ast) == BinaryOp:
            if ast.op == "+":
                return int(self.evaluate_value(ast.left, c) + self.evaluate_value(ast.right, c))
            if ast.op == "-":
                return int(self.evaluate_value(ast.left, c) - self.evaluate_value(ast.right, c))
            if ast.op == "*":
                return int(self.evaluate_value(ast.left, c) * self.evaluate_value(ast.right, c))
            if ast.op == "/":
                return int(self.evaluate_value(ast.left, c) / self.evaluate_value(ast.right, c))
            if ast.op == "%":
                return int(self.evaluate_value(ast.left, c) % self.evaluate_value(ast.right, c))
            
        elif type(ast) == Id:
            res = self.lookup(ast.name, reduce(lambda acc, ele: acc + ele, c, []), lambda x: x.name if isinstance(x, Symbol) else None) # return the Symbol type => get the symbol.value

            if res is None:
                raise Undeclared(Identifier(), ast.name)

            return self.evaluate_value(res.value, c)
        elif type(ast) == UnaryOp:
            if ast.op == "-":
                return -int(self.evaluate_value(ast.body, c))
        return 0

    def checkASTType(self, lhs_type: Type, rhs_type: Type, list_type_permission: List[Tuple[Type, Type]] = []):
        if type(rhs_type) == StructType and rhs_type.name == "":
            lhs = self.lookup(lhs_type.name, self.list_type, lambda x: x.name) if type(lhs_type) == Id else lhs_type
            return type(lhs) in [StructType,  InterfaceType] # ??? var e int = nil?
        
        lhs_type = self.lookup(lhs_type.name, self.list_type, lambda x: x.name) if type(lhs_type) == Id else lhs_type
        rhs_type = self.lookup(rhs_type.name, self.list_type, lambda x: x.name) if type(rhs_type) == Id else rhs_type

        if (type(lhs_type), type(rhs_type)) in list_type_permission:
            if isinstance(lhs_type, InterfaceType) and isinstance(rhs_type, StructType):
                for i in lhs_type.methods: 
                    method_in_struct = self.lookup(i.name, rhs_type.methods, lambda x: x.fun.name)
                    if method_in_struct is None: # check name
                        return False
                    if type(i.retType) == type(method_in_struct.fun.retType) and type(i.retType) == Id: # check return type
                        if i.retType.name != method_in_struct.fun.retType.name:
                            return False
                    elif type(i.retType) != type(method_in_struct.fun.retType): 
                        return False
                    if len(i.params) == len(method_in_struct.fun.params): # check params
                        for param_interface, param_struct in zip(i.params, method_in_struct.fun.params):
                            if type(param_interface) != type(param_struct.parType):
                                return False
                    else: return False
                return True 
            return True

        if type(lhs_type) == type(rhs_type) and type(lhs_type) in [StructType, InterfaceType]:
            return lhs_type.name == rhs_type.name

        if type(lhs_type) == ArrayType and type(rhs_type) == ArrayType:
            lhs_eleType = self.lookup(lhs_type.eleType.name, self.list_type, lambda x: x.name) if type(lhs_type.eleType) == Id else lhs_type.eleType

            rhs_eleType = self.lookup(rhs_type.eleType.name, self.list_type, lambda x: x.name) if type(rhs_type.eleType) == Id else rhs_type.eleType

            if (type(lhs_eleType), type(rhs_eleType)) in list_type_permission or type(lhs_eleType) == type(rhs_eleType):
                if len(lhs_type.dimens) == len(rhs_type.dimens):
                    for idx1, idx2 in zip(lhs_type.dimens, rhs_type.dimens):
                        if idx1.value != idx2.value:
                            return False
                elif len(lhs_type.dimens) != len(rhs_type.dimens):
                    return False
                return True
            return False
        
        return type(lhs_type) == type(rhs_type)


    def visitProgram(self, ast: Program, c: List[List[Symbol]]):         
        def checkMethodDecllist(ast: MethodDecl, c: List[MethodDecl]):
            res = self.lookup((ast.fun.name, ast.recType.name), c, lambda x: (x.fun.name, x.recType.name)) #check both method name and return Type of the receiver
            if (not res is None):
                raise Redeclared(Method(), ast.fun.name)

            struct_current = self.lookup(ast.recType.name, self.list_type, lambda x: x.name if type(x) == StructType else None)

            # check whether the method name is the same as the elements in struct
            res = self.lookup(ast.fun.name, struct_current.elements, lambda x: x[0])
            if not res is None:
                raise Redeclared(Method(), ast.fun.name)

            if not struct_current is None:
                struct_current.methods.append(ast)
            return ast

        def checkRedeclaredName(ast, list_str):
            if type(ast) == VarDecl:
                if ast.varName in list_str:
                    raise Redeclared(Variable(), ast.varName)
                else: return [ast.varName] + list_str
            if type(ast) == ConstDecl: 
                if ast.conName in list_str:
                    raise Redeclared(Constant(), ast.conName)
                return [ast.conName] + list_str
            if ast.name in list_str:
                if type(ast) == StructType or type(ast) == InterfaceType:
                    raise Redeclared(Type(), ast.name)
                if isinstance(ast, FuncDecl):
                    raise Redeclared(Function(), ast.name)
            return [ast.name] + list_str
            
        # check redeclared name at global scope        
        reduce(lambda acc, ele: checkRedeclaredName(ele, acc) if not type(ele) == MethodDecl else acc, ast.decl, ["getInt","putIntLn", "putInt", "getFloat", "putFloat", "putFloatLn", "getBool", "putBool", "putBoolLn",  "getString", "putString", "putStringLn","putLn"])

        # Check available StructType and InterfaceType
        reduce(lambda acc, ele: [self.visit(ele, acc)] + acc if type(ele) == StructType or type(ele) == InterfaceType else acc, ast.decl, [])

        # add available function into list_function 
        self.list_function = self.list_function + list(filter(lambda item: type(item) == FuncDecl, ast.decl))

        # Check Method Declaration
        reduce(lambda acc, ele: [checkMethodDecllist(ele, acc)] + acc if type(ele) == MethodDecl else acc, ast.decl, [])

        self.check_struct_interface_type = True # already checked the StructType and the InterfaceType

        def visitEachDecl(ele, acc):
            self.function_current = None
            return self.visit(ele, acc)

        # check global scope: var decl, const decl, struct decl, interface decl 
        # not sure if the global scope is the same as the global environment (built-in functions)
        reduce(lambda acc,ele: [[visitEachDecl(ele,acc)] + acc[0]] + acc[1:], ast.decl, c)
    
    def visitParamDecl(self, ast, c):
        #handle BinaryOp in arraytype
        ast.parType = self.visit(ast.parType,c) if type(ast.parType) == ArrayType else ast.parType
        if len(c) == 0:
            return Symbol(ast.parName, ast.parType, None)
        res = self.lookup(ast.parName, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        if c[0] is None:
            return None
        return Symbol(ast.parName, ast.parType, None)

    def visitVarDecl(self, ast: VarDecl, c : List[List[Symbol]]):
        result = self.lookup(ast.varName, c[0], lambda x: x.name if type(x) == Symbol else None)
        if not result is None:
            raise Redeclared(Variable(), ast.varName) 
        
        lhs_type = self.visit(ast.varType,c) if ast.varType and type(ast.varType) == ArrayType else (ast.varType if ast.varType else None) 
        rhs_type = self.visit(ast.varInit, c) if ast.varInit else None

        varValue = IntLiteral(self.evaluate_value(ast.varInit, c)) if ast.varInit and type(ast.varInit) in [BinaryOp, UnaryOp, IntLiteral] else None

        if rhs_type is None:
            return Symbol(ast.varName, lhs_type, None)
        if lhs_type is None:
            return Symbol(ast.varName, rhs_type, varValue)
        if self.checkASTType(lhs_type, rhs_type, [(FloatType, IntType)] if (type(lhs_type) == ArrayType and type(rhs_type) == ArrayType) else [(FloatType, IntType), (InterfaceType, StructType)]):
            return Symbol(ast.varName, lhs_type, varValue)
        raise TypeMismatch(ast)

    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]):
        result = self.lookup(ast.conName, c[0], lambda x: x.name if type(x) == Symbol else None)
        if not result is None:
            raise Redeclared(Constant(), ast.conName)
        rhs_type = self.visit(ast.iniExpr,c) if ast.iniExpr else None

        constValue = IntLiteral(self.evaluate_value(ast.iniExpr, c)) if ast.iniExpr and type(ast.iniExpr) in [BinaryOp, UnaryOp, IntLiteral] else None

        return Symbol(ast.conName, rhs_type, constValue)
   
    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]):
        self.function_current = ast
        param_scope = reduce(lambda acc, ele: [self.visit(ele,acc)] + acc, self.function_current.params, [])
        
        self.visit(self.function_current.body, [param_scope] + c)

        return Symbol(ast.name, MType([x.parType for x in ast.params], ast.retType), None)

    def visitStructType(self, ast: StructType, c):
        def visitElementsInStruct(ele, c):
            result = self.lookup(ele[0], c, lambda x: x[0])
            if not result is None:
                raise Redeclared(Field(), ele[0])
            return [ele]
        
        if not self.check_struct_interface_type:
            self.list_type.append(ast)
            
        reduce(lambda acc, ele: visitElementsInStruct(ele, acc) + acc, ast.elements, [])

        return ast
    
    def visitInterfaceType(self, ast: InterfaceType, c):
        if not self.check_struct_interface_type:
            self.list_type.append(ast)

        reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
            
        return ast

    def visitMethodDecl(self, ast: MethodDecl, c):
        # TODO check the body of the method
        self.function_current = ast.fun
        param_scope = reduce(lambda acc, ele: [self.visit(ele,acc)] + acc, self.function_current.params, []) # check redeclared parameters => change into Symbol Type
        # param_scope = [Symbol(ast.receiver, ast.recType, None)] + param_scope
        #reduce(lambda acc, ele: visitParameterInMethod(ele, acc) + acc, param_scope, []) # check redeclared parameters, included the receiver of the method

        self.visit(self.function_current.body,  [[param_scope, Symbol(ast.receiver, ast.recType, None)]] + c) #??? [param_scope, Symbol(ast.receiver, ast.recType, None)] => List[List[Symbol],Symbol]
        # return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        
        # Handle binaryop in arraytype in prototype in methods
        ast.params = list(map(lambda item: self.visit(item, c) if type(item) == ArrayType else item, ast.params))
        ast.retType = self.visit(ast.retType, c) if type(ast.retType) == ArrayType else ast.retType

        return ast

    
    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]): 
        condition_type = self.visit(ast.cond, c)
        if type(condition_type) != BoolType:
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]): 
        # self.forType = True
        init = self.visit(ast.init, [[]] + c)
        condition_type = self.visit(ast.cond, [[init]] + c)
        if type(condition_type) != BoolType: # not sure for the symbol here
            raise TypeMismatch(ast)
        self.visit(Block([ast.init] + [ast.upda] + ast.loop.member), c)
    
    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]): 
        type_array = self.visit(ast.arr, c)
        if type(type_array) != ArrayType:
            raise TypeMismatch(ast)
    
        type_index = self.visit(ast.idx, c)
        type_value = self.visit(ast.value, c)

        if type(type_index) != IntType:
            raise TypeMismatch(ast)

        resultCheckArrayType = self.checkASTType(type_value, type_array.eleType if len(type_array.dimens) == 1 else ArrayType(type_array.dimens[1:], type_array.eleType))
        if not resultCheckArrayType:
            raise TypeMismatch(ast)        

        # self.visit(Block([VarDecl(ast.idx.name, IntType(), None), VarDecl(ast.value.name, type_array.eleType if len(type_array.dimens) == 1 else ArrayType(type_array.dimens[1:], type_array.eleType), None)] + ast.loop.member), c)
        self.visit(ast.loop, c)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]):
        def visitCall(ele, acc):
            self.visit(ele, (acc, True))
            return acc

        reduce(lambda acc, ele: visitCall(ele, acc) if type(ele) in [FuncCall, MethCall] else [[self.visit(ele, acc)] + acc[0]] + acc[1:], ast.member, [[]] + c)
        #[[self.visit(ele, acc)] + acc[0]] => 1 scope
        # [[self.visit(ele, acc)] + acc[0]] + acc[1:] => the remain scope is added to entire scope

    def visitIf(self, ast, c): 
        condition = self.visit(ast.expr,c)
        if type(condition) != BoolType:
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            self.visit(ast.elseStmt,c)
    def visitIntType(self, ast, c): 
        return ast
    def visitFloatType(self, ast, c): 
        return ast
    def visitBoolType(self, ast, c): 
        return ast
    def visitStringType(self, ast, c):
        return ast
    def visitVoidType(self, ast, c): 
        return ast
    def visitArrayType(self, ast, c):
        ast.dimens = list(map(lambda item: IntLiteral(self.evaluate_value(item, c)), ast.dimens))
        return ast
    def visitAssign(self, ast, c): 
        if type(ast.lhs) is Id:
            res = self.lookup(ast.lhs.name, reduce(lambda acc, ele: acc + ele, c), lambda x: x.name if isinstance(x, Symbol) else None)
            
            if res is None:
                # if not self.forType:
                return Symbol(ast.lhs.name, self.visit(ast.rhs, c), None)
                # else:
                    # raise Undeclared(Identifier(), ast.lhs.name)

        lhs_assign = self.visit(ast.lhs, c)
        rhs_assign = self.visit(ast.rhs, c)
        if not self.checkASTType(lhs_assign, rhs_assign, [(FloatType, IntType), (InterfaceType, StructType)]):
            raise TypeMismatch(ast)
    def visitContinue(self, ast, c): 
        return None
    def visitBreak(self, ast, c): 
        return None
    def visitReturn(self, ast, c):
        # handle the binaryop in arraytype of the function retType
        self.function_current.retType = self.visit(self.function_current.retType, c) if type(self.function_current.retType) == ArrayType else self.function_current.retType

        if not self.checkASTType(self.function_current.retType, self.visit(ast.expr,c) if ast.expr else VoidType()):
            raise TypeMismatch(ast)
        return None
    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        LHS_BINOP = self.visit(ast.left, c)
        RHS_BINOP = self.visit(ast.right, c)

        op = ast.op
        if op == "+":
            if self.checkASTType(LHS_BINOP, RHS_BINOP, [(IntType, FloatType), (FloatType, IntType)]):
                if type(LHS_BINOP) == StringType:
                    return StringType()
                elif type(LHS_BINOP) == FloatType:
                    return FloatType()
                elif type(RHS_BINOP) == FloatType:
                    return FloatType()
                elif type(LHS_BINOP) == IntType:
                    return IntType()

        elif op in ["-", "*", "/"]:
            if self.checkASTType(LHS_BINOP, RHS_BINOP, [(IntType, FloatType), (FloatType, IntType)]):
                if type(LHS_BINOP) == FloatType:
                    return FloatType()
                elif type(RHS_BINOP) == FloatType:
                    return FloatType()
                elif type(LHS_BINOP) == IntType:
                    return IntType()
        elif op == "%":
            if type(LHS_BINOP) == type(RHS_BINOP) and type(LHS_BINOP) == IntType:
                return IntType()
        elif op in ["&&", "||"]:
            if type(LHS_BINOP) == type(RHS_BINOP) and type(LHS_BINOP) == BoolType:
                return BoolType()
        elif op in ["<", "<=", ">", ">=", "==", "!="]: # check again if 2 types can be different: int and float, float and int, string and float,... (e.g., 1 > 2.0)
            if self.checkASTType(LHS_BINOP, RHS_BINOP):
                return BoolType()
        raise TypeMismatch(ast)
    def visitUnaryOp(self, ast, c):
        UNARYOP = self.visit(ast.body,c)
        if (ast.op == "!" and type(UNARYOP) != BoolType) or (ast.op == "-" and type(UNARYOP) == BoolType):
            raise TypeMismatch(ast)
        return UNARYOP

    def visitFuncCall(self, ast, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]):
        # 2 cases, example:
        # funcall() -> stmt
        # func foo() {
        #   funcall() -> stmt
        #   var a = funcall() -> expr
        # }
        stmt = False 
        if isinstance(c, tuple):
            stmt = c[1]
            c = c[0]

        result = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        result2 = self.lookup(ast.funName, c[0] if not self.function_current else c[0] + c[1], lambda x: x.name if isinstance(x, Symbol) else None)
        if result is None:
            raise Undeclared(Function(), ast.funName)
        if not result2 is None and type(result2.mtype) != MType: # Shadowing function
            raise Undeclared(Function(), ast.funName)
        if len(result.params) != len(ast.args):
            raise TypeMismatch(ast)
        for param, arg in zip(result.params, ast.args):
            if not self.checkASTType(param.parType, self.visit(arg,c)): # check parameter (1) in the using function and the parameter (2) passed into the using function (make (2) visit the Id to check the previous declaration)
                raise TypeMismatch(ast)
        if stmt and type(result.retType) != VoidType:
            raise TypeMismatch(ast)
        if not stmt and type(result.retType) == VoidType:
            raise TypeMismatch(ast)
        return result.retType
    def visitMethCall(self, ast: MethCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]):
    # TODO Undeclared Method
        stmt = False
        if isinstance(c, tuple):
            stmt = c[1]
            c = c[0]

        receiver = self.visit(ast.receiver, c)
        if type(receiver) == Id:
            receiver = self.lookup(receiver.name, self.list_type, lambda x: x.name)

        if not type(receiver) in [StructType, InterfaceType]: #check if not InterfaceType
            raise TypeMismatch(ast)
        

        result = self.lookup(ast.metName, receiver.methods, lambda x: x.fun.name if type(receiver) == StructType else (x.name if type(receiver) == InterfaceType else None))
        if result is None:
            raise Undeclared(Method(), ast.metName)
        
        if type(receiver) == StructType:
            if len(result.fun.params) != len(ast.args):
                raise TypeMismatch(ast)
            for param, arg in zip(result.fun.params, ast.args):
                if not self.checkASTType(param.parType, self.visit(arg,c)):
                    raise TypeMismatch(ast)
            if (stmt and type(result.fun.retType) != VoidType) or (not stmt and type(result.fun.retType) == VoidType):
                raise TypeMismatch(ast)
        elif type(receiver) == InterfaceType:
            if len(result.params) != len(ast.args):
                raise TypeMismatch(ast)
            for param, arg in zip(result.params, ast.args):
                if not self.checkASTType(param, self.visit(arg,c)):
                    raise TypeMismatch(ast)
            if (stmt and type(result.retType) != VoidType) or (not stmt and type(result.retType) == VoidType):
                raise TypeMismatch(ast)
        
        return result.fun.retType if type(receiver) == StructType else result.retType


    def visitId(self, ast, c: List[List[Symbol]]):
        result = self.lookup(ast.name, reduce(lambda acc, ele: acc + ele[0] + ele[1:] if len(ele) == 2 and type(ele[0]) == list and type(ele[1]) == Symbol else acc + ele, c, []), lambda x: x.name if isinstance(x, Symbol) else None) # should flatten nested list c???
        # "acc + ele[0] + ele[1:] if len(ele) > 1 and type(ele[0]) == list and type(ele[1]) == Symbol" => only for the method parameter scope List[List[Symbol],Symbol]

        if result is None:
            raise Undeclared(Identifier(), ast.name)
        if not isinstance(result.mtype, Id):
            return result.mtype
        return self.lookup(result.mtype.name, self.list_type, lambda x: x.name) # look for and return structtype/interfacetype

    def visitArrayCell(self, ast, c): 
        array_type = self.visit(ast.arr,c)
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)
       
        if not all(map(lambda item: self.checkASTType(self.visit(item, c), IntType()), ast.idx)):
            raise TypeMismatch(ast)
        if len(array_type.dimens) == len(ast.idx):
            return array_type.eleType # not sure
        elif len(array_type.dimens) > len(ast.idx):
            len_type = len(ast.idx) # used to return the type based on array cell and the previous array type declared
            return self.visit(ArrayType(array_type.dimens[len_type:], array_type.eleType),c)
        raise TypeMismatch(ast) 
    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
    # TODO Undeclared Field
        # struct = self.visit(ast.receiver, c[1:])
        receiver = self.visit(ast.receiver, c)
        if type(receiver) == Id:
            receiver = self.lookup(receiver.name, self.list_type, lambda x: x.name)

        if type(receiver) != StructType:
            raise TypeMismatch(ast)

        result_field = self.lookup(ast.field, receiver.elements, lambda x: x[0])
        if result_field is None:
            raise Undeclared(Field(), ast.field)
        return result_field[1] #return field type
    
    def visitIntLiteral(self, ast, c): 
        return IntType()
    def visitFloatLiteral(self, ast, c): 
        return FloatType()
    def visitBooleanLiteral(self, ast, c): 
        return BoolType()
    def visitStringLiteral(self, ast, c): 
        return StringType()
    def visitArrayLiteral(self, ast, c: List[List[Symbol]]):  
        def nested2string(element: Union[Literal, list['NestedList']], c: List[List[Symbol]]):
            if isinstance(element,list):
                list(map(lambda value: nested2string(value, c), element))
            else:
                self.visit(element, c)
        nested2string(ast.value, c)
        return self.visit(ArrayType(ast.dimens, ast.eleType),c)
    def visitStructLiteral(self, ast: StructLiteral, c): 
        list(map(lambda ele: self.visit(ele[1], c), ast.elements))
        result_structtype = self.lookup(ast.name, self.list_type, lambda x: x.name)
        return result_structtype
    def visitNilLiteral(self, ast: NilLiteral, c): 
        nil = StructType("", [], [])
        return nil