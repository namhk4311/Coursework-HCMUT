import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_parser_1(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))

    def test_parser_2(self):
        """More complex program"""
        input = """func foo () {
            var x int = 2;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,302))
    
    def test_parser_3(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,303))
    def test_parser_4(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,304))
    def test_parser_5(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,305))
    
    def test_parser_6(self): 
        input = "const a = 1\n" ### must have newline or semicolon + newline
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,306))
    def test_parser_7(self):
        input = "const b = true;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,307))
    def test_parser_8(self):
        input = "const c = [2][0]string{1, \"Hello\"};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,308))
    def test_parser_9(self):
        input = "const d = [1.]ID{1, 3};"
        expect = "Error on line 1 col 12: 1."
        self.assertTrue(TestParser.checkParser(input,expect,309))
    def test_parser_10(self):
        input = """const student1 = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,310))

### 11 - 20: Test Declaration:
    def test_parser_11(self):
        input = """
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z STR;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,311))
    def test_parser_12(self):
        input = """const c = a.b() + 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,312))
    def test_parser_13(self):
        input = """
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;}         
            func VoTien2() {return;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,313))
    def test_parser_14(self):
        input = """
            type Person struct {
                name string ;
                age int ;
                ID string ;                     
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,314))
    def test_parser_15(self):
        input = """
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,315))
    def test_parser_16(self):
        input = """
            func Main() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const p = a.b() + 2;
            } 
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,316))
    def test_parser_17(self):
        input = """func ComputeArea(rect Rectangle) float {
            return rect.width * rect.height;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,317))
    def test_parser_18(self):
        input = """var flag boolean = true;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,318))
    def test_parser_19(self):
        input = """const e = 2.7182818284;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,319))
    def test_parser_20(self):
        input = """type Circle struct {
            radius float;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,320))

### 21 - 30: Test Statement:
    def test_parser_21(self):
        input = """func Divide(a float, b float) float {
            if (b == 0) {
                return -1;
            }
            return a / b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,321))
    def test_parser_22(self):
        input = """
            func Main() {
                if (x > 0) {
                    var a = 1;
                } else {
                    var b = 2;
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,322))
    def test_parser_23(self):
        input = """
            func Main() {
                for i := 0; i < 10; i += 1 {
                    break;
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,323))
    def test_parser_24(self):
        input = """
            func Main() {
                for _, val := range arr {
                    var b = 1;
                    continue;
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,324))
    def test_parser_25(self):
        input = """
            func Main() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,325))
    def test_parser_26(self):
        input = """
            func Main() {
                if (x > 10 && y < 10 && z > 100) {return;} 
                if (x > 10) {
                    return 0;
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,326))
    def test_parser_27(self):
        input = """
            func Main() {
                for i < 20 {break;}
                for i := 0; i < 20; i += 2 {continue;}
                for index, value := range arr {break;}
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,327))
    def test_parser_28(self):
        input = """
            func Main() {
                for i < 10 {
                    break;
                }
            
                foo(2 + x, 4 / y); m.goo();
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,328))
    def test_parser_29(self):
        input = """
            func Main() {
                for _, val := range arr {
                    for i < 10 {
                        for i < 20 {break;}
                        for i := 0; i < 20; i += 2 {break;}
                        for index, value := range arr {break;}
                    }
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,329))

    def test_parser_30(self):
        input = """
            func Main() {
                for _, val := range arr {
                    for i < 10 {
                        if (x > 10) {
                            break;
                        } else if (x == 10) {
                            continue;
                        } else {
                            return 0;
                        }
                    }
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,330))

### 31 - 40: Test Expression
    def test_parser_31(self):
        input = """var z Myname = [2]int{};"""
        expect = "Error on line 1 col 23: }"
        self.assertTrue(TestParser.checkParser(input,expect,331))

    def test_parser_32(self):
        input = """var a Myname = ID {b: 5};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,332))

    def test_parser_33(self):
        input = """var z [10][10][10]int = a[2][3][(b + 2) * (c + 3)];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,333))

    def test_parser_34(self):
        input = """const k = -a + -!-!c - ---[3]int{1};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,334))

    def test_parser_35(self):
        input = """const myVariable = a.b.c();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,335))

    def test_parser_36(self):
        input = """const myVariable = a.foo(123) + b.c[2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,336))

    def test_parser_37(self):
        input = """const myVariable = 1 || 2 && a + 5 / 2 - -1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,337))

    def test_parser_38(self):
        input = """
            var a = a[2].b; 
            var a = "s";
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,338))

    def test_parser_39(self):
        input = """
            const myVariable = a.b.c();
            const k = -a + -!-!c - ---[3]int{1};
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,339))


    def test_parser_40(self):
        input = """
            const z = a[2][3][(b + 2) * (c + 3)];
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,340))

### 41 - 50: Test declaration + statement
    def test_parser_41(self):
        input = """
            func Main() {
                const myConst = foo( 1.0,true,false,nil,\"votien\" );
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,341))
    
    def test_parser_42(self):
        input = """
            const myConst1 = foo(1+2-3 && 5--1); 
            func Main() {
                const myConst2 = foo( 1.0,true,false,nil,\"votien\" );
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,342))

    def test_parser_43(self):
        input = """
            const myConst1 = foo(1+2-3 && 5--1); 
            func Main() {
                const myConst2 = foo( 1.0,true,false,nil,\"votien\" );
            }
            const myConst3 = foo( a > b <= c );
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,343))

    def test_parser_44(self):
        input = """
            const myConst = foo(a.b.c.d);
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,344))

    def test_parser_45(self):
        input = """
            const myConst = foo(a[2][3]);
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,345))

    def test_parser_46(self):
        input = """
            const myConst = foo(a(),b.a(2, 3));
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,346))

    def test_parser_47(self):
        input = """
            const myConst = foo( Device{}, Calculator {a: 1} );
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,347))

    def test_parser_48(self):
        input = """
            const myConst = foo( [1]int{1}, [1][1]int{2, \"String\"} );
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,348))

    def test_parser_49(self):
        input = """
            func Main() {
                var myVar = foo(2 + x, 4 / y);
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,349))

    def test_parser_50(self):
        input = """
            func votien() {
                var a int = foo(2 + x, 4 / y);
                const a = nil;
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,350))


### 51 - 60: Test statement
    def test_parser_51(self):
        input = """
            func foo(){
                foo();
                foo(foo(), 2);
                a.foo();
                a[2].c.foo(foo(), 2);
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,351))

    def test_parser_52(self):
        input = """
            func Main() {
                a.b.c.d.foo();
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,352))

    def test_parser_53(self):
        input = """
            func Main() {
                var x int = 10;
                var y int = 11;
                var z int = 12;
                if (x > 10 && y < 10 && z > 100) {return;} 
                if (x < 10) {
                    y += 11;
                    z += 12;
                } else if (x == 10) {
                    x += 10;
                } else {
                    x := 0;
                    y := 0;
                    z := 0;
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,353))

    def test_parser_54(self):
        input = """
            func Main() {
                var x int = 10;
                var y int = 11;
                var z int = 12;
                if (x > 10 && y < 10 && z > 100) {
                    a.b.c.d.m.goo()
                } 
                if (x < 10) {
                    for i := 0; i < 10; i += 1 {
                        y += 11;
                        z += 12;
                        break;
                    }
                } else if (x == 10) {
                    for n := 0; n < 100; n *= 2 {
                        x += 10;
                        continue;
                    } 
                } else {
                    x := 0;
                    y := 0;
                    z := 0;
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,354))

    def test_parser_55(self):
        input = """
            func Add(a int, b int) int {
                return a + b;
            }

            func Main() {
                var a = 1;
                var b = 2;
                var c = Add(a, b);
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,355))

    ### statement + declare
    def test_parser_56(self):
        input = """
            type Calculator interface {
                Add(a, b int) int;
                Sub(a, b float) float;
                Mul(a, b float) float;
                Div(a, b float) float; 
            }

            func (c Calculator) Add(a int, b int) {
                return c.add(a, b);
            } 

            func (c Calculator) Sub(a int, b int) {
                return c.Sub(a, b);
            } 
            func (c Calculator) Mul(a int, b int) {
                return c.Mul(a, b);
            } 
            func (c Calculator) Div(a int, b int) {
                return c.Div(a, b);
            } 

            func Main() {
                return;
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,356))


    def test_parser_57(self):
        input = """
            func Main() {
                var a int = 0;
                for i := 0; i < 10; i +=1 {
                    for j := 0; j < 11; j += 1 {
                        for k := 0; k < 12; k += 1 {
                            a += 1;
                        }
                    }
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,357))


    def test_parser_58(self):
        input = """
            func Main() {
                const array = [1][3]float{1.};
                var sum;
                for index, value := range array {
                    sum += value * i;
                }
            }
"""
        expect = "Error on line 4 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,358))

    def test_parser_59(self):
        input = """
            func Main() {
                const array = [1][3]float{1.};
                var sum_value int;
                var sum_index = 0;
                for index, value := range array {
                    sum_index += index
                    for i := 0; i < sum_index; i += 1 {
                        sum_value += value;
                    }
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,359))

    def test_parser_60(self):
        input = """
            func Main() {
                a[1 + 1] := 1;
                a[2].b.c[2] := 1;
                a.b.c.d.foo();
                const a = a.b().c().d();
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,360))

### 61 - 70: Test Declaration
    def test_parser_61(self):
        input = """
           type Person struct {
                CID string;
                name string;
                age int;
                addresss string;                 
            }

            func main() {
                const person1 = Person{name: \"John\", age: 40, address: \"New York City\"}
                const person2 = Person{}
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,361))
    
    def test_parser_62(self):
        input = """
            type Calculation struct {
                value int;
            }

            func (c Calculator) Add(x int) int {
                c.value += x;
                return c.value;
            }

            func Main() {
                const cal = Calculator{value: 0}
                cal.Add(5);
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,362))

    def test_parser_63(self):
        input = """
            type Car interface {
                Run(velocity float);
                Brake();
                Color() [3]color;
                Speed();
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,363))

    def test_parser_64(self):
        input = """
            func (c MyStruct) myFunc(x int) int {
                return
            }  
            func (c MyStruct) myFunc() ID {return;}      
            func (c MyStruct) myFunc(x int, y [2]myFunc) {return;}  
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,364))


    def test_parser_65(self):
        input = """
            func Main() {
                var a = var b;
            }
"""
        expect = "Error on line 3 col 25: var"
        self.assertTrue(TestParser.checkParser(input,expect,365))

    def test_parser_66(self):
        input = """
            func Main() {
                var a = person{name: \"John\", age: 40};
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,366))

    def test_parser_67(self):
        input = """
            func main() {
                const a = a[2][3].foo(2 + 3, a {a:2});
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,367))

    def test_parser_68(self):
        input = """
            func Main() {
                const b = b[1.2][2].foo(5, b {c: 5});
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,368))

    def test_parser_69(self):
        input = """
            func Main() {
                func abc() {
                    return 1;
                }
            }
"""
        expect = "Error on line 3 col 17: func"
        self.assertTrue(TestParser.checkParser(input,expect,369))

    def test_parser_70(self):
        input = """
            func abc() int {
                return 1;
            }

            func def() string {
                return "Hello";
            }
        
            func Main() {
                return "hello";
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,370))

### 71 - 80: literal + statement
    def test_parser_71(self):
        input = """
            func Main() {
                2 + 2 += 2;
            }
"""
        expect = "Error on line 3 col 17: 2"
        self.assertTrue(TestParser.checkParser(input,expect,371))

    def test_parser_72(self):
        input = """
            func Main() {
                ID {id:2}.c += 2;
            }
"""
        expect = "Error on line 3 col 20: {"
        self.assertTrue(TestParser.checkParser(input,expect,372))

    def test_parser_73(self):
        input = """
            func Main() {
                if (x.foo().b[2]) {
                    if (1){
                        x := 1;
                    } else {
                        x := 2;
                    }

                } else if(2) {
                    x += 3;
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,373))

    def test_parser_74(self):
        input = """
            func Main() {
                a[2].b := 2;     
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,374))

    def test_parser_75(self):
        input = """
            func Main() {
                const a = a[2].b
                var a = a[2].b; var a = "s"; 
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,375))

    def test_parser_76(self):
        input = """
            func Main() {
                const a = a[2.1].b
                var a = a[2.].b; var a = "s"; 
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,376))

    def test_parser_77(self):
        input = """
            func Main() {
                for index, value := range 10 {
                    return "Hello";
                }
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,377))

    def test_parser_78(self):
        input = """
            func Main() {
                a.foo() += 2;
            }
"""
        expect = "Error on line 3 col 25: +="
        self.assertTrue(TestParser.checkParser(input,expect,378))

    def test_parser_79(self):
        input = """
            func Main() {
                a[(2 + 3) * (4 + 5)][b + c * d].foo(2 + 3, a {a:2})
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,379))

    def test_parser_80(self):
        input = """
            func Main() {
                if (i == 5) {
                    a + b += 2;
                }
            }
"""
        expect = "Error on line 4 col 23: +"
        self.assertTrue(TestParser.checkParser(input,expect,380))

### 81 - 90: Test Declare        
    def test_parser_81(self):
        input = """

"""
        expect = "Error on line 3 col 1: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,381))

    def test_parser_82(self):
        input = """
            func (c c) Add(x, c int) {
                return x + c;
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,382))

    def test_parser_83(self):
        input = """
            func (c c) Add(x int) {return;};
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,383))

    def test_parser_84(self):
        input = """
            func Add(x int, y int) int {};
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,384))

    def test_parser_85(self):
        input = """
            type Calculator struct {
                c Calculator
                c Cal a int;         
            }
"""
        expect = "Error on line 4 col 23: a"
        self.assertTrue(TestParser.checkParser(input,expect,385))

    def test_parser_86(self):
        input = """
            const ab = x +;
"""
        expect = "Error on line 2 col 27: ;"
        self.assertTrue(TestParser.checkParser(input,expect,386))

    def test_parser_87(self):
        input = """
            const ab = (x > y) && (z < t) || (m + n)
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,387))

    def test_parser_88(self):
        input = """
            type Calculator struct {
                value int
            }
            func (c) Sub(x int) int {
                c.value += x;
                return c.value;
            }
"""
        expect = "Error on line 5 col 20: )"
        self.assertTrue(TestParser.checkParser(input,expect,388))

    def test_parser_89(self):
        input = """
            func Add(x int, y) int {
                return x + y;
            }
"""
        expect = "Error on line 2 col 30: )"
        self.assertTrue(TestParser.checkParser(input,expect,389))

    def test_parser_90(self):
        input = """
            const ab = 1,2,3;            
"""
        expect = "Error on line 2 col 25: ,"
        self.assertTrue(TestParser.checkParser(input,expect,390))

### 91 - 100: Statement:
    def test_parser_91(self):
        input = """
            func main() {
                a[2][3] := b[2] + 1;
            }            
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,391))

    def test_parser_92(self):
        input = """
            func main() {
                person.name := "John";
                person.age := 30;          
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,392))

    def test_parser_93(self):
        input = """
            func main() {
                arr := [3]int{10, 20, 30}
                marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}          
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,393))

    def test_parser_94(self):
        input = """
            func main() {
                str1 := "Hello"
                str2 := "World"
                str3 := str1 + " " + str2 // str3 == "Hello World"
            }          
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,394))

    def test_parser_95(self):
        input = """
            func main() {
                str4 := "apple"
                str5 := "banana"
                result := str4 == str5 // result == false
            }        
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,395))

    def test_parser_96(self):
        input = """
            func main() {
                arr := [3]int{10, 20, 30}
                for index, value := range arr {
                    // index: 0, 1, 2
                    // value: 10, 20, 30
                    return "Hello";
                }
            }            
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,396))

    def test_parser_97(self):
        input = """
            func main() {
                arr := [3]int{10, 20, 30}
                for _, value := range arr {
                    // value: 10, 20, 30
                    return "Hi";
                }
            }           
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,397))

    def test_parser_98(self):
        input = """
            func main() {
                for i := 0; i < 10; i+=1 {
                    if (i == 5) {
                        break;
                    }
                    // other statements
                }
            }           
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,398))

    def test_parser_99(self):
        input = """
            func main() {
                for var i = 0; i < 10; i += 1 {
                    if (i == 5) {
                        a := goo(1 + 1, a.goo())
                        continue;
                    }
                    // statements that will not execute when i == 5
                }                          
                for _, value := range array {
                    break
                }                          
            }          
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,399))

    def test_parser_100(self):
        input = """
            type Calculator struct {
                value int;
            }
            
            func (c Calculator) Add(x int) int {
                c.value += x;
                return c.value;
            }          

            func main() {
                var calculator = Calculator{value: 0};
                calculator.add(3, 4)
                calculator.reset()
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,400))
    
