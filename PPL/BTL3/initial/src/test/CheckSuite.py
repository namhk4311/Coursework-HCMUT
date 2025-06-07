import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    #simple test
    def test_001(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_002(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_003(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_004(self):
        """
var abc = 1; 
var abc = 2;
        """
        input = Program([VarDecl("abc", None,IntLiteral(1)),VarDecl("abc", None,IntLiteral(2))])
        expect = "Redeclared Variable: abc\n"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_005(self):
        """
var abc = 1; 
const abc = 2;
        """
        input = Program([VarDecl("abc", None,IntLiteral(1)),ConstDecl("abc",None,IntLiteral(2))])
        expect = "Redeclared Constant: abc\n"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_006(self):
        """
const def = 1; 
var def = 2;
        """
        input = Program([ConstDecl("def",None,IntLiteral(1)),VarDecl("def", None,IntLiteral(2))])
        expect = "Redeclared Variable: def\n"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_007(self):
        """
const aaa = 1; 
func aaa () {return;}
        """
        input = Program([ConstDecl("aaa",None,IntLiteral(1)),FuncDecl("aaa",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: aaa\n"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_008(self):
        """ 
func myfunction () {return;}
var myfunction = 1;
        """
        input = Program([FuncDecl("myfunction",[],VoidType(),Block([Return(None)])),VarDecl("myfunction", None,IntLiteral(1))])
        expect = "Redeclared Variable: myfunction\n"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_009(self):
        """ 
var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        expect = "Redeclared Variable: getInt\n"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_010(self):
        """ 
type myStruct struct {
    myStruct int;
}
type myStruct2 struct {
    myStruct string;
    atribute int;
    atribute float;
}
        """
        input = Program([StructType("myStruct",[("myStruct",IntType())],[]),StructType("myStruct2",[("myStruct",StringType()),("atribute",IntType()),("atribute",FloatType())],[])])
        expect = "Redeclared Field: atribute\n"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_011(self):
        """ 
func (v myStruct) putIntLn () {return;}
func (v myStruct) getInt () {return;}
func (v myStruct) getInt () {return;}
type myStruct struct {
    hello int;
}
        """
        input = Program([MethodDecl("v",Id("myStruct"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("myStruct"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("myStruct"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("myStruct",[("hello",IntType())],[])])
        expect = "Redeclared Method: getInt\n"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_012(self):
        """ 
type myInterface interface {
    abc();
    abc(a int);
}
        """
        input = Program([InterfaceType("myInterface",[Prototype("abc",[],VoidType()),Prototype("abc",[IntType()],VoidType())])])
        expect = "Redeclared Prototype: abc\n"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_013(self):
        """ 
func myFunc (a, a int) {return;}
        """
        input = Program([FuncDecl("myFunc",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_014(self):
        """ 
func myFunc (b int) {
    var b = 1;
    var a = 1;
    const a = 1;
}
        """
        input = Program([FuncDecl("myFunc",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_015(self):
        """ 
func myFunc (b int) {
    for var a = 1; a < 1; a += 1 {
        const a = 2;
    }
}
        """
        input = Program([FuncDecl("myFunc",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_016(self):
        """ 
var a = 1;
var b = a;
var c = d;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_017(self):
        """ 
func myFunc() int {return 1;}

fun foo () {
    var b = myFunc();
    foo_myFunc();
    return;
}
        """
        input = Program([FuncDecl("myFunc",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("myFunc",[])),FuncCall("foo_myFunc",[]),Return(None)]))])
        expect = "Undeclared Function: foo_myFunc\n"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_018(self):
        """ 
type myStruct struct {
    a int;
}

func (v myStruct) getInt () {
    const c = v.a;
    var d = v.b;
}
        """
        input = Program([StructType("myStruct",[("a",IntType())],[]),MethodDecl("v",Id("myStruct"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"a")),VarDecl("d", None,FieldAccess(Id("v"),"b"))])))])
        expect = "Undeclared Field: b\n"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_019(self):
        """ 
type myStruct struct {
    a int;
}

func (v myStruct) getInt () {
    v.getInt();
    v.putInt();
}
        """
        input = Program([StructType("myStruct",[("a",IntType())],[]),MethodDecl("v",Id("myStruct"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        expect = "Undeclared Method: putInt\n"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_020(self):
        """func putInt() {return;}"""
        input = Program([FuncDecl("putInt",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Function: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_021(self):
        """type myStruct struct {abc int;}
           func (v myStruct) foo (v, v int) {return;}
           func foo () {return;}"""
        input = Program([StructType("myStruct",[("abc",IntType())],[]),MethodDecl("v",Id("myStruct"),FuncDecl("foo",[ParamDecl("v",IntType()),ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Parameter: v\n"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_022(self):
        """func (v myStruct) foo (a, b int) {var a = 1;}
           type myStruct struct {abc int;}
           type myStruct2 struct {def int;}
           func (v myStruct2) foo (a, b int) {var a = 1; const a = 1;}"""
        input = Program([MethodDecl("v",Id("myStruct"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),StructType("myStruct",[("abc",IntType())],[]),StructType("myStruct2",[("def",IntType())],[]),MethodDecl("v",Id("myStruct2"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1)), ConstDecl("a", None,IntLiteral(1))])))])
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_023(self):
        """const a = 2;
           func foo () {
               const a = 1;
               for a < 1 {
                   const a = 1;
                   for a < 1 {
                       const a = 1;
                       const b = 1;
                   }
                   const b = 1;
                   var a = 1;
               }
           }"""
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ConstDecl("b",None,IntLiteral(1))])),ConstDecl("b",None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))]))])
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_024(self):
        """func foo () {
            const a = 1;
            for a, b := range [3]int {1, 2, 3} {
                var b = 1;
            }
        }"""
        input = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1))]))]))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_025(self):
        """var a = 1;
           func foo () {
               const b = 1;
               for a, b := range [3]int{1, 2, 3} {
                   var d = b;
               }
               var d = b;
               var a = 1;
           }
           var d = a;"""
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("b"))])),VarDecl("d", None,Id("b")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("a"))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_026(self):
        """var a = foo();
           func foo () int {
               var a = koo();
               var c = getInt();
               putInt(c);
               putIntLn(c);
               return 1;
           }
           var d = foo();
           func koo () int {
               var a = foo();
               return 1;
           }"""
        input = Program([VarDecl("a", None,FuncCall("foo",[])),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,FuncCall("koo",[])),VarDecl("c", None,FuncCall("getInt",[])),FuncCall("putInt",[Id("c")]),FuncCall("putIntLn",[Id("c")]),Return(IntLiteral(1))])),VarDecl("d", None,FuncCall("foo",[])),FuncDecl("koo",[],IntType(),Block([VarDecl("a", None,FuncCall("foo",[])),Return(IntLiteral(1))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_027(self):
        """var v ABC;
           const b = v.b;
           type ABC struct {a int; b int; c int;}
           const a = v.a;
           const e = v.e;"""
        input = Program([VarDecl("v",Id("ABC"), None),ConstDecl("b",None,FieldAccess(Id("v"),"b")),StructType("ABC",[("a",IntType()),("b",IntType()),("c",IntType())],[]),ConstDecl("a",None,FieldAccess(Id("v"),"a")),ConstDecl("e",None,FieldAccess(Id("v"),"e"))])
        expect = "Undeclared Field: e\n"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_028(self):
        """var v ABC;
           const b = v.foo();
           type ABC struct {a int;}
           func (v ABC) foo() int {return 1;}
           func (v ABC) koo() int {return 1;}
           const c = v.koo();
           const d = v.zoo();"""
        input = Program([VarDecl("v",Id("ABC"), None),ConstDecl("b",None,MethCall(Id("v"),"foo",[])),StructType("ABC",[("a",IntType())],[]),MethodDecl("v",Id("ABC"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("v",Id("ABC"),FuncDecl("koo",[],IntType(),Block([Return(IntLiteral(1))]))),ConstDecl("c",None,MethCall(Id("v"),"koo",[])),ConstDecl("d",None,MethCall(Id("v"),"zoo",[]))])
        expect = "Undeclared Method: zoo\n"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_029(self):
        """var v ABC;
           type ABC struct {a int;}
           func (v ABC) foo() int {return 1;}
           func (b ABC) koo() {b.koo();}
           func foo() {
               const b = v.foo();
               v.koo();
               const d = v.zoo();
           }"""
        input = Program([VarDecl("v",Id("ABC"), None),StructType("ABC",[("a",IntType())],[]),MethodDecl("v",Id("ABC"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("ABC"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,MethCall(Id("v"),"foo",[])),MethCall(Id("v"),"koo",[]),ConstDecl("d",None,MethCall(Id("v"),"zoo",[]))]))])
        expect = "Undeclared Method: zoo\n"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_030(self):
        """
           var v ABC;
           type ABC struct {a int;}
           type DEF interface {foo() int;}
           func (v ABC) foo() int {return 1;}
           func (b ABC) koo() {b.koo();}
           func foo() {
               var x DEF;
               const b = x.foo();
               x.koo();
           }
        """
        input = Program([VarDecl("v",Id("ABC"), None),StructType("ABC",[("a",IntType())],[]),InterfaceType("DEF",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("ABC"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("ABC"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("DEF"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        expect = "Undeclared Method: koo\n"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_031(self):
        """const a = 1;
           func foo() {var a = 1;}
           func foo() {var b = 1;}
           """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,IntLiteral(1))]))])
        expect = "Redeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_032(self):
        """type ABC struct {abc int;}
           func (v ABC) foo (a, b int) {return;}
           func foo (a, a int) {return;}"""
        input = Program([StructType("ABC",[("abc",IntType())],[]),MethodDecl("v",Id("ABC"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_033(self):
        """type ABC struct {abc int;}
           var a = 1;
           func (v ABC) foo (a, b int) {var a = v.abc;}
           func foo (a, b int) {var a = 1;}"""
        input = Program([StructType("ABC",[("abc",IntType())],[]),VarDecl("a", None,IntLiteral(1)),MethodDecl("v",Id("ABC"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None, FieldAccess(Id("v"),"def"))]))),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))])
        expect = "Undeclared Field: def\n"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_034(self):
        """type S1 struct {abc int;}
           type S2 struct {def int;}
           var v S1;
           const x = v;
           var z S1 = x;
           var k S2 = x;"""
        input = Program([StructType("S1",[("abc",IntType())],[]),StructType("S2",[("def",IntType())],[]),VarDecl("v",Id("S1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("S1"),Id("x")),VarDecl("k",Id("S2"),Id("x"))])
        expect = "Type Mismatch: VarDecl(k,Id(S2),Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_035(self):
        """type S1 struct {abc int;}
           type S2 struct {abc int;}
           type I1 interface {abc();}
           type I2 interface {abc();}
           func (s S1) abc() {return;}
           var a S1;
           var b S2;
           var c I1 = a;
           var d I2 = b;"""
        input = Program([StructType("S1",[("abc",IntType())],[]),StructType("S2",[("abc",IntType())],[]),InterfaceType("I1",[Prototype("abc",[],VoidType())]),InterfaceType("I2",[Prototype("abc",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("abc",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        expect = "Redeclared Method: abc\n"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_036(self):
        """type S1 struct {abc int;}
           type S2 struct {abc int;}
           type I1 interface {abc();}
           type I2 interface {abc() int;}
           func (s S1) abc() {return;}
           var a S1;
           var b S2;
           var c I2 = a;"""
        input = Program([StructType("S1",[("abc",IntType())],[]),StructType("S2",[("abc",IntType())],[]),InterfaceType("I1",[Prototype("abc",[],VoidType())]),InterfaceType("I2",[Prototype("abc",[],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("abc",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I2"),Id("a"))])
        expect = "Redeclared Method: abc\n"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_037(self):
        """type S1 struct {abc int;}
           type S2 struct {abc int;}
           type I1 interface {abc() S1;}
           type I2 interface {abc() S2;}
           func (s S1) abc() S1 {return s;}
           var a S1;
           var c I1 = a;
           var d I2 = a;"""
        input = Program([StructType("S1",[("abc",IntType())],[]),StructType("S2",[("abc",IntType())],[]),InterfaceType("I1",[Prototype("abc",[],Id("S1"))]),InterfaceType("I2",[Prototype("abc",[],Id("S2"))]),MethodDecl("s",Id("S1"),FuncDecl("abc",[],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        expect = "Redeclared Method: abc\n"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_038(self):
        """type S1 struct {abc int;}
           type S2 struct {abc int;}
           type I1 interface {abc(e, e int) S1;}
           type I2 interface {abc(a int) S1;}
           func (s S1) abc(a, b int) S1 {return s;}
           var a S1;
           var c I1 = a;
           var d I2 = a;"""
        input = Program([StructType("S1",[("abc",IntType())],[]),StructType("S2",[("abc",IntType())],[]),InterfaceType("I1",[Prototype("abc",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("abc",[IntType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("abc",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        expect = "Redeclared Method: abc\n"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_039(self):
        """type ABC struct {v int;}
           var v ABC;
           func foo(){
               for 1 {var a int = 1.2;}
           }"""
        input = Program([StructType("ABC",[("v",IntType())],[]),VarDecl("v",Id("ABC"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
        expect = "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.2))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_040(self):
        """var a = [2] int {1, 2}
           var c [3] int = a"""
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3)]),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_041(self):
        """var a = [2] int {1, 2}
           var c [3] float = a"""
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],FloatType()),Id("a"))])
        expect = "Type Mismatch: VarDecl(c,ArrayType(FloatType,[IntLiteral(3)]),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_042(self):
        """var a [2][3] int;
           var b = a[1];
           var c [2] int = b;
           var d [1] string = b;"""
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(2)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_043(self):
        """var a = [2] int {1, 2}
           var c [3][2] int = a"""
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3),IntLiteral(2)],IntType()),Id("a"))])
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3),IntLiteral(2)]),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_044(self):
        """type S1 struct {v int; x S1;}
           var b S1;
           var c = b.x.v;
           var d = c.x;"""
        input = Program([StructType("S1",[("v",IntType()),("x",Id("S1"))],[]),VarDecl("b",Id("S1"), None),VarDecl("c", None,FieldAccess(FieldAccess(Id("b"),"x"),"v")),VarDecl("d", None,FieldAccess(Id("c"),"x"))])
        expect = "Type Mismatch: FieldAccess(Id(c),x)\n"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_045(self):
        """type S1 struct {abc int;}
           type I1 interface {abc();}
           var a I1;
           var c I1 = nil;
           var d S1 = nil;
           func foo(){
               c := a;
               a := nil;
           }
           var e int = nil;"""
        input = Program([StructType("S1",[("abc",IntType())],[]),InterfaceType("I1",[Prototype("abc",[],VoidType())]),VarDecl("a",Id("I1"), None),VarDecl("c",Id("I1"),NilLiteral()),VarDecl("d",Id("S1"),NilLiteral()),FuncDecl("foo",[],VoidType(),Block([Assign(Id("c"),Id("a")),Assign(Id("a"),NilLiteral())])),VarDecl("e",IntType(),NilLiteral())])
        expect = "Type Mismatch: VarDecl(e,IntType,Nil)\n"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_046(self):
        """var a = -1;
           var b = -1.2;
           var c = - true;"""
        input = Program([VarDecl("a", None,UnaryOp("-",IntLiteral(1))),VarDecl("b", None,UnaryOp("-",FloatLiteral(1.2))),VarDecl("c", None,UnaryOp("-",BooleanLiteral(True)))])
        expect = "Type Mismatch: UnaryOp(-,BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_047(self):
        """var a = ! true;
           var b = ! 1;"""
        input = Program([VarDecl("a", None,UnaryOp("!",BooleanLiteral(True))),VarDecl("b", None,UnaryOp("!",IntLiteral(1)))])
        expect = "Type Mismatch: UnaryOp(!,IntLiteral(1))\n"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_048(self):
        """var a int = 1 % 2;
           var b int = 1 % 2.0;"""
        input = Program([VarDecl("a",IntType(),BinaryOp("%", IntLiteral(1), IntLiteral(2))),VarDecl("b",IntType(),BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_049(self):
        """var a boolean = true && false || true;
           var b boolean = true && 1;"""
        input = Program([VarDecl("a",BoolType(),BinaryOp("||", BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True))),VarDecl("b",BoolType(),BinaryOp("&&", BooleanLiteral(True), IntLiteral(1)))])
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),&&,IntLiteral(1))\n"
        self.assertTrue(TestChecker.test(input, expect, 448))


    def test_050(self):
        """
           var a boolean = 1 > 2;
           var b boolean = 1.0 < 2.0;
           var c boolean = "1" == "2";
           var d boolean = 1 > 2.0;
        """
        input = Program([
            VarDecl("a",BoolType(),BinaryOp(">", IntLiteral(1), IntLiteral(2))),
            VarDecl("b",BoolType(),BinaryOp("<", FloatLiteral(1.0), FloatLiteral(2.0))),
            VarDecl("c",BoolType(),BinaryOp("==", StringLiteral("\"1\""), StringLiteral("\"2\""))),
            VarDecl("d",BoolType(),BinaryOp(">", IntLiteral(1), FloatLiteral(2.0)))
            ])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),>,FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_051(self):
        """var a boolean = 1 > 2;
           var b boolean = 1.0 < 2.0;
           var c boolean = "1" == "2";
           var d boolean = 1 > 2.0;"""
        input = Program([
            VarDecl("a",BoolType(),BinaryOp(">", IntLiteral(1), IntLiteral(2))),
            VarDecl("b",BoolType(),BinaryOp("<", FloatLiteral(1.0), FloatLiteral(2.0))),
            VarDecl("c",BoolType(),BinaryOp("==", StringLiteral("\"1\""), StringLiteral("\"2\""))),
            VarDecl("d",BoolType(),BinaryOp(">", IntLiteral(1), FloatLiteral(2.0)))
            ])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),>,FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_052(self):
        """func foo(){
            for var i int = 1; i; i := 1. {
                var a = 1;
            }
        }"""
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),Id("i"),Assign(Id("i"),FloatLiteral(1.)),Block([VarDecl("a", None,IntLiteral(1))]))]))])
        expect = "Type Mismatch: For(VarDecl(i,IntType,IntLiteral(1)),Id(i),Assign(Id(i),FloatLiteral(1.0)),Block([VarDecl(a,IntLiteral(1))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_053(self):
        """var a = [2] int {1, 2}
           var c [2] float = a"""
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(2)],FloatType()),Id("a"))])
        expect = "Type Mismatch: VarDecl(c,ArrayType(FloatType,[IntLiteral(2)]),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_054(self):
        """var a [2][3] int;
           var b = a[1];
           var c [3] int = b;
           var d [3] string = b;"""
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(3)],StringType()),Id("b"))])
        expect = "Type Mismatch: VarDecl(d,ArrayType(StringType,[IntLiteral(3)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_055(self):
        """func foo() int {
            return [2] int {1, 2}[a];
        }
        var a = foo();"""
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(ArrayCell(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),[Id("a")]))])),VarDecl("a", None,FuncCall("foo",[]))])
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_056(self):
        """type putLn struct {a int;};"""
        input = Program([StructType("putLn",[("a",IntType())],[])])
        expect = "Redeclared Type: putLn\n"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_057(self):
        """type putLn interface {foo();};"""
        input = Program([InterfaceType("putLn",[Prototype("foo",[],VoidType())])])
        expect = "Redeclared Type: putLn\n"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_058(self):
        """type ABC struct {a [2]int;} 
           type DEF interface {foo() int;}
           func (v ABC) foo() int {return 1;}
           func foo(a DEF) {
               var b DEF = ABC{a: [2]int{1, 2}};
               foo(1)
           }"""
        input = Program([StructType("ABC",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("DEF",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("ABC"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("DEF"))],VoidType(),Block([VarDecl("b",Id("DEF"),StructLiteral("ABC",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),FuncCall("foo",[IntLiteral(1)])]))])
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(1)])\n"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_059(self):
        """type ABC struct {a [2]int;} 
           type DEF interface {foo() int;}
           func (v ABC) foo() int {return 1;}
           func foo(a DEF) {
               var b = nil;
               foo(b)
               const b = nil;
           }"""
        input = Program([StructType("ABC",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("DEF",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("ABC"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("DEF"))],VoidType(),Block([VarDecl("b", None,NilLiteral()),FuncCall("foo",[Id("b")]),ConstDecl("b", None,NilLiteral())]))])
        expect = "Redeclared Constant: b\n"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_060(self):
        """func foo(){return}
           func foo1() int{return 1}
           func foo2() float{return 2}"""
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("foo1",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo2",[],FloatType(),Block([Return(IntLiteral(2))]))])
        expect = "Type Mismatch: Return(IntLiteral(2))\n"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_061(self):
        """type ABC struct {a [2]int;} 
           func foo() ABC {return 1}"""
        input = Program([StructType("ABC",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),FuncDecl("foo",[],Id("ABC"),Block([Return(IntLiteral(1))]))])
        expect = "Type Mismatch: Return(IntLiteral(1))\n"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_062(self):
        """func foo() [2] float {
            return [2] float {1.0, 2.0};
            return [2] int {1, 2};
        }"""
        input = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],FloatType()),Block([Return(ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])),Return(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        expect = "Type Mismatch: Return(ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_063(self):
        """var A = 1;
           type A struct {a int;}"""
        input = Program([VarDecl("A", None,IntLiteral(1)),StructType("A",[("a",IntType())],[])])
        expect = "Redeclared Type: A\n"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_064(self):
        """type S1 struct {abc int;}
           type I1 interface {abc();}
           func (s S1) abc() {return;}
           var b [2] S1;
           var a [2] I1 = b;"""
        input = Program([StructType("S1",[("abc",IntType())],[]),InterfaceType("I1",[Prototype("abc",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("abc",[],VoidType(),Block([Return(None)]))),VarDecl("b",ArrayType([IntLiteral(2)],Id("S1")), None),VarDecl("a",ArrayType([IntLiteral(2)],Id("I1")),Id("b"))])
        expect = "Redeclared Method: abc\n"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_065(self):
        """var a [1 + 9] int;
           var b [10] int = a;
           var c int = a;"""
        input = Program([VarDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(9))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(10)],IntType()),Id("a")), VarDecl("c", IntType(), Id("a"))])
        expect = "Type Mismatch: VarDecl(c,IntType,Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_066(self):
        """var a [5 / 2] int;
           var b [2] int = a;
           var c int = b;"""
        input = Program([VarDecl("a",ArrayType([BinaryOp("/", IntLiteral(5), IntLiteral(2))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(2)],IntType()),Id("a")), VarDecl("c",IntType(),Id("b"))])
        expect = "Type Mismatch: VarDecl(c,IntType,Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_067(self):
        """var a [5 % 2] int;
           var b [1] int = a;
           var d int = b;"""
        input = Program([VarDecl("a",ArrayType([BinaryOp("%", IntLiteral(5), IntLiteral(2))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(1)],IntType()),Id("a")), VarDecl("d", IntType(), Id("b"))])
        expect = "Type Mismatch: VarDecl(d,IntType,Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_068(self):
        """const a = 2 + 3;
           var b [a * 2 + a] int;
           var c [15] int = b;
           var d [a * 2] int = c;"""
        input = Program([ConstDecl("a",None,BinaryOp("+", IntLiteral(2), IntLiteral(3))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(15)],IntType()),Id("b")), VarDecl("d", ArrayType([BinaryOp("*", Id("a"), IntLiteral(2))],IntType()),Id("c"))])
        expect = "Type Mismatch: VarDecl(d,ArrayType(IntType,[IntLiteral(10)]),Id(c))\n"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_069(self):
        """const v = 3;
           const a = v + v;
           var b [a * 2 + a] int;
           var c [18] int = b;
           var d int = d;"""
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b")), VarDecl("d",IntType(),Id("d"))])
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_070(self):
        """const v = 3;
           var c [3] int = [v * 1] int {1 , 2, 3};
           var d int = c;"""
        input = Program([ConstDecl("v",None,IntLiteral(3)),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),ArrayLiteral([BinaryOp("*", Id("v"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])), VarDecl("d", IntType(), Id("c"))])
        expect = "Type Mismatch: VarDecl(d,IntType,Id(c))\n"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_071(self):
        """const v = 3;
           const k = v + 1;
           func foo(a [1 + 2] int) {
               foo([k - 1] int {1,2,3})
               foo(1)
           }"""
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("k",None,BinaryOp("+", Id("v"), IntLiteral(1))),FuncDecl("foo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])]), FuncCall("foo",[IntLiteral(1)])]))])
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(1)])\n"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_072(self):
        """type K struct {a int;}
           func (k K) koo(a [1 + 2] int) {return;}
           type H interface {koo(a [1 + 2] int);}
           const c = 4;
           func foo() {
               var k H;
               k.koo([c - 1] int {1,2,3})
               var h string = k.a;
           }"""
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],VoidType())]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],VoidType(),Block([VarDecl("k",Id("H"), None),MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])]), VarDecl("h", StringType(), FieldAccess(Id("k"), "a"))]))])
        expect = "Type Mismatch: FieldAccess(Id(k),a)\n"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_073(self):
        """type K struct {a int;}
           func (k K) koo(a [1 + 2] int) [1 + 2] int {return [3*1] int {1,2,3};}
           type H interface {koo(a [1 + 2] int) [1 + 2] int;}
           const c = 4;
           func foo() [1 + 2] int{
               return foo()
               var k K;
               return k.koo([c - 1] int {1,2,3})
               var h H;
               return h.koo([c - 1] int {1,2,3})
               var c int = h;
           }"""
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(ArrayLiteral([BinaryOp("*", IntLiteral(3), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(FuncCall("foo",[])),VarDecl("k",Id("K"), None),Return(MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])),VarDecl("h",Id("H"), None),Return(MethCall(Id("h"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])), VarDecl("c", IntType(), Id("h"))]))])
        expect = "Type Mismatch: VarDecl(c,IntType,Id(h))\n"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_074(self):
        """var a [2][3][4] int;
           var b [3][4] int = a[1];
           var c [4] int = a[1][1];
           var d int = a[1][1][1];
           var e int = c;"""
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3),IntLiteral(4)],IntType()), None),VarDecl("b",ArrayType([IntLiteral(3),IntLiteral(4)],IntType()),ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(4)],IntType()),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1)])),VarDecl("d",IntType(),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1),IntLiteral(1)])), VarDecl("e", IntType(),Id("c"))])
        expect = "Type Mismatch: VarDecl(e,IntType,Id(c))\n"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_075(self):
        """func foo() {
            a := 1;
            var a = 1;
        }"""
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_076(self):
        """const a = 2;
           type STRUCT struct {x [a] int;}
           func (s STRUCT) foo(x [a] int) [a] int {return s.x;}
           func foo(x [a] int) [a] int  {
               const a = 3;
               return [a] int {1,2};
           }"""
        input = Program([ConstDecl("a",None,IntLiteral(2)),StructType("STRUCT",[("x",ArrayType([Id("a")],IntType()))],[]),MethodDecl("s",Id("STRUCT"),FuncDecl("foo",[ParamDecl("x",ArrayType([Id("a")],IntType()))],ArrayType([Id("a")],IntType()),Block([Return(FieldAccess(Id("s"),"x"))]))),FuncDecl("foo",[ParamDecl("x",ArrayType([Id("a")],IntType()))],ArrayType([Id("a")],IntType()),Block([ConstDecl("a",None,IntLiteral(3)),Return(ArrayLiteral([Id("a")],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_077(self):
        """func foo()  {return ;}
           func abc()  {
               foo();
               return abc();
           }"""
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("abc",[],VoidType(),Block([FuncCall("foo",[]),Return(FuncCall("abc",[]))]))])
        expect = "Type Mismatch: FuncCall(abc,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_078(self):
        """var a ABC;
           func foo() ABC {
               return a;
               return ABC;
           }
           type ABC struct {abc int;}"""
        input = Program([VarDecl("a",Id("ABC"), None),FuncDecl("foo",[],Id("ABC"),Block([Return(Id("a")),Return(Id("ABC"))])),StructType("ABC",[("abc",IntType())],[])])
        expect = "Undeclared Identifier: ABC\n"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_079(self):
        """func A() {
            return A;
        }"""
        input = Program([FuncDecl("A",[],VoidType(),Block([Return(Id("A"))]))])
        expect = "Undeclared Identifier: A\n"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_080(self):
        """var a float = 1 * 2.0;
           var b int = 1 / 2;
           var c float = 1 / 2;
           func foo() int {
               return b;
               return c;
           }"""
        input = Program([VarDecl("a",FloatType(),BinaryOp("*", IntLiteral(1), FloatLiteral(2.0))),VarDecl("b",IntType(),BinaryOp("/", IntLiteral(1), IntLiteral(2))),VarDecl("c",FloatType(),BinaryOp("/", IntLiteral(1), IntLiteral(2))),FuncDecl("foo",[],IntType(),Block([Return(Id("b")),Return(Id("c"))]))])
        expect = "Type Mismatch: Return(Id(c))\n"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_081(self):
        """var a = 1;
           func foo () {
               const b = 1;
               for a, b := range [3][2]int{1, 2, 3} {
                   var d [1+2] int = b;
               }
               var d = b;
               var a = 1;
           }
           var d = a;"""
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3), IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))], IntType()),Id("b"))])),VarDecl("d", None,Id("b")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("a"))])
        expect = "Type Mismatch: ForEach(Id(a),Id(b),ArrayLiteral([IntLiteral(3),IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl(d,ArrayType(IntType,[BinaryOp(IntLiteral(1),+,IntLiteral(2))]),Id(b))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_082(self):
        """func foo(){
            for i := 1; i < 10; c += 1 {
                var c = 5;
            }
        }"""
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("c"),BinaryOp("+",Id("c"),IntLiteral(1))),Block([VarDecl("c", None,IntLiteral(5))]))]))])
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_083(self):
        """type ABC struct {abc int;}
           func (v ABC) foo (v int) {return v;}
           func foo () {return;}"""
        input = Program([StructType("ABC",[("abc",IntType())],[]),MethodDecl("v",Id("ABC"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(Id("v"))]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        expect = "Type Mismatch: Return(Id(v))\n"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_084(self):
        """const a = 2;
           func foo () {
               const a = 1;
               for var a = 1; a < 1; b := 2 {
                   const b = 1;
               }
           }"""
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Block([ConstDecl("b",None,IntLiteral(1))]))]))])
        expect = "Redeclared Constant: b\n"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_085(self):
        """
func (v ABC) abc() {return ;}
func (v ABC) def() {return ;}
type ABC struct {
    a int;
    def int;
}  
        """
        input = Program([MethodDecl("v",Id("ABC"),FuncDecl("abc",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("ABC"),FuncDecl("def",[],VoidType(),Block([Return(None)]))),StructType("ABC",[("a",IntType()),("def",IntType())],[])])
        expect = "Redeclared Method: def\n"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_086(self):
        """
func foo() {
    foo := 1;
    foo()
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("foo"),IntLiteral(1)),FuncCall("foo",[])]))])
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_087(self):
        input = Program([FuncDecl("main",[],VoidType(), Block([VarDecl("a", IntType(), None), Assign(Id("a"),BinaryOp("+", Id("a"),StringLiteral("str")))]))])
        expect = "Type Mismatch: BinaryOp(Id(a),+,StringLiteral(str))\n"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_088(self):
        input = Program([
    FuncDecl(
        "main",
        [],
        VoidType(),
        Block([
            VarDecl("a", IntType(), None),
            VarDecl("b", IntType(), None),
            VarDecl("c", IntType(), None),
            ForEach(
                Id("a"),
                Id("b"),
                Id("c"),
                Block([
                    VarDecl("d", None, IntLiteral(1))
                ])
            )
        ])
    )
])
        expect = "Type Mismatch: ForEach(Id(a),Id(b),Id(c),Block([VarDecl(d,IntLiteral(1))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 487))


    def test_089(self):
        input = Program([
            FuncDecl("main",[],VoidType(), Block([VarDecl("a", IntType(), None), Assign(Id("a"),BinaryOp("+", Id("a"),StringLiteral("str")))]))
        ])
        expect = "Type Mismatch: BinaryOp(Id(a),+,StringLiteral(str))\n"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_090(self):
        """
var a = 1;
var b = 2;
var c = a + b;
var d = c + 3;
var e = d + 4;
var f = e + 5;
        """
        input = Program([VarDecl("a", None, IntLiteral(1)), VarDecl("b", None, IntLiteral(2)), VarDecl("c", None, BinaryOp("+", Id("a"), Id("b"))), VarDecl("d", None, BinaryOp("+", Id("c"), IntLiteral(3))), VarDecl("e", None, BinaryOp("+", Id("d"), IntLiteral(4))), VarDecl("f", None, BinaryOp("+", Id("e"), IntLiteral(5)))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_091(self):
        """
var a = 1;
var b = 2;
var c = a + b;
var d = c + 3;
var e = d + 4;
var f = e + 5.0;
        """
        input = Program([VarDecl("a", None, IntLiteral(1)), VarDecl("b", None, IntLiteral(2)), VarDecl("c", None, BinaryOp("+", Id("a"), Id("b"))), VarDecl("d", None, BinaryOp("+", Id("c"), IntLiteral(3))), VarDecl("e", None, BinaryOp("+", Id("d"), IntLiteral(4))), VarDecl("f", None, BinaryOp("+", Id("e"), FloatLiteral(5.0)))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_092(self):
        """
var a = 1;
var b = 2;
var c = a + b;
var d = c + 3;
var e = d + 4;
var f = e + "string";
        """
        input = Program([VarDecl("a", None, IntLiteral(1)), VarDecl("b", None, IntLiteral(2)), VarDecl("c", None, BinaryOp("+", Id("a"), Id("b"))), VarDecl("d", None, BinaryOp("+", Id("c"), IntLiteral(3))), VarDecl("e", None, BinaryOp("+", Id("d"), IntLiteral(4))), VarDecl("f", None, BinaryOp("+", Id("e"), StringLiteral("string")))])
        expect = "Type Mismatch: BinaryOp(Id(e),+,StringLiteral(string))\n"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_093(self):
        """
var a int; 
type b struct {c:int;}; 
func (x b) a() {
       x.c += 1;
}; 
func (x b) c() {
       x.c += 2;
}; 
        """
        input = Program([VarDecl("a", IntType(), None), StructType("b", [("c", IntType())], []), MethodDecl("x", Id("b"), FuncDecl("a", [], VoidType(), Block([Assign(FieldAccess(Id("x"), "c"), BinaryOp("+", FieldAccess(Id("x"), "c"), IntLiteral(1)))]))), MethodDecl("x", Id("b"), FuncDecl("c", [], VoidType(), Block([Assign(FieldAccess(Id("x"), "c"), BinaryOp("+", FieldAccess(Id("x"), "c"), IntLiteral(2)))])))])
        expect = "Redeclared Method: c\n"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_094(self):
        """
var a = 1;
var b = 2;
var c = a + b;
var d = c + 3;
var e = d + 4;
var f = e + 5.0;
var g = f + h;
        """
        input = Program([VarDecl("a", None, IntLiteral(1)), VarDecl("b", None, IntLiteral(2)), VarDecl("c", None, BinaryOp("+", Id("a"), Id("b"))), VarDecl("d", None, BinaryOp("+", Id("c"), IntLiteral(3))), VarDecl("e", None, BinaryOp("+", Id("d"), IntLiteral(4))), VarDecl("f", None, BinaryOp("+", Id("e"), FloatLiteral(5.0))), VarDecl("g", None, BinaryOp("+", Id("f"), Id("h")))]);
        expect = "Undeclared Identifier: h\n"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_095(self):
        """
func foo(a int) {

      foo(1);

      var foo = 1;

      foo(2); // error

 }
        """
        input = Program([FuncDecl("foo", [ParamDecl("a", IntType())], VoidType(), Block([FuncCall("foo", [IntLiteral(1)]), VarDecl("foo", None, IntLiteral(1)), FuncCall("foo", [IntLiteral(2)])]))])
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_096(self):
        """
var a int;

type a struct {

name: string

}
        """
        input = Program([VarDecl("a", IntType(), None), StructType("a", [("name", StringType())], [])])
        expect = "Redeclared Type: a\n"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_097(self):
        """
var a = 1;
type ID struct {
    a int;
};
func (x ID) foo(x, c int) {
    x.a += 1;
}
        """
        input = Program([VarDecl("d", None, IntLiteral(1)), StructType("ID", [("a", IntType())], []), MethodDecl("x", Id("ID"), FuncDecl("foo", [ParamDecl("x", IntType()), ParamDecl("c", IntType())], VoidType(), Block([Assign(FieldAccess(Id("x"), "a"), BinaryOp("+", FieldAccess(Id("x"), "a"), IntLiteral(1)))])))])
        expect = "Type Mismatch: FieldAccess(Id(x),a)\n" # since the scope of the body inside the scope of parameter => x in body will be the parameter x
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_098(self):
        """
func foo() {
    var a = foo
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,Id("foo"))]))])
        expect = "Undeclared Identifier: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_099(self):
        """
func main() {
    const a = 3
    var arr [2]int = [a]int{1, 2, 3}
    return
}
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([ConstDecl("a", None, IntLiteral(3)), VarDecl("arr", ArrayType([IntLiteral(2)], IntType()), ArrayLiteral([Id("a")], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)])), Return(None)]))])
        expect = "Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(2)]),ArrayLiteral([Id(a)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_100(self):
        """
const b = "no";
func main(a [b]int) { return; }
        """
        input = Program([ConstDecl("b", None, StringLiteral("no")), FuncDecl("main", [ParamDecl("a", ArrayType([Id("b")], IntType()))], VoidType(), Block([Return(None)]))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 499))