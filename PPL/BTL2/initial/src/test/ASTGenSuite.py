import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_ast_001(self):
        """Simple program: int main() {} """
        input = """func main() {};"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_ast_002(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_ast_003(self):
        """More complex program"""
        input = """func main () {}; var x int ;"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_ast_004(self):
        input = """const a = 1;"""
        expect = str(Program([ConstDecl("a",None,IntLiteral("1"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_ast_005(self):
        input = """var a int = 1;"""
        expect = str(Program([VarDecl("a",IntType(),IntLiteral("1"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_ast_006(self):
        input = """const abc = 0b11;"""
        expect = str(Program([ConstDecl("abc",None,IntLiteral("0b11"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_ast_007(self):
        input = """var abc int = 0o70;"""
        expect = str(Program([VarDecl("abc",IntType(),IntLiteral("0o70"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_ast_008(self):
        input = """const abc = 01.e-1;"""
        expect = str(Program([ConstDecl("abc",None,FloatLiteral("01.e-1"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
   
    def test_ast_009(self):
        input = """var abc int = 01.e-1;"""
        expect = str(Program([VarDecl("abc",IntType(),FloatLiteral("01.e-1"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_ast_010(self):
        input = """const abc = 0x123abc;"""
        expect = str(Program([ConstDecl("abc",None,IntLiteral("0x123abc"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    ### 11 - 20: test declaration
    def test_ast_011(self):
        input = """var a int; var b float;"""
        expect = str(Program([VarDecl("a",IntType(),None), VarDecl("b",FloatType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_ast_012(self):
        input = """var a int; var b int = 1;"""
        expect = str(Program([VarDecl("a",IntType(),None), VarDecl("b",IntType(),IntLiteral("1"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_ast_013(self):
        input = """var a int
                   var b float = 1.5;"""
        expect = str(Program([VarDecl("a",IntType(),None), VarDecl("b",FloatType(),FloatLiteral("1.5"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_ast_014(self):
        input = """const a = 1; const b = 2;"""
        expect = str(Program([ConstDecl("a",None,IntLiteral("1")), ConstDecl("b",None,IntLiteral("2"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_ast_015(self):
        input = """const a = a[2].foo(1,2); const b = 2.5;"""
        expect = str(Program([ConstDecl("a",None,MethCall(ArrayCell(Id("a"),[IntLiteral("2")]),"foo",[IntLiteral("1"),IntLiteral("2")])), ConstDecl("b",None,FloatLiteral("2.5"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_ast_016(self):
        input = """var a = [1]int{1,2,3,4};"""
        expect = str(Program([VarDecl("a",None,ArrayLiteral([IntLiteral("1")],IntType(), [IntLiteral("1"), IntLiteral("2"), IntLiteral("3"), IntLiteral("4")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_ast_017(self):
        input = """var a = [1]float{1.,2.5,3.5,4.5};"""
        expect = str(Program([VarDecl("a",None,ArrayLiteral([IntLiteral(1)],FloatType(), [FloatLiteral("1."), FloatLiteral("2.5"), FloatLiteral("3.5"), FloatLiteral("4.5")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_ast_018(self):
        input = """var a = [1][2]int{1,2,ID{a: 1, b: true}};"""
        expect = str(Program([VarDecl("a",None,ArrayLiteral([IntLiteral(1), IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2), StructLiteral("ID",[("a", IntLiteral(1)),("b", BooleanLiteral("true"))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_ast_019(self):
        input = """const obj = ID{a: [1]int{1}};"""
        expect = str(Program([ConstDecl("obj",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral("1")],IntType(),[IntLiteral("1")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_ast_020(self):
        input = """const a = foo();"""
        expect = str(Program([ConstDecl("a",None,FuncCall("foo",[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    ### 21 - 30: test func declaration
    def test_ast_021(self):
        input = """func foo() {return;};"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_ast_022(self):
        input = """func foo(a int, b float) {return;};"""
        expect = str(Program([FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",FloatType())],VoidType(),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_ast_023(self):
        input = """
            func foo(a [2]ID) {return;}
"""
        expect = str(Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral("2")],Id("ID")))],VoidType(),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_ast_024(self):
        input = """
            func foo(a [2]ID, b [3][ID][4][5]float) {return;}
        """
        expect = str(Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral("2")],Id("ID"))),ParamDecl("b",ArrayType([IntLiteral("3"),Id("ID"),IntLiteral("4"),IntLiteral("5")],FloatType()))],VoidType(),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_ast_025(self):
        input = """
            func foo(a [2]ID, b [3][ID][4][5]float) {
                var x = b
                const y = a
                return y[0][1+1][0]
            }
        """
        expect = str(Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral("2")],Id("ID"))),ParamDecl("b",ArrayType([IntLiteral("3"),Id("ID"), IntLiteral("4"), IntLiteral("5")], FloatType()))],VoidType(),Block([VarDecl("x", None, Id("b")), ConstDecl("y", None, Id("a")), Return(ArrayCell(Id("y"),[IntLiteral("0"),BinaryOp("+",IntLiteral("1"),IntLiteral("1")), IntLiteral("0")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_ast_026(self):
        input = """
            func foo() {
                var a = 1
                var b = 2
                return a + b
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None, IntLiteral("1")), VarDecl("b", None, IntLiteral("2")), Return(BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_ast_027(self):
        input = """
            func foo() {
                a[1 + 1] := 1;
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral("1"), IntLiteral("1"))]),IntLiteral("1"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_ast_028(self):
        input = """
            func foo() int {
                if (a == 1) {
                    return 1
                } else {
                    return 2
                }
            }
        """
        expect = str(Program([FuncDecl("foo",[], IntType(), Block([If(BinaryOp("==", Id("a"), IntLiteral("1")), Block([Return(IntLiteral("1"))]), Block([Return(IntLiteral("2"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_ast_029(self):
        input = """
            func MyInterface() {
                for i < 10 {return;}
                for var i = 0; i < 10; i += 1  {return;}
            }
        """
        expect = str(Program([FuncDecl("MyInterface",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral("10")),Block([Return(None)])),ForStep(VarDecl("i", None,IntLiteral("0")),BinaryOp("<", Id("i"), IntLiteral("10")),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral("1"))),Block([Return(None)]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_ast_030(self):
        input = """
            func foo() {
                const a = a[1].b.c()[2].d.e();
            }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,MethCall(FieldAccess(ArrayCell(MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1)]),"b"),"c",[]),[IntLiteral(2)]),"d"),"e",[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    ### 31 - 40: test struct declaration
    def test_ast_031(self):
        input = """
            type MyStruct struct {
                a int;
            }
        """
        expect = str(Program([StructType("MyStruct",[("a",IntType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_ast_032(self):
        input = """
            type MyStruct struct {
                a int;
                b float;
            }
        """
        expect = str(Program([StructType("MyStruct",[("a",IntType()),("b",FloatType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_ast_033(self):
        input = """
            type MyStruct struct {
                a int;
                b float;
                c string;
            }
        """
        expect = str(Program([StructType("MyStruct",[("a",IntType()),("b",FloatType()),("c",StringType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_ast_034(self):
        input = """
            type MyStruct struct {
                a int;
                b float;
                c string;
                d [2]int;
            }
        """
        expect = str(Program([StructType("MyStruct",[("a",IntType()),("b",FloatType()),("c",StringType()),("d",ArrayType([IntLiteral(2)],IntType()))],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_ast_035(self):
        input = """
            type MyStruct struct {
                a int;
                b float;
                c string;
                d [2]int;
                e [3][4][5]float;
            }
        """
        expect = str(Program([StructType("MyStruct",[("a",IntType()),("b",FloatType()),("c",StringType()),("d",ArrayType([IntLiteral(2)],IntType())),("e",ArrayType([IntLiteral(3),IntLiteral(4),IntLiteral(5)],FloatType()))],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_ast_036(self):
        input = """
            type MyStruct struct {
                a int; b float;
                c string
                d [2]int;
                e [3][4][5]float;
            }
        """
        expect = str(Program([StructType("MyStruct",[("a",IntType()),("b",FloatType()),("c",StringType()),("d",ArrayType([IntLiteral(2)],IntType())),("e",ArrayType([IntLiteral(3),IntLiteral(4),IntLiteral(5)],FloatType()))],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_ast_037(self):
        input = """
            type struct_01 struct {
                a int;
                b float;
                c string;
                d [2]int;
                e [ID][4][5]float;
            }
        """
        expect = str(Program([StructType("struct_01",[("a",IntType()),("b",FloatType()),("c",StringType()),("d",ArrayType([IntLiteral(2)],IntType())),("e",ArrayType([Id("ID"),IntLiteral(4),IntLiteral(5)],FloatType()))],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_ast_038(self):
        input = """
            type struct_02 struct {
                a int;
                b float;
                c string;
                d [2]int;
                e [ID][4][5]float;
                f [ID][ID][ID][ID][ID]ID;
            }
        """
        expect = str(Program([StructType("struct_02",[("a",IntType()),("b",FloatType()),("c",StringType()),("d",ArrayType([IntLiteral(2)],IntType())),("e",ArrayType([Id("ID"),IntLiteral(4),IntLiteral(5)],FloatType())),("f",ArrayType([Id("ID"),Id("ID"),Id("ID"),Id("ID"),Id("ID")],Id("ID")))],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_ast_039(self):
        input = """
            type struct_03 struct {
                a struct_02;
                b float;
                c string; 
            }
"""
        expect = str(Program([StructType("struct_03",[("a",Id("struct_02")),("b",FloatType()),("c",StringType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_ast_040(self):
        input = """
            type struct_04 struct {
                a struct_02;
                b float;
                c string;
                d [2]int;
                e [ID][4][5]float;
                f [ID][ID][ID][ID][ID]ID;
            }
        """
        expect = str(Program([StructType("struct_04",[("a",Id("struct_02")),("b",FloatType()),("c",StringType()),("d",ArrayType([IntLiteral(2)],IntType())),("e",ArrayType([Id("ID"),IntLiteral(4),IntLiteral(5)],FloatType())),("f",ArrayType([Id("ID"),Id("ID"),Id("ID"),Id("ID"),Id("ID")],Id("ID")))],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    ## 41 - 50: test interface declaration
    def test_ast_041(self):
        input = """
            type MyInterface interface {
                Add() ;
            }
"""
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[],VoidType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_ast_042(self):
        input = """
            type MyInterface interface {
                Add(a int) ;
            }
"""
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[IntType()],VoidType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_ast_043(self):
        input = """
            type MyInterface interface {
                Add(a int, b float, c, d string);
            }
"""
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[IntType(),FloatType(),StringType(),StringType()],VoidType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))


    def test_ast_044(self):
        input = """
            type MyInterface interface {
                Add(a int, b float, c, d string);
                Subtract(a, b, c, d, e, f int) int;
            }
        """
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[IntType(),FloatType(),StringType(),StringType()],VoidType()),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType()],IntType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_ast_045(self):
        input = """
            type MyInterface interface {
                Add(a int, b float, c, d string);
                Subtract(a, b, c, d, e, f int) int;
                Multiply(a, b, c, d, e, f int, d float) float;
            }
        """
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[IntType(),FloatType(),StringType(),StringType()],VoidType()),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType()],IntType()),Prototype("Multiply",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],FloatType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_ast_046(self):
        input = """
            type MyInterface interface {
                Add(a int, b float, c, d string);
                Subtract(a, b, c, d, e, f int) int
                Multiply(a, b, c, d, e, f int, d float) float; Divide(a, b, c, d, e, f int, d float) string
            }
        """
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[IntType(),FloatType(),StringType(),StringType()],VoidType()),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType()],IntType()),Prototype("Multiply",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],FloatType()),Prototype("Divide",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],StringType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_ast_047(self):
        input = """
            type MyInterface interface {
                Add(a int, b float, c, d string)
                Subtract(a, b, c, d, e, f int) int
                Multiply(a, b, c, d, e, f int, d float) float; Divide(a, b, c, d, e, f int, d float) string
                Calculate(a, b, c, d, e, f int, d float) float
            }
        """
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[IntType(),FloatType(),StringType(),StringType()],VoidType()),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType()],IntType()),Prototype("Multiply",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],FloatType()),Prototype("Divide",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],StringType()),Prototype("Calculate",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],FloatType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    
    def test_ast_048(self):
        input = """
            type MyInterface interface {
                Add(a int, b float, c, d string)
                Subtract(a, b, c, d, e, f int) int
                Multiply(a, b, c, d, e, f int, d float) float; Divide(a, b, c, d, e, f int, d float) string
                Calculate(a, b, c, d, e, f int, d float) float
                Compare(a, b, c, d, e, f [ID][1][2][3]ID, d float) [3]int
            }
        """
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[IntType(),FloatType(),StringType(),StringType()],VoidType()),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType()],IntType()),Prototype("Multiply",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],FloatType()),Prototype("Divide",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],StringType()),Prototype("Calculate",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],FloatType()),Prototype("Compare",[ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")),ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")),ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")),ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")),ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")),ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")),FloatType()],ArrayType([IntLiteral(3)],IntType()))])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))  

    def test_ast_049(self):
        input = """
            type MyInterface interface {
                Add(a int, b float, c, d string)
                Subtract(a, b, c, d, e, f int) int
                Multiply(a, b, c, d, e, f int, d float) float; Divide(a, b, c, d, e, f int, d float) string
                Calculate(a, b, c, d, e, f int, d float) float
                Compare(a, b, c, d, e [ID][2][1][3]ID, d float) [3]int
                Swap(a, b, c, d, e, f [ID][1][2][3]ID, d float) [ID][1][2][3]ID
            }
        """
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[IntType(),FloatType(),StringType(),StringType()],VoidType()),Prototype("Subtract",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType()],IntType()),Prototype("Multiply",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],FloatType()),Prototype("Divide",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],StringType()),Prototype("Calculate",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],FloatType()),Prototype("Compare",[ArrayType([Id("ID"),IntLiteral(2),IntLiteral(1),IntLiteral(3)], Id("ID")),ArrayType([Id("ID"),IntLiteral(2),IntLiteral(1),IntLiteral(3)], Id("ID")),ArrayType([Id("ID"),IntLiteral(2),IntLiteral(1),IntLiteral(3)], Id("ID")),ArrayType([Id("ID"),IntLiteral(2),IntLiteral(1),IntLiteral(3)], Id("ID")),ArrayType([Id("ID"),IntLiteral(2),IntLiteral(1),IntLiteral(3)], Id("ID")),FloatType()],ArrayType([IntLiteral(3)], IntType())),Prototype("Swap",[ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")), ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")), ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")), ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")), ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")), ArrayType([Id("ID"),IntLiteral(1),IntLiteral(2),IntLiteral(3)], Id("ID")), FloatType()], ArrayType([Id("ID"),IntLiteral(1), IntLiteral(2), IntLiteral(3)], Id("ID")))])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))  

    def test_ast_050(self):
        input = """
            type MyInterface interface {
                Add(a int, b float, c, d string)
                Subtract(a, b, c, d, e, f int) int
                Multiply(a, b, c, d, e, f int, d float) [ID]ID; 
            };"""
        expect = str(Program([InterfaceType("MyInterface",[Prototype("Add",[IntType(),FloatType(),StringType(),StringType()],VoidType()),Prototype("Subtract",[IntType(),IntType(),IntType(), IntType(),IntType(),IntType()],IntType()),Prototype("Multiply",[IntType(),IntType(),IntType(),IntType(),IntType(),IntType(),FloatType()],ArrayType([Id("ID")], Id("ID")))])]))

        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    ## test 51 - 60: Method Declaration
    def test_ast_051(self):
        input = """
            func (MyMethod v) foo(a int) {return;}
"""
        expect = str(Program([MethodDecl("MyMethod",Id("v"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_ast_052(self):
        input = """
            func (v MyMethod) foo(a int, b int) {return;}
"""
        expect = str(Program([MethodDecl("v", Id("MyMethod"),FuncDecl("foo",[ParamDecl("a", IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_ast_053(self):
        input = """
            func (v MyStruct) MyFunc(a, b int, c string, d float) {
                return 1 + 1;
            }
"""
        expect = str(Program([MethodDecl("v", Id("MyStruct"), FuncDecl("MyFunc", [ParamDecl("a", IntType()), ParamDecl("b", IntType()),ParamDecl("c", StringType()), ParamDecl("d", FloatType())], VoidType(), Block([Return(BinaryOp("+", IntLiteral(1), IntLiteral(1)))])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_ast_054(self):
        input = """
           func (v MyStruct) foo(a, b int, c string, d float) [ID][1][ID][2]int {
                return 1 + 1;
            } 
"""
        expect = str(Program([MethodDecl("v", Id("MyStruct"), FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType()),ParamDecl("c", StringType()), ParamDecl("d", FloatType())], ArrayType([Id("ID"),IntLiteral(1),Id("ID"),IntLiteral(2)],IntType()), Block([Return(BinaryOp("+", IntLiteral(1), IntLiteral(1)))])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_ast_055(self):
        input = """
           func (v MyStruct) foo(a, b [1][2][3]ID, c string, d float) [ID][1][ID][2]int {
                return 1 + 1;
            }
"""
        expect = str(Program([MethodDecl("v", Id("MyStruct"), FuncDecl("foo", [ParamDecl("a", ArrayType([IntLiteral(1),IntLiteral(2),IntLiteral(3)],Id("ID"))), ParamDecl("b",ArrayType([IntLiteral(1),IntLiteral(2),IntLiteral(3)],Id("ID"))),ParamDecl("c", StringType()), ParamDecl("d", FloatType())], ArrayType([Id("ID"),IntLiteral(1),Id("ID"),IntLiteral(2)],IntType()), Block([Return(BinaryOp("+", IntLiteral(1), IntLiteral(1)))])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_ast_056(self):
        input = """
            func (Cat c) foo() {return;}
"""
        expect = str(Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[],VoidType(),Block([Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_ast_057(self):
        input = """
            func (Cat c) foo(a ID) ID {return;}
"""
        expect = str(Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[ParamDecl("a",Id("ID"))],Id("ID"),Block([Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_ast_058(self):
        input = """
            func (dog Dog) foo(a ID, b string, c int) [1][ID]string {
                return a + b;
            }
"""
        expect = str(Program([MethodDecl("dog", Id("Dog"), FuncDecl("foo", [ParamDecl("a", Id("ID")), ParamDecl("b", StringType()), ParamDecl("c", IntType())], ArrayType([IntLiteral(1), Id("ID")], StringType()), Block([Return(BinaryOp("+", Id("a"), Id("b")))])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_ast_059(self):
        input = """
            func (dog Dog) foo(a ID, b string) [1][ID]string {
                const a = 1 && 2 || 3 >= 4 + 5 * -6;
                return;
            }
        """
        expect = str(Program([MethodDecl("dog", Id("Dog"), FuncDecl("foo", [ParamDecl("a", Id("ID")), ParamDecl("b", StringType())], ArrayType([IntLiteral(1), Id("ID")], StringType()), Block([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), BinaryOp(">=", IntLiteral(3), BinaryOp("+", IntLiteral(4), BinaryOp("*", IntLiteral(5), UnaryOp("-",IntLiteral(6))))))),Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_ast_060(self):
        input = """
            func (dog Dog) foo(a ID, b string) [1][ID]string {
                return 1 && 2 || 3 >= 4 + 5 * -6;
            }
        """
        expect = str(Program([MethodDecl("dog", Id("Dog"), FuncDecl("foo", [ParamDecl("a", Id("ID")), ParamDecl("b", StringType())], ArrayType([IntLiteral(1), Id("ID")], StringType()), Block([Return(BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), BinaryOp(">=", IntLiteral(3), BinaryOp("+", IntLiteral(4), BinaryOp("*", IntLiteral(5), UnaryOp("-",IntLiteral(6)))))))])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    ## test 61 - 70: test Assign Statement
    def test_ast_061(self):
        input = """
            func foo(){
            a += 1;
            a -= 1;
            a *= 1;
            a /= 1;
            a %= 1;
        } 
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_ast_062(self):
        input = """
            func foo(){
                a[1 + 1] := 1;
            } 
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
        
    def test_ast_063(self):
        input = """
            func foo(){
                a[b[1 + 1]] := 1;
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[ArrayCell(Id("b"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))])]),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_ast_064(self):
        input = """
            func foo(){
                a[2].b.c[2] := 1;
            } 
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),"c"),[IntLiteral(2)]),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_ast_065(self):
        input = """
            func foo(){
                a["s"][foo()] := a[2][2][3];
                a[2] := a[3][4];
                b.c.a[2] := b.c.a[2];
                b.c.a[2][3] := b.c.a[2][3];
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[StringLiteral("\"s\""),FuncCall("foo",[])]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)])),Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_ast_066(self):
        input = """
            func foo(){
                a.b := 1;
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"b"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    

    def test_ast_067(self):
        input = """
            func foo(){
                a.b[2].c := 1;
            } 
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_ast_068(self):
        input = """
            func foo(){
                a.b[2].c := 1;
            } 
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
        

    def test_ast_069(self):
        input = """
            func myFunc() {
                a += 1;
            }
"""
        expect = str(Program([FuncDecl("myFunc",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_ast_070(self):
        input = """
            func myFunc() {
                a[b[c].d.e()] += 1;
            }
"""
        expect = str(Program([FuncDecl("myFunc",[],VoidType(),Block([Assign(ArrayCell(Id("a"), [MethCall(FieldAccess(ArrayCell(Id("b"), [Id("c")]), "d"),"e",[])]),BinaryOp("+", ArrayCell(Id("a"), [MethCall(FieldAccess(ArrayCell(Id("b"), [Id("c")]), "d"),"e",[])]), IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    ### test 71 - 80: If statement
    def test_ast_071(self):
        input = """
            func foo(){
                if(1) {
                    return 1;
                }else if(2) {
                    return 2;
                } else if(3) {
                    return 3;
                } else if(4) {
                    return 4;
                } 

            } 
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(IntLiteral(1))]), 
                If(IntLiteral(2), Block([Return(IntLiteral(2))]), 
                If(IntLiteral(3), Block([Return(IntLiteral(3))]),If(IntLiteral(4), Block([Return(IntLiteral(4))]), None))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_ast_072(self):
        input = """
            func foo(){
                if(1) { return;
                }else if(1) {
                    return 1;
                    return ;
                } else {return;}

                if(1) {return;
                }  else {
                    return 1;
                    return ;
                }

            } 
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Return(IntLiteral(1)),Return(None)]), Block([Return(None)]))),
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(1)),Return(None)]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_ast_073(self):
        input = """
            func foo(){
                if(1) {return;}
                if(1 + 1) {
                    return 1;
                    return;
                }
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), None),
            If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), Block([Return(IntLiteral(1)),Return(None)]), None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_ast_074(self):
        input = """
            func main() {
                if(1) {return;}
            }
"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([If(IntLiteral(1), Block([Return(None)]), None)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_ast_075(self):
        input = """
            func foo() {
                if(1) {
                    a := 1;
                } else {
                    a := 1;
                }
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), Block([Assign(Id("a"),IntLiteral(1))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_ast_076(self):
        input = """
            func main() {
                if(1) { return;
                }else if(1) {
                    a := 1;
                }else if(2) {
                    a := 1;
                }
            }
"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), 
                    If(IntLiteral(2), Block([Assign(Id("a"),IntLiteral(1))]), None)))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_ast_077(self):
        input = """
            func foo() {
                if (1) {
                    const a = -1.;
                    a := 1;
                } else {
                    return;
                }
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([If(IntLiteral(1), Block([
            ConstDecl("a",None,UnaryOp("-", FloatLiteral(1.0))), Assign(Id("a"), IntLiteral(1))]), Block([Return(None)]))]))]))
        
    def test_ast_078(self):
        input = """
            func main() {
                if (1+2-3&&5--1) {
                    return;
                } else if (1 && 2 || 3) {
                    return 1;
                } else if (1 + 2 && 3) {
                    return 2;
                } else if (1 - 2 % 3) {
                    if (1) {
                        return 1;
                    } else if (2) {
                        return 2;
                    } else {
                        return 3;
                    }
                } else {
                    return 0;
                }
            }
"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([
            If(BinaryOp("&&", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), BinaryOp("-", IntLiteral(5), UnaryOp("-",IntLiteral(1)))), Block([Return(None)]), 
               If(BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), Block([Return(IntLiteral(1))]), 
                  If(BinaryOp("&&", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), Block([Return(IntLiteral(2))]), 
                    If(BinaryOp("-", IntLiteral(1), BinaryOp("%", IntLiteral(2), IntLiteral(3))), Block([
                        If(IntLiteral(1), Block([Return(IntLiteral(1))]), 
                           If(IntLiteral(2), Block([Return(IntLiteral(2))]), Block([Return(IntLiteral(3))])))
                    ]), Block([Return(IntLiteral(0))])))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_ast_079(self):
        input = """
            func foo() {
                if (a.b.c) {
                    b.a(2, 3)
                    return;
                } else if (a * (1+2)) {
                    const a = foo( b {}, c {a: 1} ); 
                } else {
                    return a[2][3];
                }
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(), Block([
            If(FieldAccess(FieldAccess(Id("a"),"b"),"c"), Block([MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)]), Return(None)]),
               If(BinaryOp("*", Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2))), Block([ConstDecl("a", None, FuncCall("foo",[StructLiteral("b",[]),StructLiteral("c",[("a",IntLiteral(1))])]))]), 
                  Block([Return(ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]))]))
               )
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_ast_080(self):
        input = """
            func foo() boolean {
                if (true) {
                    return true;
                }
                if (False) {
                    return false;
                }
                return nil;
            }
"""
        expect = str(Program([FuncDecl("foo", [], BoolType(), Block([
            If(BooleanLiteral(True), Block([Return(BooleanLiteral(True))]), None),
            If(Id("False"), Block([Return(BooleanLiteral(False))]), None),
            Return(NilLiteral())
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    ### test 81 - 90: For statement + call statement + break + continue 
    def test_ast_081(self):
        input = """
            func foo() {
                for i < 10 {return;}
                for var i = 0; i < 10; i += 1  {return;}
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([Return(None)])),ForStep(VarDecl("i", None,IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([Return(None)]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_ast_082(self):
        input = """
            func foo() {
                for index, value := range array[2] {return;}
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayCell(Id("array"),[IntLiteral(2)]),Block([Return(None)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_ast_083(self):
        input = """
            func foo() {
                for a.i[8] {
                    return;
                    return 1;
                }
                for i := 0; i[1] < 10; i *= 2+3  {
                    return;
                    return 1;
                }
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(ArrayCell(FieldAccess(Id("a"),"i"),[IntLiteral(8)]),Block([Return(None),Return(IntLiteral(1))])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(1)]), IntLiteral(10)),Assign(Id("i"),BinaryOp("*", Id("i"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))),Block([Return(None),Return(IntLiteral(1))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_ast_084(self):
        input = """
            func votien() {
                for index, value := range [2]int{1,2} {
                     return;
                    return 1;
                }
            }
"""
        expect = str(Program([FuncDecl("votien",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None),Return(IntLiteral(1))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_ast_085(self):
        input = """
            func foo() {
                a.b.c[2].d()
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([MethCall(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(2)]),"d",[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_ast_086(self):
        input = """
            func foo(){
                break;
                continue;
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Break(),Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_ast_087(self):
        input = """
            func foo(){
                foo();
                foo(foo(), 2);
                a.foo();
                a[2].c.foo(foo(), 2);
            }
"""
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("foo",[]),FuncCall("foo",[FuncCall("foo",[]),IntLiteral(2)]),MethCall(Id("a"),"foo",[]),MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"foo",[FuncCall("foo",[]),IntLiteral(2)])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_ast_088(self):
        input = """
            func foo() {
                foo(0 || 1 || 2, 0 >= 1 <= 2, 0 + 1 - 2, foo(), !-!2)
            }
"""
        expect = str(Program([FuncDecl("foo",[], VoidType(), Block([FuncCall("foo", [
            BinaryOp("||", BinaryOp("||", IntLiteral(0), IntLiteral(1)), IntLiteral(2)),
            BinaryOp("<=", BinaryOp(">=", IntLiteral(0), IntLiteral(1)), IntLiteral(2)),
            BinaryOp("-", BinaryOp("+", IntLiteral(0), IntLiteral(1)), IntLiteral(2)),
            FuncCall("foo", []),
            UnaryOp("!",UnaryOp("-",UnaryOp("!",IntLiteral(2))))    
        ])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_ast_089(self):
        input = """
            func foo() {
                for i := 0; i < 10 && i % 2 == 0; i += 1 {
                    return;
                }
            }
"""
        expect = str(Program([FuncDecl("foo", [], VoidType(), Block([
            ForStep(Assign(Id("i"), IntLiteral(0)), BinaryOp("&&", BinaryOp("<", Id("i"), IntLiteral(10)), BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0))), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([Return(None)]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_ast_090(self):
        input = """
            func foo() {
                for abc == def {
                    for i := 0; i < 10; i += 1 {
                        for i, v := range [1]int{1} {
                            return;
                        }
                    }
                }
            }
"""
        expect = str(Program([FuncDecl("foo", [], VoidType(), Block([
            ForBasic(BinaryOp("==", Id("abc"), Id("def")), Block([
                ForStep(Assign(Id("i"), IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([
                    ForEach(Id("i"), Id("v"), ArrayLiteral([IntLiteral(1)], IntType(), [IntLiteral(1)]), Block([Return(None)]))
                ]))
            ]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_ast_091(self):
        input = """
            const foo = foo( 1 );         
"""
        expect = str(Program([ConstDecl("foo",None,FuncCall("foo",[IntLiteral(1)]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_ast_092(self):
        input = """const abc = foo( a[0b1][3] ); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[ArrayCell(Id("a"),[IntLiteral("0b1"),IntLiteral(3)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_ast_093(self):
        input = """
            const a = [1][3]float{1.};
"""
        expect = str(Program([ConstDecl("a",None,ArrayLiteral([IntLiteral("1"),IntLiteral("3")],FloatType(),[FloatLiteral("1.")]))
		]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_ast_094(self):
        input = """
            const a = ID{a: [1][1]ID{1}};
"""
        expect = str(Program([ConstDecl("a",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral(1),IntLiteral(1)],Id("ID"),[IntLiteral(1)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_ast_095(self):
        input = """
            const a = ID{b: true};
"""
        expect = str(Program([ConstDecl("a",None,StructLiteral("ID",[("b",BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_ast_096(self):
        input = """
            const a = ID {}.a[2];
"""
        expect = str(Program([ConstDecl("a",None,ArrayCell(FieldAccess(StructLiteral("ID",[]),"a"),[IntLiteral(2)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_ast_097(self):
        input = """
            const a = a.b().c().d();
"""
        expect = str(Program([ConstDecl("a",None,MethCall(MethCall(MethCall(Id("a"),"b",[]),"c",[]),"d",[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_ast_098(self):
        input = """
            const a = a * (nil - "a");
"""
        expect = str(Program([ConstDecl("a",None,BinaryOp("*", Id("a"), BinaryOp("-", NilLiteral(), StringLiteral("\"a\""))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_ast_099(self):
        input = """
            const a = a[2] + b[3];
"""
        expect = str(Program([ConstDecl("a",None,BinaryOp("+", ArrayCell(Id("a"), [IntLiteral(2)]), ArrayCell(Id("b"), [IntLiteral(3)])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    
    def test_ast_100(self):
        input = """
            const a = a[2].b + b[3].c;
"""
        expect = str(Program([ConstDecl("a",None,BinaryOp("+", FieldAccess(ArrayCell(Id("a"), [IntLiteral(2)]),"b"), FieldAccess(ArrayCell(Id("b"), [IntLiteral(3)]),"c")))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    
