from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *
from typing import Tuple, List


class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType:
    def __init__(self, name):
        #value: Id
        self.name = name

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.list_type = dict()
        self.struct: StructType = None
        self.initVarDecl = False

    def init(self):
        mem = [
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),

            # Boolean related functions
            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            
            # String related functions
            Symbol("getString", MType([], StringType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            
            # Newline function
            Symbol("putLn", MType([], VoidType()), CName("io", True))
        ]

        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", Id(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  


    def emitObjectCInit(self, ast: Program, env):
        frame = Frame("<cinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) 
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame
        def create_id(item):
            return Id(item.varName) if type(item) is VarDecl else Id(item.conName)
            
        def get_init_expr(item):
            return item.varInit if type(item) is VarDecl else item.iniExpr
            
        def is_initialized_decl(item):
            return (type(item) is VarDecl and item.varInit) or (type(item) is ConstDecl)
            
        assignments = [Assign(create_id(item), get_init_expr(item)) 
                      for item in ast.decl if is_initialized_decl(item)]
        self.visit(Block(assignments), env)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    ## Helper functions ------------------------------

    def init_primitive(self, varType: Type) -> tuple[Literal, Type]:
        """Initialize primitive type variables with default values"""
        if type(varType) is IntType:
            return IntLiteral(0)
        elif type(varType) is FloatType:
            return FloatLiteral(0.0)
        elif type(varType) is StringType:
            return StringLiteral("\"\"")
        elif type(varType) is BoolType:
            return BooleanLiteral("false")
        elif type(varType) is Id:
            return StructLiteral(varType.name, [])
        return None
            
    def init_array(self, varType: ArrayType, o: dict):
        """Initialize array type variables recursively"""
        
        if next(filter(lambda x: type(x) in [Id, ArrayCell], varType.dimens), None):
            return ArrayType(varType.dimens, varType.eleType)
        if len(varType.dimens) == 1:
            return [self.init_primitive(varType.eleType) for _ in range(int(varType.dimens[0].value))]
        return [self.var_init(ArrayType(varType.dimens[1:], varType.eleType), o) for _ in range(int(varType.dimens[0].value))]
        
    def var_init(self, varType: Type, o: dict):
        """Initialize variables with their default values based on type"""
        if isinstance(varType, ArrayType):
            return self.init_array(varType, o)
        return self.init_primitive(varType)
    
    def checkType(self, LHS_type: Type, RHS_type: Type, list_type_permission: List[Tuple[Type, Type]] = []) -> bool:
        if type(RHS_type) == StructType and RHS_type.name == "":
            lhs = self.lookup(LHS_type.name, self.list_type.values(), lambda x: x.name) if type(LHS_type) == Id else LHS_type
            return type(lhs) in [StructType,  InterfaceType]

        LHS_type = self.lookup(LHS_type.name, self.list_type.values(), lambda x: x.name) if isinstance(LHS_type, Id) else LHS_type
        RHS_type = self.lookup(RHS_type.name, self.list_type.values(), lambda x: x.name) if isinstance(RHS_type, Id) else RHS_type

        if (type(LHS_type), type(RHS_type)) in list_type_permission:
            if isinstance(LHS_type, InterfaceType) and isinstance(RHS_type, StructType):
                return all(
                    any(
                        struct_methods.fun.name == inteface_method.name and
                        self.checkType(struct_methods.fun.retType, inteface_method.retType) and
                        len(struct_methods.fun.params) == len(inteface_method.params) and
                        reduce(
                            lambda x, i: x and self.checkType(struct_methods.fun.params[i].parType, inteface_method.params[i]),
                            range(len(struct_methods.fun.params)),
                            True
                        )
                        for struct_methods in RHS_type.methods
                    )
                    for inteface_method in LHS_type.methods
                )
            if type(LHS_type) == type(RHS_type) and type(LHS_type) in [StructType, InterfaceType]:
                return LHS_type.name == RHS_type.name

        if isinstance(LHS_type, ArrayType) and isinstance(RHS_type, ArrayType):
            lhs_eleType = self.lookup(LHS_type.eleType.name, self.list_type, lambda x: x.name) if type(LHS_type.eleType) == Id else LHS_type.eleType

            rhs_eleType = self.lookup(RHS_type.eleType.name, self.list_type, lambda x: x.name) if type(RHS_type.eleType) == Id else RHS_type.eleType

            return (type(lhs_eleType) == type(rhs_eleType)
                    and all(
                        l.value == r.value  for l, r in zip(LHS_type.dimens, RHS_type.dimens)
                    )
                    and self.checkType(lhs_eleType, rhs_eleType, [list_type_permission[0]] if len(list_type_permission) != 0 else [])) 

        return type(LHS_type) == type(RHS_type)

    ## Main function to generate code for the program

    def visitProgram(self, ast: Program, c):
        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        self.list_type = { x.name: x for x in ast.decl if isinstance(x, StructType) or isinstance(x, InterfaceType) }
        for item in ast.decl:
            if type(item) is MethodDecl:
                self.struct = self.lookup(item.recType.name, self.list_type.values(), lambda x: x.name if type(x) == StructType else None)

                # should I handle methods when no found struct available?

                if self.struct:
                    self.struct.methods.append(item)

        env ={}
        env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, VarDecl) or isinstance(x, ConstDecl) else a, ast.decl, env)

        # reduce(lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a, ast.decl, env)

        g = env['env'][0]
        env['env'] = [[]]
        for decl in ast.decl:
            if isinstance(decl, VarDecl):
                res = self.lookup(decl.varName, g, lambda x: x.name)
                if res:
                    env['env'][0].append(res)
            if isinstance(decl, ConstDecl):
                res = self.lookup(decl.conName, g, lambda x: x.name)
                if res:
                    env['env'][0].append(res)
            if isinstance(decl, FuncDecl):
                self.visit(decl, env)

        self.emitObjectInit()
        self.emitObjectCInit(ast, env)
        self.emit.printout(self.emit.emitEPILOG())

        for item in self.list_type.values():
            self.struct = item
            self.emit = Emitter(self.path + "/" + item.name + ".j")
            self.visit(item, {'env': env['env']})

        return env

    def visitFuncDecl(self, ast, o: dict) -> dict:
        self.function = ast
        frame = Frame(ast.name, ast.retType) # initialize frame
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
    def visitStructType(self, ast: StructType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))

        for item in self.list_type.values():
            if type(item) == InterfaceType and self.checkType(item, ast, [(InterfaceType, StructType)]): #???
                self.emit.printout(self.emit.emitIMPLEMENTS(item.name))

        for item in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(f"public {item[0]}", item[1], False, False, False))
        self.visit(MethodDecl(None, None, FuncDecl("<init>", [ParamDecl(item[0], item[1]) for item in ast.elements], VoidType(), Block([Assign(FieldAccess(Id("this"), item[0]), Id(item[0])) for item in ast.elements]))), o) #???
        
        self.visit(MethodDecl(None, None, FuncDecl("<init>", [], VoidType(), Block([]))), o) #???

        for item in ast.methods: self.visit(item, o)
        self.emit.printout(self.emit.emitEPILOG())

    def visitInterfaceType(self, ast: InterfaceType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object", True))
        for item in ast.methods:
            codeGen = ""
            codeGen += self.emit.emitABSTRACTMETHOD(item.name, MType(item.params, item.retType), False)
            codeGen += self.emit.emitENDABSTRACTMETHOD()
            self.emit.printout(codeGen)
        self.emit.printout(self.emit.emitEPILOG())

    def visitMethodDecl(self, ast: MethodDecl, o):
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = MType(list(map(lambda x: x.parType, ast.fun.params)), ast.fun.retType)
        
        env = o.copy()
        env['frame'] = frame

        index = 0
        for item in self.astTree.decl:
            if type(item) in [VarDecl, ConstDecl]:
                index += 1
            if item == ast:
                break
        env_g = env['env'][0][:index]

        env['env'] = [[]] + [env_g]

        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype,False, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(self.struct.name), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR("this", Id(self.struct.name), 0, frame))  
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
        else:
            env['env'] = [[Symbol(ast.receiver, ast.recType, Index(0))]] + env['env'] #???

        env['env'] = [[]] + env['env']
        env = reduce(lambda acc,e: self.visit(e,acc),ast.fun.params,env) 
        self.visit(ast.fun.body, env) 


        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitFieldAccess(self, ast:FieldAccess, o: dict) -> tuple[str, Type]:
        code, typ = self.visit(ast.receiver, o) 
        typ = self.list_type[typ.name]
        field = next(filter(lambda x: x[0] == ast.field, typ.elements), None) 
        return code + self.emit.emitGETFIELD(typ.name + "/" + ast.field, field[1], o["frame"]), field[1]
    
    def visitMethCall(self, ast: MethCall, o: dict) -> tuple[str, Type]:
        code, typ = self.visit(ast.receiver, o)

        if isinstance(typ, Id):
            typ = self.list_type.get(typ.name)

        is_stmt = o.pop("stmt", False)

        for arg in ast.args:
            arg_code, _ = self.visit(arg, o)
            code += arg_code

        returnType = None
        if isinstance(typ, StructType):
            method = next(filter(lambda x: x.fun.name == ast.metName, typ.methods), None)
            
            mtype = MType([x.parType for x in method.fun.params], method.fun.retType)
            returnType = method.fun.retType
            code += self.emit.emitINVOKEVIRTUAL(typ.name + "/" + method.fun.name, mtype, o['frame'])
            
                
        elif isinstance(typ, InterfaceType):
            method = next(filter(lambda x: x.name == ast.metName, typ.methods), None) 
            mtype = MType(method.params, method.retType)
            returnType = method.retType
            code += self.emit.emitINVOKEINTERFACE(f"{typ.name}/{method.name}", mtype, o['frame'])
        
        if is_stmt:
            self.emit.printout(code)
            return o

        return code, returnType
    
    def visitStructLiteral(self, ast: StructLiteral, o: dict) -> tuple[str, Type]:
        
        code = self.emit.emitNEW(ast.name, o['frame'])
        code += self.emit.emitDUP(o['frame'])
        list_type = []
        for item in ast.elements:
            c, t = self.visit(item[1], o)
            code += c
            list_type += [t]
        code += self.emit.emitINVOKESPECIAL(o['frame'], ast.name + "/<init>", MType(list_type,VoidType()) if len(ast.elements) else MType([], VoidType()))
        return code, Id(ast.name)

    def visitNilLiteral(self, ast: NilLiteral, o: dict) -> tuple[str, Type]:
        code = self.emit.emitPUSHNULL(o['frame'])
       
        return code, Id("")
    
    def visitParamDecl(self, ast: ParamDecl, o: dict) -> dict:
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel() ,frame.getEndLabel(), frame))     
        return o
    
    def visitVarDecl(self, ast: VarDecl, o: dict) -> dict:
        varInit = ast.varInit
        varType = ast.varType
        if not varInit:
            varInit = self.var_init(varType, o)
            if type(varType) == ArrayType:
                varInit = ArrayLiteral(varType.dimens, varType.eleType, varInit)
            ast.varInit = varInit
            self.initVarDecl = False
        else:
            self.initVarDecl = True

        env = o.copy()
        env['frame'] = Frame("<template>", VoidType()) 
        rhsCode, rhsType = self.visit(varInit, env)
        if not varType:
            varType = rhsType

        if 'frame' not in o: 
            o['env'][0].append(Symbol(ast.varName, varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, varType, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            
            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                rhsCode = rhsCode + self.emit.emitI2F(frame)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index, frame))                    
        return o
    
    def visitFuncCall(self, ast: FuncCall, o: dict) -> dict:
        sym = next(filter(lambda x: x.name == ast.funName, self.list_function),None)
        env = o.copy()
        if o.get('stmt'):
            o["stmt"] = False
            [self.emit.printout(self.visit(x, o)[0]) if type(x) is not FuncCall else self.visit(x, env) for x in ast.args]
            output = self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
            return o
        output = "".join([str(self.visit(x, env)[0]) for x in ast.args])
        output += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame'])
        return output, sym.mtype.rettype

    def visitBlock(self, ast: Block, o: dict) -> dict:
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env["frame"].getStartLabel(), env["frame"]))

        for item in ast.member:
            if type(item) in [FuncCall, MethCall]:
                env["stmt"] = True
            env = self.visit(item, env)

        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitId(self, ast: Id, o: dict) -> dict:
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        if o.get('isLeft'):
            if type(sym.value) is Index:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:         
                return self.emit.emitPUTSTATIC(sym.value.value + '/' + sym.name, sym.mtype, o['frame']),sym.mtype        
        if type(sym.value) is Index:
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o['frame']),sym.mtype
        else:         
            return self.emit.emitGETSTATIC(sym.value.value + '/' + sym.name, sym.mtype, o['frame']), sym.mtype

    def visitAssign(self, ast: Assign, o: dict) -> dict:
        if type(ast.lhs) is Id and not next(filter(lambda x: ast.lhs.name == x.name, [j for i in o['env'] for j in i]),None):
            self.visit(VarDecl(ast.lhs.name, None, ast.rhs), o)

        if type(ast.lhs) is FieldAccess:
            if self.struct:
                res = self.lookup(ast.lhs.field, self.struct.elements, lambda x: x[0])
                
                codeGen = self.emit.emitREADVAR("this", res[1], 0, o['frame'])
                codeGen += self.visit(ast.rhs, o)[0]

                codeGen += self.emit.emitPUTFIELD(self.struct.name + "/" + ast.lhs.field, res[1], o['frame'])
                self.emit.printout(codeGen)
            else:
                lhsCode, lhsType = self.visit(ast.lhs.receiver, o)
                rhsCode, rhsType = self.visit(ast.rhs, o)
                typ = self.list_type[lhsType.name]
                field = next(filter(lambda x: x[0] == ast.lhs.field, typ.elements), None)
                codeGen = lhsCode + rhsCode + self.emit.emitPUTFIELD(f"{lhsType.name}/{field[0]}", field[1], o['frame'])
                self.emit.printout(codeGen)
        elif type(ast.lhs) is ArrayCell:
            o['frame'].push() 
            rhsCode, rhsType = self.visit(ast.rhs, o)
            o['isLeft'] = True
            lhsCode, lhsType = self.visit(ast.lhs, o)
            o['isLeft'] = False
            codeGen = lhsCode + rhsCode
            if (type(lhsType) is FloatType and type(rhsType) is IntType) or (type(lhsType) is IntType and type(rhsType) is FloatType):
                codeGen += self.emit.emitI2F(o['frame']) 
            self.emit.printout(codeGen + self.emit.emitASTORE(self.arrayCell, o['frame']))
            if type(ast.rhs) is StructLiteral:
                rhsCode, rhsType = self.visit(ast.rhs, o)
                o['isLeft'] = True
                lhsCode, lhsType = self.visit(ast.lhs, o)
                o['isLeft'] = False
                self.emit.printout(rhsCode + lhsCode)
        else:
            o['frame'].push() 
            rhsCode, rhsType = self.visit(ast.rhs, o)
            o['isLeft'] = True
            lhsCode, lhsType = self.visit(ast.lhs, o)
            o['isLeft'] = False
            if type(lhsType) is FloatType and type(rhsType) is IntType:
                rhsCode = rhsCode + self.emit.emitI2F(o['frame'])
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)
        return o

    def visitReturn(self, ast: Return, o: dict) -> dict:
        if ast.expr:
            self.emit.printout(self.visit(ast.expr, o)[0])
        self.emit.printout(self.emit.emitRETURN(self.visit(ast.expr, o)[1] if ast.expr else VoidType(), o['frame']))
        return o

    def visitBinaryOp(self, ast: BinaryOp, o: dict) -> tuple[str, Type]:
        op = ast.op
        frame = o['frame']
        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o)
        if op in ['+', '-'] and type(typeLeft) in [FloatType, IntType]:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitADDOP(op, typeReturn, frame), typeReturn
        if op in ['*', '/']:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitMULOP(op, typeReturn, frame), typeReturn
        if op in ['%']:
            return codeLeft + codeRight + self.emit.emitMOD(frame), IntType()
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [FloatType, IntType]:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitREOP(op, typeReturn, frame), BoolType()
        if op in ['||']:
            ## short circuit
            codeGen = codeLeft
            
            label_exit = frame.getNewLabel()
            label_end_if = frame.getNewLabel()

            codeGen += self.emit.emitDUP(frame)

            codeGen += self.emit.emitIFFALSE(label_end_if, frame)

            codeGen += self.visit(BooleanLiteral(True), o)[0]

            codeGen += self.emit.emitGOTO(label_exit, frame)
            codeGen += self.emit.emitLABEL(label_end_if, frame)

            codeGen += codeRight

            codeGen += self.emit.emitLABEL(label_exit, frame)

            return codeGen + self.emit.emitOROP(frame), BoolType()
        if op in ['&&']:
            ## short circuit
            codeGen = codeLeft

            label_exit = frame.getNewLabel()
            label_end_if = frame.getNewLabel()

            codeGen += self.emit.emitDUP(frame)

            codeGen += self.emit.emitIFTRUE(label_end_if, frame)

            codeGen += self.visit(BooleanLiteral(False), o)[0]

            codeGen += self.emit.emitGOTO(label_exit, frame)
            codeGen += self.emit.emitLABEL(label_end_if, frame)

            codeGen += codeRight
            
            codeGen += self.emit.emitLABEL(label_exit, frame)

            return codeGen + self.emit.emitANDOP(frame), BoolType()  

        if op in ['+'] and type(typeLeft) in [StringType]:
            codeOp = self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), frame)
            return codeLeft + codeRight + codeOp, StringType()    
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [StringType]:
            codeOp = self.emit.emitINVOKEVIRTUAL("java/lang/String/compareTo", MType([StringType()], IntType()), frame) + self.emit.emitPUSHICONST(0, frame) + self.emit.emitREOP(op, IntType(), frame)
            code = codeLeft + codeRight + codeOp
            return code, BoolType()    
              
    def visitUnaryOp(self, ast: UnaryOp, o: dict) -> tuple[str, Type]:
        if ast.op == '!':
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNOT(BoolType(), o['frame']), BoolType()

        elif ast.op == '-':
            code, type_return = self.visit(ast.body, o)
            if type(type_return) in [FloatType,IntType]:
                return code + self.emit.emitNEGOP(type_return, o['frame']), type_return

    def visitIntLiteral(self, ast: IntLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST("true" if ast.value == 'true' else "false", o['frame']), BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHCONST(ast.value, StringType(),o["frame"]), StringType()
    
    def visitArrayLiteral(self, ast:ArrayLiteral , o: dict) -> tuple[str, Type]:
        def nested2recursive(element: Union[Literal, list['NestedList']], o: dict) -> tuple[str, Type]:
            if not isinstance(element,list): 
                return self.visit(element, 0)

            frame = o['frame'] 
            codeGen = self.emit.emitPUSHCONST(len(element), IntType(), frame)

            if not isinstance(element[0],list):
                _, type_element_array = self.visit(element[0], o) 
                codeGen += self.emit.emitNEWARRAY(type_element_array, frame)

                for idx, item in enumerate(element):
                    codeGen += self.emit.emitDUP(frame)  
                    codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame) 
                    codeGen += self.visit(item,o)[0]
                    codeGen += self.emit.emitASTORE(type_element_array, frame)
                return codeGen , ArrayType([len(element)], type_element_array)

            _, type_element_array = nested2recursive(element[0], o)
            codeGen += self.emit.emitANEWARRAY(type_element_array, frame)

            for idx, item in enumerate(element):
                codeGen += self.emit.emitDUP(frame)
                codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)
                codeGen += nested2recursive(item, o)[0]
                codeGen += self.emit.emitASTORE(type_element_array, frame) 
            return  codeGen, ArrayType([len(element)], type_element_array)
        
        if type(ast.value) is ArrayType:
            return self.visit(ast.value, o)
        if type(ast.eleType) is Id and self.initVarDecl == False:
            return self.visit(ArrayType(ast.dimens, ast.eleType), o)

        return nested2recursive(ast.value, o)

    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        newO = o.copy()
        newO['isLeft'] = False 
        codeGen, arrType = self.visit(ast.arr, newO) 

        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            if idx != len(ast.idx) - 1: 
                codeGen += self.emit.emitALOAD(arrType, o['frame'])

        retType = None
        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                self.arrayCell = retType
        else:
            len_type = len(ast.idx)
            retType = ArrayType(arrType.dimens[len_type:], arrType.eleType)
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                self.arrayCell = retType
        return codeGen, retType


    def visitIf(self, ast: If, o: dict) -> dict:
        frame = o['frame']
        label_exit = frame.getNewLabel()
        label_end_if = frame.getNewLabel()
        condCode, _ = self.visit(ast.expr, o)
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(label_end_if, frame))
        self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(label_exit, frame))
        self.emit.printout(self.emit.emitLABEL(label_end_if, frame))

        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)
        self.emit.printout(self.emit.emitLABEL(label_exit, frame))  
        return o
    

    def visitForBasic(self, ast: ForBasic, o: dict) -> dict:
        frame = o['frame']
        frame.enterLoop()
        lable_new = frame.getNewLabel()
        label_Break = frame.getBreakLabel() 
        label_Cont = frame.getContinueLabel()
        self.emit.printout(self.emit.emitLABEL(lable_new, frame))
        self.emit.printout(self.visit(ast.cond, o)[0])
        self.emit.printout(self.emit.emitIFFALSE(label_Break, frame))
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(label_Cont, frame))
        self.emit.printout(self.emit.emitGOTO(lable_new, frame))
        self.emit.printout(self.emit.emitLABEL(label_Break, frame))
        frame.exitLoop()
        return o
    
    def visitForStep(self, ast: ForStep, o: dict) -> dict:   
        env = o.copy()
        frame = env['frame']
        env['env'] = [[]] + env['env']
        frame.enterScope(False) # New
        frame.enterLoop()
        label_new = frame.getNewLabel()
        label_Break = frame.getBreakLabel() 
        label_Cont = frame.getContinueLabel()

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame)) 

        self.visit(ast.init, env)

        self.emit.printout(self.emit.emitLABEL(label_new, frame))
        self.emit.printout(self.visit(ast.cond, env)[0])
        self.emit.printout(self.emit.emitIFFALSE(label_Break, frame))
        self.visit(ast.loop, env)
        self.emit.printout(self.emit.emitLABEL(label_Cont, frame))

        self.visit(ast.upda, env)

        self.emit.printout(self.emit.emitGOTO(label_new, frame))
        self.emit.printout(self.emit.emitLABEL(label_Break, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitLoop()    
        frame.exitScope()
        return o

    def visitForEach(self, ast, o: dict) -> dict:
        return o

    def visitContinue(self, ast, o: dict) -> dict:
        self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(), o['frame']))
        return o

    def visitBreak(self, ast, o: dict) -> dict:
        self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(), o['frame']))
        return o

    def visitConstDecl(self, ast:ConstDecl, o: dict) -> dict:
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)
    
    def visitArrayType(self, ast:ArrayType, o):
        codeGen = ""
        codeGen += "".join([self.visit(x, o)[0] for x in ast.dimens])
        codeGen += self.emit.emitMULTIANEWARRAY(ast, o['frame'])
        return codeGen, ast
