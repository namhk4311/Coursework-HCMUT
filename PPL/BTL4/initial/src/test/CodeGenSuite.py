import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_001(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_002(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_003(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_004(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_005(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_006(self):
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    ## fix here
    def test_007(self):
        input = """
func fvoid() {putStringLn("ABC");}

var global = fint()
func main() {
    fvoid();
    putFloatLn(global + 2.0)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

};

func fint() int {return 1;}
"""
        expect = "ABC\n3.0\ntrue\nac\n"
        self.assertTrue(TestCodeGen.test(input,expect,507))


    def test_008(self): # test_016
        input = """
func main() {
    putIntLn(5 % 2)
    putIntLn(2 % 5)
}
"""
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_009(self): # test_019
        input = """
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        expect = "true\nfalse\ntrue\ntrue\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_010(self): # test_024
        input = """
func main() {
    putBoolLn(! true)
    putBoolLn(! false)
    putIntLn(-1)
    putFloatLn(-1.0)
}
"""
        expect = "false\ntrue\n-1\n-1.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_011(self): ## test_032
        input = """
func foo() int {return 1;}

func main() {
    putInt(foo())
}
"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_012(self): # test_037
        input = """
var a = 1;
func main() {
    b := a + 1;
    putInt(a)
    putInt(b)
}
"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_013(self): # test_044
        input = """
func main() {
    var f = true;
    var g boolean;

    putBoolLn(f)
    putBool(g)
}
"""
        expect = "true\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_014(self): # test_047
        input = """
func main() {
    a := 50
    putInt(a)
}
"""
        expect = "50"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_015(self): # test_051
        input = """
func foo() int {return foo1();}
var a = foo() + foo1();
func main() {
    putInt(a)
    a := foo()
    putInt(a)
}
func foo1() int {return 1;}
"""
        expect = "21"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_016(self): # test_090
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,516))


    def test_017(self): # test_091
        input = """
func main() {
    var a [1][1][1] int  = [1][1][1] int {{{0}}};
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_018(self): # test_055
        input = """
            func main() {
                var a [2][3] int = [2][3] int {{10, 20, 30}, {40, 50, 60}};
                putInt(a[1][0])
            }
"""
        expect = "40"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_019(self): # test_057
        input = """
            func main() {
                var a [2] int;
                putInt(a[0])
                putInt(a[1])
            }
"""
        expect = "00"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_020(self): # test_059
        input = """
            func main() {
                var a [2][3][2] int ;
                putInt(a[0][0][0])
            }
"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_021(self): # test_061
        input = """
            func main() {
                var a [2] int;
                a[0] := 100
                a[1] += a[0] + a[0]
                putInt(a[1])
            }
"""
        expect = "200"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_022(self): # test_065
        input = """
            func main() {
                var a [2][3] float;
                a[0][0] += 2.0
                putFloat(a[0][0] + a[0][1])
            }
"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_023(self): # test_077
        input = """
    var a [2] int;
    func main() {
        a[0] := 100
        a[1] += a[0] + a[0]
        putInt(a[1])
    }
"""
        expect = "200"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_024(self): # test_085
        input = """
            func createArray() [3] int {
                return [3] int {10, 20, 30};
            }

            func main() {
                var a [3] int = createArray();
                putInt(a[0]);
                putInt(a[1]);
                putInt(a[2]);
            }
"""
        expect = "102030"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_025(self): # test_092
        input = """
            func main() {
                var a [2][2] float ;
                a[1][0] := 10
                putFloat(a[1][0]);
            }
"""
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,525))


    def test_026(self): # test_096
        input = """
func main() {
    if (true) {
        putBool(true)
    }
}
    """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    # start here

    def test_027(self): # test_097
        input = """
func main() {
    if (true) {
        putBool(true)
    } else {
        putBool(false)
    }
}
    """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_028(self): # test_098
        input = """
func main() {
    if (false) {
        putBool(true)
    } else {
        putBool(false)
    }
}
    """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_029(self): # test_113
        input = """
func main() {
    var i = 0;
    for i < 3 {
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_030(self): # test_114
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_031(self): # test_115
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        expect = "1355"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_032(self): # test_126
        input = """
func main() {
    var i int = 10;
    for var i int = 0; i < 2; i += 1 {
        putIntLn(i)
        break;
    }
    putInt(i)
}
        """
        expect = "0\n10"
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_033(self): # test_127
        input = """
    const a = 1 + 1
    const c = 5 - a
    func main() {
    var b [a][c] int;
    putInt(b[0][0]);
    b[0][0] := 20;
    putInt(b[0][0]);
    }
        """
        expect = "020"
        self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_034(self): # test_125
        input = """
            func main() {
                var i int = 10;
                for var i int = 0; i < 2; i += 1 {
                    putIntLn(i)
                }
                putInt(i)
            }

"""
        expect = "0\n1\n10"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_035(self): # test_130
        input = """
            const a = "ABC"
            func main() {
                putString(a)
            }
"""
        expect = "ABC"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_036(self): # test_136
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
"""
        expect = "020"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_037(self): # test_140
        input = """
            const a = [2] int {2,3}
            func main() {
                var c = a[0];
                var d = a[1];
                var b [c][d] int;
                putInt(b[0][0]);
                b[0][0] := 20;
                putInt(b[0][0]);
            }
"""
        expect = "020"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_038(self): # test_141
        input = """
type Course interface {study();}
type PPL3 struct {number int;}
func (p PPL3) study() {putInt(p.number);}

func main(){
    var a PPL3 = PPL3 {number: 10}
    putIntLn(a.number)
    a.study()
}
        """
        expect = "10\n10"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_039(self): # test_142
        input = """
type Course interface {study();}
type PPL3 struct {number int;}
func (p PPL3) study() {putInt(p.number);}

func main(){
    var a Course = nil
    a := PPL3 {number: 10}
    a.study()
}
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_040(self): # test_143
        input = """
type PPL3 struct {number int;}

func main(){
    var a PPL3 = PPL3 {number: 10}
    putInt(a.number)
}
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_041(self): # test_144
        input = """
type PPL3 struct {number int;}

func main(){
    var a PPL3
    a.number := 10
    putInt(a.number)
}
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_042(self): # test_145
        input = """
type PPL2 struct {number int;}
type PPL3 struct {number int; ppl PPL2;}

func main(){
    var a PPL3
    a.ppl := PPL2 {number: 10}
   putInt(a.ppl.number)
}
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,542))

    def test_043(self): # test_146
        input = """
type PPL2 struct {number int;}
type PPL3 struct {number int; ppl PPL2;}

func main(){
    var a PPL3
    a.ppl := PPL2 {number: 10}
    a.ppl.number := 100
   putInt(a.ppl.number)
}
        """
        self.assertTrue(TestCodeGen.test(input, "100", 543))

    # start here 2

    def test_044(self): # test_147
        input = """
type Study interface { study(); }
type Play interface { play(); }

type PPL3 struct {number int;}

func (p PPL3) study() { putInt(p.number); }
func (p PPL3) play()  { putInt(p.number + 5); }

func main() {
    var a PPL3 = PPL3 {number: 1}
    a.study()
    a.play()
}
        """
        self.assertTrue(TestCodeGen.test(input, "16", 544))


    def test_045(self): # test_148
        input = """
type Study interface { study(); }
type Play interface { play(); }

type PPL3 struct {number int;}

func (p PPL3) study() { putInt(p.number); }
func (p PPL3) play()  { putInt(p.number + 5); }

func main() {
    var a PPL3 = PPL3 {number: 1}
    var b Study = a
    var c Play = a
    b.study()
    c.play()
}
        """
        self.assertTrue(TestCodeGen.test(input, "16", 545))

    def test_046(self): # test_149
        input = """
type Worker interface {
    study();
    play();
}

type PPL4 struct {number int;}
type PPL5 struct {number int;}

// Implement Worker cho PPL4
func (p PPL4) study() { putInt(p.number); }
func (p PPL4) play()  { putInt(p.number + 5); }

// Implement Worker cho PPL5
func (p PPL5) study() { putInt(p.number * 2); }
func (p PPL5) play()  { putInt(p.number * 3); }

func main() {
    var w1 Worker = PPL4 {number: 3}
    var w2 Worker = PPL5 {number: 4}

    w1.study(); // in: 3
    w1.play();  // in: 8

    w2.study(); // in: 8
    w2.play();  // in: 12
}
        """
        self.assertTrue(TestCodeGen.test(input, "38" "812", 546))

    def test_047(self): # test_150
        input = """
type Worker interface {
    study();
    play();
}

type PPL4 struct {number int;}
type PPL5 struct {number int;}

// Implement Worker cho PPL4
func (p PPL4) study() { putInt(p.number); }
func (p PPL4) play()  { putInt(p.number + 5); }

// Implement Worker cho PPL5
func (p PPL5) study() { putInt(p.number * 2); }

func main() {
    var w1 Worker = PPL4 {number: 3}
    var w2 PPL5 = PPL5 {number: 4}

    w1.study(); // in: 3
    w1.play();  // in: 8

    w2.study(); // in: 8
}
        """
        self.assertTrue(TestCodeGen.test(input, "38" "8", 547))


    def test_048(self): # test_151
        input = """
type Speaker interface { speak(); }

type Human struct {name int; }

func (h Human) speak() { putIntLn(h.name); }

func saySomething(s Speaker) {
    s.speak();
}

func main() {
    var h Speaker = Human {name: 2025};
    saySomething(h);
}
        """
        self.assertTrue(TestCodeGen.test(input, "2025\n", 548))


    def test_049(self): # test_152
        input = """
type Speaker interface { speak(); }

type Human struct { name int; }

func (h Human) speak() { putIntLn(h.name); }

func main() {
    var people [3]Speaker;

    people[0] := Human {name: 1};
    people[1] := Human {name: 2};
    people[2] := Human {name: 3};

    people[0].speak(); // Output: 1
    people[1].speak(); // Output: 2
    people[2].speak(); // Output: 3
}
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n3\n", 549))

    def test_050(self): # test_153
        input = """
type Speaker interface { speak(); }

type Human struct { name int; }

func (h Human) speak() { putIntLn(h.name); }

func main() {
    var people [3]Human;

    people[0] := Human {name: 1};
    people[1] := Human {name: 2};
    people[2] := Human {name: 3};

    people[0].speak(); // Output: 1
    people[1].speak(); // Output: 2
    people[2].speak(); // Output: 3
}
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n3\n", 550))

    def test_051(self): # test_154
        input = """
type Calculator struct { x int; y int; }

func (c Calculator) sum() int {
    return c.x + c.y;
}

func main() {
    var cal Calculator = Calculator {x: 7, y: 8};
    var result int = cal.sum();
    putIntLn(result);
}
        """
        self.assertTrue(TestCodeGen.test(input, "15\n", 551))

    def test_052(self): # test_155
        input = """
type Calculator interface { sum() int; }

type BasicCalc struct { x int; y int; }

func (b BasicCalc) sum() int {
    return b.x + b.y;
}

func main() {
    var c Calculator = BasicCalc {x: 5, y: 15};
    var result int = c.sum();
    putIntLn(result);
}
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", 552))

    def test_053(self): # test_156
        input = """
type Speaker interface { speak(); }

type Human struct { name int; }

func (h Human) speak() { putIntLn(h.name); }

func sayHello(s Speaker) {
    s.speak();
}

func main() {
    var h Human = Human {name: 100};
    sayHello(h);
}
        """
        self.assertTrue(TestCodeGen.test(input, "100\n", 553))

    # start here 3

    def test_054(self): # test_157
        input = """
type Calculator interface { sum() int; }

type BasicCalc struct { x int; y int; }

func (b BasicCalc) sum() int {
    return b.x + b.y;
}

func calculate(c Calculator) int {
    return c.sum();
}

func main() {
    var b BasicCalc = BasicCalc {x: 20, y: 30};
    var result int = calculate(b);
    putIntLn(result);
}
        """
        self.assertTrue(TestCodeGen.test(input, "50\n", 554))

    def test_055(self): # test_158
        input = """
type Multiplier struct { factor int; }

func (m Multiplier) multiply(value int) int {
    return m.factor * value;
}

func main() {
    var mul Multiplier = Multiplier {factor: 5};
    var result int = mul.multiply(4);
    putIntLn(result);
}
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", 555))

    def test_056(self): # test_159
        input = """
type Calculator interface { calculate(a int, b int) int; }

type BasicCalc struct {number int;}

func (b BasicCalc) calculate(a int, b int) int {
    return a + b;
}

func main() {
    var c Calculator = BasicCalc {};
    var result int = c.calculate(15, 25);
    putIntLn(result);
}
        """
        self.assertTrue(TestCodeGen.test(input, "40\n", 556))


    def test_057(self): # test_160
        input = """
type Calculator interface { calculate(a int, b int); }

type BasicCalc struct {number int;}

func (b BasicCalc) calculate(a int, b int) {
    putIntLn(a+b);
}

func main() {
    var c Calculator = BasicCalc {};
    c.calculate(15, 25);
}
        """
        self.assertTrue(TestCodeGen.test(input, "40\n", 557))

    def test_058(self): # test_161
        input = """
type Calculator interface { calculate(a int, b int); }

type BasicCalc struct {number int;}

func (b BasicCalc) calculate(a int, b int) {
    putIntLn(a+b);
}

func main() {
    var c BasicCalc
    c.calculate(15, 25);
}
        """
        self.assertTrue(TestCodeGen.test(input, "40\n", 558))

    def test_059(self): # test_162
        input = """
type Speaker interface { speak(); }

type Human struct { name int; }

func (h Human) speak() {
    putIntLn(h.name);
}

type Classroom struct {
    student Human;
    guest Speaker;
}

func main() {
    var h Human = Human {name: 777};
    var k Speaker = Human {name: 999};
    var room Classroom = Classroom {student: h, guest: k};

    putIntLn(room.student.name);
    room.guest.speak();
}
        """
        expect = "777\n999\n"
        self.assertTrue(TestCodeGen.test(input, "777\n999\n", 559))

    def test_060(self): # test_163
        input = """
    type Person struct {
        name string;
        age int;
    }
    func main() {
        var p Person = Person{name: "Alice", age: 22};
        putStringLn(p.name);
        putIntLn(p.age);
    }
        """
        self.assertTrue(TestCodeGen.test(input, "Alice\n22\n", 560))

    def test_061(self): # test_164
        input = """
    type Greeter interface { greet(); }

    type Person struct {
        name string;
        age int;
    }
    func (p Person) greet() {
        putStringLn(p.name);
    }

    func main() {
        var g Greeter = Person{name: "Bob", age: 30};
        g.greet();
    }
        """
        self.assertTrue(TestCodeGen.test(input, "Bob\n", 561))

    def test_062(self): # test_165
        input = """
    type Person struct {
        name string;
        age int;
    }
    func (p Person) agePlus(n int) int {
        return p.age + n;
    }
    func main() {
        var p Person = Person{name: "Charlie", age: 18};
        var result int = p.agePlus(5);
        putIntLn(result);
    }
        """
        self.assertTrue(TestCodeGen.test(input, "23\n", 562))

    def test_063(self): # test_166
        input = """
    type Person struct {
        name string;
        age int;
    }
    func sumAges(p1 Person, p2 Person) int {
        return p1.age + p2.age;
    }
    func main() {
        var p1 Person = Person{name: "Dan", age: 20};
        var p2 Person = Person{name: "Eve", age: 25};
        var total int = sumAges(p1, p2);
        putIntLn(total);
    }
        """
        self.assertTrue(TestCodeGen.test(input, "45\n", 563))

    def test_064(self): # test_167
        input = """
    type Person struct {
        name string;
        age int;
    }
    func (p Person) printInfo() {
        putStringLn(p.name);
        putIntLn(p.age);
    }
    func main() {
        var people [1]Person
        people[0] := Person{name: "Anna", age: 19};
        people[0].printInfo()
    }
        """
        self.assertTrue(TestCodeGen.test(input, "Anna\n19\n", 564))

    def test_065(self): # test_168
        input = """
    type Speaker interface { speak(); }
    type Person struct {
        name string;
        age int;
    }
    func (p Person) speak() {
        putStringLn(p.name);
    }
    func announce(s Speaker) {
        s.speak();
    }
    func main() {
        var p Person = Person{name: "Grace", age: 27};
        announce(p);
    }
        """
        self.assertTrue(TestCodeGen.test(input, "Grace\n", 565))

    def test_066(self): # test_169
        input = """
    type Person struct {
        name string;
        age int;
    }
    func createPerson(n string, a int) Person {
        return Person{name: n, age: a};
    }
    func main() {
        var p Person = createPerson("Helen", 24);
        putStringLn(p.name);
        putIntLn(p.age);
    }
        """
        self.assertTrue(TestCodeGen.test(input, "Helen\n24\n", 566))

    def test_067(self): # test_170
        input = """
    type Person struct {
        name string;
        age int;
    }
    func (p Person) isAdult() boolean {
        return p.age >= 18;
    }
    func main() {
        var p Person = Person{name: "Ivy", age: 17};
        if (p.isAdult()) {
            putStringLn("Adult");
        } else {
            putStringLn("Minor");
        }
    }
        """
        self.assertTrue(TestCodeGen.test(input, "Minor\n", 567))

    def test_068(self): # test_171
        input = """
    type Person struct {
        name string;
        age int;
    }
    func (p Person) duplicate() Person {
        return Person{name: p.name, age: p.age};
    }
    func main() {
        var p1 Person = Person{name: "Jack", age: 31};
        var p2 Person = p1.duplicate();
        putStringLn(p2.name);
        putIntLn(p2.age);
    }
        """
        self.assertTrue(TestCodeGen.test(input, "Jack\n31\n", 568))

    def test_069(self): # test_172
        input = """
    type Person struct {
        name string;
        age int;
    }
    func (p Person) printInfo() {
        putStringLn(p.name);
        putIntLn(p.age);
    }
    func main() {
        var people [2]Person = [2]Person{Person{name: "Anna", age: 19},Person{name: "Bill", age: 21}};
        people[0].printInfo();
        people[1].printInfo();
    }
        """
        self.assertTrue(TestCodeGen.test(input, "Anna\n19\nBill\n21\n", 569))

    def test_070(self): # test_174
        input = """
func foo() boolean {
    putStringLn("foo");
    return true;
}

func main() {
    var a = true && foo()
    putBoolLn(a)
    var b = false && foo()
    putBoolLn(b)

}
        """
        self.assertTrue(TestCodeGen.test(input, "foo\ntrue\nfalse\n", 570))

    def test_071(self): # test_175
        input = """
func foo() boolean {
    putStringLn("foo");
    return false;
}

func main() {
    var a = true || foo()
    putBoolLn(a)
    var b = false || foo()
    putBoolLn(b)

}
        """
        self.assertTrue(TestCodeGen.test(input, "true\nfoo\nfalse\n", 571))

    def test_072(self): # test_173
        input = """
var prefix string;

type Person struct {
    name string;
    age int;
}

func getGreeting(name string) string {
    return prefix + name;
}

func (p Person) greet() string {
    return getGreeting(p.name);
}

func main() {
    var ABC Person = Person{name: "ABC", age: 19};
    prefix := "Hello, my name is ";
    var msg string = ABC.greet();
    putStringLn(msg);
}
        """
        self.assertTrue(TestCodeGen.test(input, "Hello, my name is ABC\n", 572))

    def test_073(self): # test_176
        input = """
type Course interface {print(a [2] int);}
type PPL3 struct {number int;}
func (p PPL3) print(a [2] int) {putInt(a[0]);}

func main(){
    var a PPL3 = PPL3 {number: 10}
    a.print([2] int {10, 2})
}
        """
        self.assertTrue(TestCodeGen.test(input, "10", 573))

    def test_074(self): # test_177
        input = """
type PPL2 struct {number [1][1][1]int;}
type PPL3 struct {ppl2 PPL2;}


func main(){
    var a [2][2]PPL3
    a[0][1] := PPL3 {ppl2: PPL2 {number: [1][1][1]int{{{10}}} }}
    putInt(a[0][1].ppl2.number[0][0][0])
}
        """
        self.assertTrue(TestCodeGen.test(input, "10", 574))

    def test_075(self): # test_182
        input = """
        const MAX = 5;

        func bfs(graph [MAX][MAX]int, start int){
            var visited [MAX] boolean;
            var queue [MAX] int;
            var front = 0;
            var rear = 0;
            visited[start] := true;
            queue[rear] := start;
            rear += 1;

            for front < rear {
                var u = queue[front]
                front += 1;
                putInt(u)
                putString(" ")
                for v := 0; v < MAX; v += 1{
                    if (graph[u][v] == 1 && !visited[v]){
                        visited[v] := true;
                        queue[rear] := v;
                        rear += 1;
                    }
                }
            }
        }

        func main(){
            var graph = [MAX][MAX] int {{0, 1, 0, 0, 0}, {1, 0, 1, 0, 0}, {0, 1, 0, 1, 0}, {0, 0, 1, 0, 1}, {0, 0, 0, 1, 0}};
            bfs(graph, 0);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0 1 2 3 4 ", 575))

    def test_076(self): # test_183
        input = """
        const MAX = 10;
        
        func generateBinary(arr [MAX]int, n int, index int){
            if (index == n) {
                for i := 0; i < n; i += 1 {
                    putInt(arr[i]);
                }
                putLn();
            } else {
                arr[index] := 0;
                generateBinary(arr, n, index + 1);
                arr[index] := 1;
                generateBinary(arr, n, index + 1);
            }
        }
        
        func main() {
            var n = 3;
            var arr [MAX] int;
            putString("All binary strings of length = ")
            putInt(n)
            putLn()
            generateBinary(arr, n, 0);
        }
        """
        self.assertTrue(TestCodeGen.test(input, """All binary strings of length = 3
000
001
010
011
100
101
110
111
""", 576))

    def test_077(self):
        input = """
        const MAX = 8;
        
        func bubbleSort(arr [MAX]int){
            var i = 0;
            for i < MAX - 1 {
                var j = 0;
                for j < MAX - i - 1 {
                    if (arr[j] > arr[j + 1]) {
                        var temp = arr[j];
                        arr[j] := arr[j + 1];
                        arr[j + 1] := temp;
                    }
                    j += 1;
                }
                i += 1;
            }
        }
        
        func main() {
            var arr = [MAX]int {64, 34, 25, 12, 22, 11, 90, 1};
            bubbleSort(arr);
            for i := 0; i < MAX; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1 11 12 22 25 34 64 90 ", 577))

    def test_078(self):
        input = """
        type Shape interface {
            getArea() float;
            getPerimeter() float;
        }

        type Rectangle struct {
            width float;
            height float;
        }

        func (r Rectangle) getArea() float {
            return r.width * r.height;
        }

        func (r Rectangle) getPerimeter() float {
            return 2 * (r.width + r.height);
        }

        func main() {
            var rect Shape = Rectangle{width: 5.0, height: 3.0};
            putFloatLn(rect.getArea());
            putFloat(rect.getPerimeter());
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15.0\n16.0", 578))

    def test_079(self):
        input = """
        func isPalindrome(s string) boolean {
            return true;
        }

        func main() {
            putBoolLn(isPalindrome("racecar"));
            putBool(isPalindrome("hello"));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\ntrue", 579))

    def test_080(self):
        input = """
        type myStack struct {
            items [10]int;
            top int;
        }

        func (s myStack) isEmpty() boolean {
            return s.top < 0;
        }

        func (s myStack) push(item int) {
            s.top += 1;
            s.items[s.top] := item;
        }

        func (s myStack) pop() int {
            if (!s.isEmpty()) {
                var item = s.items[s.top];
                s.top -= 1;
                return item;
            }
            return -1;
        }

        func main() {
            var mystack myStack = myStack{items: [10]int{1,2,3,4,5,6,7,8,9,10}, top: -1};
            mystack.push(1);
            mystack.push(2);
            putIntLn(mystack.pop());
            putInt(mystack.pop());
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n1", 580))

    def test_081(self):
        input = """
        type Animal interface {
            makeSound();
            getAge() int;
        }

        type Dog struct {
            age int;
            breed string;
        }

        func (d Dog) makeSound() {
            putStringLn("Woof!");
        }

        func (d Dog) getAge() int {
            return d.age;
        }

        func main() {
            var dog Animal = Dog{age: 3, breed: "Husky"};
            dog.makeSound();
            putInt(dog.getAge());
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Woof!\n3", 581))

    def test_082(self):
        input = """
        type Math struct {
            a int; 
            b int;
        }

        func (m Math) factorial(n int) int {
            if (n <= 1) {
                return 1;
            }
            return n * m.factorial(n - 1);
        }

        func main() {
            var math Math;
            putIntLn(math.factorial(5));
            putInt(math.factorial(3));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "120\n6", 582))

    def test_083(self):
        input = """
        func main() {
            var result = [2]string{"world", "hello"};
            putStringLn(result[0]);
            putString(result[1]);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "world\nhello", 583))

    def test_084(self):
        input = """
        type Complex struct {
            real float;
            imag float;
        }

        func (c Complex) add(other Complex) Complex {
            return Complex{
                real: c.real + other.real,
                imag: c.imag + other.imag
            };
        }

        func main() {
            var c1 Complex = Complex{real: 1.5, imag: 2.5};
            var c2 Complex = Complex{real: 3.5, imag: 4.5};
            var result Complex = c1.add(c2);
            putFloatLn(result.real);
            putFloat(result.imag);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5.0\n7.0", 584))

    def test_085(self):
        input = """
        type Counter interface {
            increment() int;
            getValue() int;
        }

        type SimpleCounter struct {
            value int;
        }

        func (sc SimpleCounter) increment() int {
            sc.value += 1;
            return sc.value;
        }

        func (sc SimpleCounter) getValue() int {
            return sc.value;
        }

        func main() {
            var counter Counter = SimpleCounter{value: 0};
            putIntLn(counter.increment());
            putIntLn(counter.increment());
            putInt(counter.getValue());
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n2", 585))

    def test_086(self):
        input = """
        func findMax(arr [5]int) int {
            var max = arr[0];
            for i := 1; i < 5; i += 1 {
                if (arr[i] > max) {
                    max := arr[i];
                }
            }
            return max;
        }

        func main() {
            var numbers = [5]int{3, 7, 2, 9, 1};
            putInt(findMax(numbers));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "9", 586))

    def test_087(self):
        input = """
        type StringUtils struct {a int; b int;}

        func (su StringUtils) concatenation(s1 string, s2 string) string {
            return s1 + s2;
        }

        func main() {
            var utils StringUtils;
            var result string = utils.concatenation("Hello, ", "World!");
            putString(result);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Hello, World!", 587))

    def test_088(self):
        input = """
        func countEven(arr [6]int) int {
            var count = 0;
            for i := 0; i < 6; i += 1 {
                if (arr[i] % 2 == 0) {
                    count += 1;
                }
            }
            return count;
        }

        func main() {
            var numbers = [6]int{1, 2, 3, 4, 5, 6};
            putInt(countEven(numbers));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3", 588))

    def test_089(self):
        input = """
        type Logger struct {
            prefix string;
        }

        func (l Logger) log(message string) {
            putStringLn(l.prefix + ": " + message);
        }

        func main() {
            var logger Logger = Logger{prefix: "INFO"};
            logger.log("Application started");
            logger.log("Process completed");
        }
        """
        self.assertTrue(TestCodeGen.test(input, "INFO: Application started\nINFO: Process completed\n", 589))

    def test_090(self):
        input = """
        func reverseArray(arr [5]int) [5]int {
            var result [5]int;
            for i := 0; i < 5; i += 1 {
                result[i] := arr[4 - i];
            }
            return result;
        }

        func main() {
            var arr = [5]int{1, 2, 3, 4, 5};
            var reversed [5]int = reverseArray(arr);
            for i := 0; i < 5; i += 1 {
                putInt(reversed[i]);
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "54321", 590))

    def test_091(self):
        input = """
        type Calculator struct {
            value float;
        }

        func (c Calculator) add(x float) Calculator {
            return Calculator{value: c.value + x};
        }

        func (c Calculator) multiply(x float) Calculator {
            return Calculator{value: c.value * x};
        }

        func main() {
            var calc Calculator = Calculator{value: 5.0};
            calc := calc.add(3.0).multiply(2.0);
            putFloat(calc.value);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "16.0", 591))

    def test_092(self):
        input = """
        func sumDigits(n int) int {
            var sum = 0;
            for n > 0 {
                sum += n % 10;
                n := n / 10;
            }
            return sum;
        }

        func main() {
            putIntLn(sumDigits(123));
            putInt(sumDigits(456));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n15", 592))

    def test_093(self):
        input = """
        type Temperature interface {
            toCelsius() float;
            toFahrenheit() float;
        }

        type Celsius struct {
            value float;
        }

        func (c Celsius) toCelsius() float {
            return c.value;
        }

        func (c Celsius) toFahrenheit() float {
            return c.value * 9.0 / 5.0 + 32.0;
        }

        func main() {
            var temp Temperature = Celsius{value: 25.0};
            putFloatLn(temp.toCelsius());
            putFloat(temp.toFahrenheit());
        }
        """
        self.assertTrue(TestCodeGen.test(input, "25.0\n77.0", 593))

    def test_094(self):
        input = """
        func filterPositive(arr [6]int) [6]int {
            var result [6]int;
            var j = 0;
            for i := 0; i < 6; i += 1 {
                if (arr[i] > 0) {
                    result[j] := arr[i];
                    j += 1;
                }
            }
            return result;
        }

        func main() {
            var numbers = [6]int{1, 2, 3, 4, 5, 6};
            var filtered [6]int = filterPositive(numbers);
            for i := 0; i < 6; i += 1 {
                if (filtered[i] > 0) {
                    putInt(filtered[i]);
                    putString(" ");
                }
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1 2 3 4 5 6 ", 594))

    def test_095(self):
        input = """
        type Queue struct {
            items [10]int;
            front int;
            rear int;
        }

        func (q Queue) enqueue(item int) Queue {
            if (q.rear < 10) {
                q.items[q.rear] := item;
                q.rear += 1;
            }
            return q;
        }

        func (q Queue) dequeue() int {
            if (q.front < q.rear) {
                var item = q.items[q.front];
                q.front += 1;
                return item;
            }
            return -1;
        }

        func main() {
            var q Queue = Queue{items: [10]int{0,0,0,0,0,0,0,0,0,0}, front: 0, rear: 0};
            q := q.enqueue(1).enqueue(2).enqueue(3);
            putIntLn(q.dequeue());
            putIntLn(q.dequeue());
            putInt(q.dequeue());
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n3", 595))

    def test_096(self):
        input = """
        type Matrix struct {
            data [2][2]int;
        }

        func (m Matrix) add(other Matrix) Matrix {
            var result Matrix = Matrix{data: [2][2]int{{0, 0}, {0, 0}}};
            for i := 0; i < 2; i += 1 {
                for j := 0; j < 2; j += 1 {
                    result.data[i][j] := m.data[i][j] + other.data[i][j];
                }
            }
            return result;
        }

        func main() {
            var m1 Matrix = Matrix{data: [2][2]int{{1, 2}, {3, 4}}};
            var m2 Matrix = Matrix{data: [2][2]int{{5, 6}, {7, 8}}};
            var result Matrix = m1.add(m2);
            putIntLn(result.data[0][0]);
            putIntLn(result.data[0][1]);
            putIntLn(result.data[1][0]);
            putInt(result.data[1][1]);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n8\n10\n12", 596))

    def test_097(self):
        input = """
        type Comparator interface {
            compare(a int, b int) int;
        }

        type NumericComparator struct {
            a int; 
            b int;
        }

        func (nc NumericComparator) compare(a int, b int) int {
            if (a < b) { return -1; }
            if (a > b) { return 1; }
            return 0;
        }

        func main() {
            var comp Comparator = NumericComparator{};
            putIntLn(comp.compare(5, 3));
            putIntLn(comp.compare(2, 4));
            putInt(comp.compare(6, 6));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n-1\n0", 597))

    def test_098(self):
        input = """
        func fibonacci(n int) int {
            if (n <= 1) { return n; }
            var prev = 0;
            var curr = 1;
            for i := 2; i <= n; i += 1 {
                var next = prev + curr;
                prev := curr;
                curr := next;
            }
            return curr;
        }

        func main() {
            for i := 0; i < 5; i += 1 {
                putInt(fibonacci(i));
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0 1 1 2 3 ", 598))

    def test_099(self):
        input = """
        type EmailValidator struct {
            a int; 
            b int;
        }

        func (ev EmailValidator) isValidEmail(email string) boolean {
            var hasAt = false;
            var hasDot = false;
            return hasAt && hasDot;
        }

        func main() {
            var validator EmailValidator;
            putBoolLn(validator.isValidEmail("test@example.com"));
            putBool(validator.isValidEmail("invalid-email"));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "false\nfalse", 599))

    def test_100(self):
        input = """
        type BankAccount struct {
            balance float;
            owner string;
        }

        func (ba BankAccount) deposit(amount float) BankAccount {
            return BankAccount{
                balance: ba.balance + amount,
                owner: ba.owner
            };
        }

        func (ba BankAccount) withdraw(amount float) BankAccount {
            if (amount <= ba.balance) {
                return BankAccount{
                    balance: ba.balance - amount,
                    owner: ba.owner
                };
            }
            return ba;
        }

        func main() {
            var account BankAccount = BankAccount{balance: 1000.0, owner: "John"};
            account := account.deposit(500.0);
            putFloatLn(account.balance);
            account := account.withdraw(300.0);
            putFloat(account.balance);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1500.0\n1200.0", 600))
