import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_lexer_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_lexer_2(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_lexer_3(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_lexer_4(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    def test_lexer_5(self):
        self.assertTrue(TestLexer.checkLexeme("10", "10,<EOF>",105))
    def test_lexer_6(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>", 106))
    def test_lexer_7(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("[]","[,],<EOF>", 107))
    def test_lexer_8(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>", 108))
    def test_lexer_9(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>", 109))
    def test_lexer_10(self):
        """Comments"""
        self.assertTrue(TestLexer.checkLexeme("// abc?0123","<EOF>", 110))

### 11 - 20: Test Identifier & Keywords
    def test_lexer_11(self):
        self.assertTrue(TestLexer.checkLexeme("var a int = 12","var,a,int,=,12,<EOF>", 111))
    def test_lexer_12(self):
        self.assertTrue(TestLexer.checkLexeme("var b1 float","var,b1,float,<EOF>", 112))
    def test_lexer_13(self):
        self.assertTrue(TestLexer.checkLexeme("const _c = 2;","const,_c,=,2,;,<EOF>", 113))
    def test_lexer_14(self):
        self.assertTrue(TestLexer.checkLexeme("if (c > 2) {}","if,(,c,>,2,),{,},<EOF>", 114))
    def test_lexer_15(self):
        self.assertTrue(TestLexer.checkLexeme("for i < 10","for,i,<,10,<EOF>", 115))
    def test_lexer_16(self):
        self.assertTrue(TestLexer.checkLexeme("""
            for i := 0; i < 10; i += 1 {
                // loop body    
            }
""","for,i,:=,0,;,i,<,10,;,i,+=,1,{,},;,<EOF>", 116))
    def test_lexer_17(self):
        self.assertTrue(TestLexer.checkLexeme("""
            const a = 10;
""","const,a,=,10,;,<EOF>", 117))
    def test_lexer_18(self):
        self.assertTrue(TestLexer.checkLexeme("var y = \"Hello\";","var,y,=,\"Hello\",;,<EOF>", 118))
    def test_lexer_19(self):
        self.assertTrue(TestLexer.checkLexeme("var arr [5]int","var,arr,[,5,],int,<EOF>", 119))
    def test_lexer_20(self):
        self.assertTrue(TestLexer.checkLexeme("""
            type People struct {
                name string;
                age int;
            }
""","type,People,struct,{,name,string,;,age,int,;,},;,<EOF>", 120))
### 21 - 30: Test String
    def test_lexer_21(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello World" ""","\"Hello World\",<EOF>", 121))
    def test_lexer_22(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello World\\t" ""","\"Hello World\\t\",<EOF>", 122))
    def test_lexer_23(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello World \\n" ""","\"Hello World \\n\",<EOF>", 123))
    def test_lexer_24(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello World \\n This is MiniGo \\n" ""","\"Hello World \\n This is MiniGo \\n\",<EOF>", 124))
    def test_lexer_25(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello World \\n This is MiniGo \n" ""","Unclosed string: \"Hello World \\n This is MiniGo ", 125))
    def test_lexer_26(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello World \\f" ""","Illegal escape in string: \"Hello World \\f", 126))
    def test_lexer_27(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""Hello World" ""","Unclosed string: \"Hello World", 127))
    def test_lexer_28(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123" ""","123,Unclosed string: \" ", 128))
    def test_lexer_29(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string with a newline\\n" ""","\"This is a string with a newline\\n\",<EOF>", 129))
    def test_lexer_30(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hello World \\n This is \'MiniGo\' language \\\\ \\t \\r \\n This is a string with a newline\\n" ""","\"Hello World \\n This is \'MiniGo\' language \\\\ \\t \\r \\n This is a string with a newline\\n\",<EOF>", 130))
### 31 - 40: Test Floating Point:
    def test_lexer_31(self):
        self.assertTrue(TestLexer.checkLexeme("1.23", "1.23,<EOF>", 131))
    def test_lexer_32(self):
        self.assertTrue(TestLexer.checkLexeme(".456", ".,456,<EOF>", 132))
    def test_lexer_33(self):
        self.assertTrue(TestLexer.checkLexeme("3e10", "3,e10,<EOF>", 133))
    def test_lexer_34(self):
        self.assertTrue(TestLexer.checkLexeme("6.022E23", "6.022E23,<EOF>", 134))
    def test_lexer_35(self):
        self.assertTrue(TestLexer.checkLexeme("0456.", "0456.,<EOF>", 135))
    def test_lexer_36(self):
        self.assertTrue(TestLexer.checkLexeme("1.e+10", "1.e+10,<EOF>", 136))
    def test_lexer_37(self):
        self.assertTrue(TestLexer.checkLexeme(".e1", ".,e1,<EOF>", 137))
    def test_lexer_38(self):
        self.assertTrue(TestLexer.checkLexeme("12.34.56", "12.34,.,56,<EOF>", 138))
    def test_lexer_39(self):
        self.assertTrue(TestLexer.checkLexeme("1.2e3.4", "1.2e3,.,4,<EOF>", 139))
    def test_lexer_40(self):
        self.assertTrue(TestLexer.checkLexeme("0.0", "0.0,<EOF>", 140))   
### 41 - 50: Test Integer:
    def test_lexer_41(self):
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 141))
    def test_lexer_42(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 142))
    def test_lexer_43(self):
        self.assertTrue(TestLexer.checkLexeme("42", "42,<EOF>", 143))
    def test_lexer_44(self):
        self.assertTrue(TestLexer.checkLexeme("0123", "0,123,<EOF>", 144))
    def test_lexer_45(self):
        self.assertTrue(TestLexer.checkLexeme("0x1A", "0x1A,<EOF>", 145))
    def test_lexer_46(self):
        self.assertTrue(TestLexer.checkLexeme("0b101", "0b101,<EOF>", 146))
    def test_lexer_47(self):
        self.assertTrue(TestLexer.checkLexeme("0o77", "0o77,<EOF>", 147))
    def test_lexer_48(self):
        self.assertTrue(TestLexer.checkLexeme("-123", "-,123,<EOF>", 148))
    def test_lexer_49(self):
        self.assertTrue(TestLexer.checkLexeme("1_000", "1,_000,<EOF>", 149))
    def test_lexer_50(self):
        self.assertTrue(TestLexer.checkLexeme("9999999", "9999999,<EOF>", 150))
### 51 - 60: Test Boolean and Nil
    def test_lexer_51(self):
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 151))
    def test_lexer_52(self):
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 152))
    def test_lexer_53(self):
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 153))
    def test_lexer_54(self):
        self.assertTrue(TestLexer.checkLexeme("truetrue", "truetrue,<EOF>", 154))
    def test_lexer_55(self):
        self.assertTrue(TestLexer.checkLexeme("false_nil", "false_nil,<EOF>", 155))
    def test_lexer_56(self):
        self.assertTrue(TestLexer.checkLexeme("niltrue", "niltrue,<EOF>", 156))
    def test_lexer_57(self):
        self.assertTrue(TestLexer.checkLexeme("nil_", "nil_,<EOF>", 157))
    def test_lexer_58(self):
        self.assertTrue(TestLexer.checkLexeme("_truefalse", "_truefalse,<EOF>", 158))
    def test_lexer_59(self):
        self.assertTrue(TestLexer.checkLexeme("true_", "true_,<EOF>", 159))
    def test_lexer_60(self):
        self.assertTrue(TestLexer.checkLexeme("_nilfalse", "_nilfalse,<EOF>", 160))
### 61 - 70: Test Separator
    def test_lexer_61(self):
        self.assertTrue(TestLexer.checkLexeme("{", "{,<EOF>", 161))
    def test_lexer_62(self):
        self.assertTrue(TestLexer.checkLexeme("}", "},<EOF>", 162))
    def test_lexer_63(self):
        self.assertTrue(TestLexer.checkLexeme("(", "(,<EOF>", 163))
    def test_lexer_64(self):
        self.assertTrue(TestLexer.checkLexeme(")", "),<EOF>", 164))
    def test_lexer_65(self):
        self.assertTrue(TestLexer.checkLexeme("[", "[,<EOF>", 165))
    def test_lexer_66(self):
        self.assertTrue(TestLexer.checkLexeme("]", "],<EOF>", 166))
    def test_lexer_67(self):
        self.assertTrue(TestLexer.checkLexeme(";", ";,<EOF>", 167))
    def test_lexer_68(self):
        self.assertTrue(TestLexer.checkLexeme(",", ",,<EOF>", 168))
    def test_lexer_69(self):
        self.assertTrue(TestLexer.checkLexeme("{}", "{,},<EOF>", 169))
    def test_lexer_70(self):
        self.assertTrue(TestLexer.checkLexeme("[()]", "[,(,),],<EOF>", 170))
### 71 - 80: Test Comments
    def test_lexer_71(self):
        self.assertTrue(TestLexer.checkLexeme("// Single-line comment", "<EOF>", 171))
    def test_lexer_72(self):
        self.assertTrue(TestLexer.checkLexeme("/* Multi-line\ncomment */", "<EOF>", 172))
    def test_lexer_73(self):
        self.assertTrue(TestLexer.checkLexeme("/* Nested /* comment */ end */", "<EOF>", 173))
    def test_lexer_74(self):
        self.assertTrue(TestLexer.checkLexeme("// Another comment\nNextLine", "NextLine,<EOF>", 174))
    def test_lexer_75(self):
        self.assertTrue(TestLexer.checkLexeme("/**/", "<EOF>", 175))
    def test_lexer_76(self):
        self.assertTrue(TestLexer.checkLexeme("/* Unterminated comment", "/,*,Unterminated,comment,<EOF>", 176))
    def test_lexer_77(self):
        self.assertTrue(TestLexer.checkLexeme("// Mixed // comments /* */", "<EOF>", 177))
    def test_lexer_78(self):
        self.assertTrue(TestLexer.checkLexeme("//Comment\n\"Not ignored\"", "\"Not ignored\",<EOF>", 178))
    def test_lexer_79(self):
        self.assertTrue(TestLexer.checkLexeme("/*Nested\ncomments\nend*/", "<EOF>", 179))
    def test_lexer_80(self):
        self.assertTrue(TestLexer.checkLexeme("//Line1\n//Line2", "<EOF>", 180))
### 81 - 90: Operators
    def test_lexer_81(self):
        self.assertTrue(TestLexer.checkLexeme("%", "%,<EOF>", 181))
    def test_lexer_82(self):
        self.assertTrue(TestLexer.checkLexeme("-", "-,<EOF>", 182))
    def test_lexer_83(self):
        self.assertTrue(TestLexer.checkLexeme("*", "*,<EOF>", 183))
    def test_lexer_84(self):
        self.assertTrue(TestLexer.checkLexeme("/", "/,<EOF>", 184))
    def test_lexer_85(self):
        self.assertTrue(TestLexer.checkLexeme("%=", "%=,<EOF>", 185))
    def test_lexer_86(self):
        self.assertTrue(TestLexer.checkLexeme("==", "==,<EOF>", 186))
    def test_lexer_87(self):
        self.assertTrue(TestLexer.checkLexeme("!=", "!=,<EOF>", 187))
    def test_lexer_88(self):
        self.assertTrue(TestLexer.checkLexeme("<", "<,<EOF>", 188))
    def test_lexer_89(self):
        self.assertTrue(TestLexer.checkLexeme(">", ">,<EOF>", 189))
    def test_lexer_90(self):
        self.assertTrue(TestLexer.checkLexeme("<=", "<=,<EOF>", 190))

### 91 - 100: Complex Test Cases:
    def test_lexer_91(self):
        self.assertTrue(TestLexer.checkLexeme("var x = 5;", "var,x,=,5,;,<EOF>", 191))
    def test_lexer_92(self):
        self.assertTrue(TestLexer.checkLexeme("func foo() {}", "func,foo,(,),{,},<EOF>", 192))
    def test_lexer_93(self):
        self.assertTrue(TestLexer.checkLexeme("type Person struct { name string; }", "type,Person,struct,{,name,string,;,},<EOF>", 193))
    def test_lexer_94(self):
        self.assertTrue(TestLexer.checkLexeme("const Pi = 3.14;", "const,Pi,=,3.14,;,<EOF>", 194))
    def test_lexer_95(self):
        self.assertTrue(TestLexer.checkLexeme("for i := 0; i < 10; i += 1 { }", "for,i,:=,0,;,i,<,10,;,i,+=,1,{,},<EOF>", 195))
    def test_lexer_96(self):
        self.assertTrue(TestLexer.checkLexeme("if x == y { return z; }", "if,x,==,y,{,return,z,;,},<EOF>", 196))
    def test_lexer_97(self):
        self.assertTrue(TestLexer.checkLexeme("x[2] = 5;", "x,[,2,],=,5,;,<EOF>", 197))
    def test_lexer_98(self):
        self.assertTrue(TestLexer.checkLexeme("p.name = \"Alice\";", "p,.,name,=,\"Alice\",;,<EOF>", 198))
    def test_lexer_99(self):
        self.assertTrue(TestLexer.checkLexeme("a := [3]int{1, 2, 3};", "a,:=,[,3,],int,{,1,,,2,,,3,},;,<EOF>", 199))
    def test_lexer_100(self):
        self.assertTrue(TestLexer.checkLexeme("func (p Person) Greet() string { return \"Hello\"; }", "func,(,p,Person,),Greet,(,),string,{,return,\"Hello\",;,},<EOF>", 200))

    
    
    