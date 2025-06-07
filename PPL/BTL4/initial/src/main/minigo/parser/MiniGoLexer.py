# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u020a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\7\65\u0159\n\65\f\65\16\65\u015c\13\65\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u0162\n\66\3\67\3\67\6\67\u0166\n")
        buf.write("\67\r\67\16\67\u0167\3\67\7\67\u016b\n\67\f\67\16\67\u016e")
        buf.write("\13\67\5\67\u0170\n\67\38\38\38\68\u0175\n8\r8\168\u0176")
        buf.write("\39\39\39\69\u017c\n9\r9\169\u017d\3:\3:\3:\6:\u0183\n")
        buf.write(":\r:\16:\u0184\3;\3;\3;\7;\u018a\n;\f;\16;\u018d\13;\3")
        buf.write(";\3;\5;\u0191\n;\3;\3;\5;\u0195\n;\3<\6<\u0198\n<\r<\16")
        buf.write("<\u0199\3<\7<\u019d\n<\f<\16<\u01a0\13<\3=\3=\3>\3>\3")
        buf.write("?\3?\7?\u01a8\n?\f?\16?\u01ab\13?\3?\3?\3@\3@\5@\u01b1")
        buf.write("\n@\3A\3A\3A\3B\3B\3B\3C\5C\u01ba\nC\3C\3C\3C\3D\6D\u01c0")
        buf.write("\nD\rD\16D\u01c1\3D\3D\3E\3E\3E\3E\7E\u01ca\nE\fE\16E")
        buf.write("\u01cd\13E\3E\3E\3F\3F\3F\3F\3F\7F\u01d6\nF\fF\16F\u01d9")
        buf.write("\13F\3F\3F\3F\3F\3F\3G\3G\3G\3H\3H\3H\3H\3H\3H\5H\u01e9")
        buf.write("\nH\3I\3I\7I\u01ed\nI\fI\16I\u01f0\13I\3I\3I\3I\5I\u01f5")
        buf.write("\nI\3J\3J\3J\7J\u01fa\nJ\fJ\16J\u01fd\13J\3J\3J\3K\3K")
        buf.write("\7K\u0203\nK\fK\16K\u0206\13K\3K\3K\3K\3\u01d7\2L\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2")
        buf.write("u8w\2y\2{\2}9\177\2\u0081\2\u0083\2\u0085:\u0087;\u0089")
        buf.write("<\u008b=\u008d>\u008f?\u0091\2\u0093\2\u0095@\3\2\25\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\3\2\62\62\4\2")
        buf.write("DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2")
        buf.write("--//\4\2GGgg\5\2\f\f$$^^\7\2$$^^ppttvv\6\2^^ppttvv\5\2")
        buf.write("\13\13\16\17\"\"\3\2\f\f\3\3\f\f\2\u0218\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2u\3\2\2\2\2}\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0095\3\2\2\2\3\u0097\3\2\2")
        buf.write("\2\5\u009a\3\2\2\2\7\u009f\3\2\2\2\t\u00a3\3\2\2\2\13")
        buf.write("\u00aa\3\2\2\2\r\u00af\3\2\2\2\17\u00b4\3\2\2\2\21\u00bb")
        buf.write("\3\2\2\2\23\u00c5\3\2\2\2\25\u00cc\3\2\2\2\27\u00d0\3")
        buf.write("\2\2\2\31\u00d6\3\2\2\2\33\u00de\3\2\2\2\35\u00e4\3\2")
        buf.write("\2\2\37\u00e8\3\2\2\2!\u00f1\3\2\2\2#\u00f7\3\2\2\2%\u00fd")
        buf.write("\3\2\2\2\'\u0101\3\2\2\2)\u0106\3\2\2\2+\u010c\3\2\2\2")
        buf.write("-\u010e\3\2\2\2/\u0110\3\2\2\2\61\u0112\3\2\2\2\63\u0114")
        buf.write("\3\2\2\2\65\u0116\3\2\2\2\67\u0119\3\2\2\29\u011c\3\2")
        buf.write("\2\2;\u011e\3\2\2\2=\u0121\3\2\2\2?\u0123\3\2\2\2A\u0126")
        buf.write("\3\2\2\2C\u0129\3\2\2\2E\u012c\3\2\2\2G\u012e\3\2\2\2")
        buf.write("I\u0130\3\2\2\2K\u0133\3\2\2\2M\u0136\3\2\2\2O\u0139\3")
        buf.write("\2\2\2Q\u013c\3\2\2\2S\u013f\3\2\2\2U\u0142\3\2\2\2W\u0144")
        buf.write("\3\2\2\2Y\u0146\3\2\2\2[\u0148\3\2\2\2]\u014a\3\2\2\2")
        buf.write("_\u014c\3\2\2\2a\u014e\3\2\2\2c\u0150\3\2\2\2e\u0152\3")
        buf.write("\2\2\2g\u0154\3\2\2\2i\u0156\3\2\2\2k\u0161\3\2\2\2m\u016f")
        buf.write("\3\2\2\2o\u0171\3\2\2\2q\u0178\3\2\2\2s\u017f\3\2\2\2")
        buf.write("u\u0186\3\2\2\2w\u0197\3\2\2\2y\u01a1\3\2\2\2{\u01a3\3")
        buf.write("\2\2\2}\u01a5\3\2\2\2\177\u01b0\3\2\2\2\u0081\u01b2\3")
        buf.write("\2\2\2\u0083\u01b5\3\2\2\2\u0085\u01b9\3\2\2\2\u0087\u01bf")
        buf.write("\3\2\2\2\u0089\u01c5\3\2\2\2\u008b\u01d0\3\2\2\2\u008d")
        buf.write("\u01df\3\2\2\2\u008f\u01e8\3\2\2\2\u0091\u01ea\3\2\2\2")
        buf.write("\u0093\u01f6\3\2\2\2\u0095\u0200\3\2\2\2\u0097\u0098\7")
        buf.write("k\2\2\u0098\u0099\7h\2\2\u0099\4\3\2\2\2\u009a\u009b\7")
        buf.write("g\2\2\u009b\u009c\7n\2\2\u009c\u009d\7u\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\6\3\2\2\2\u009f\u00a0\7h\2\2\u00a0\u00a1")
        buf.write("\7q\2\2\u00a1\u00a2\7t\2\2\u00a2\b\3\2\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7w\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7p\2\2\u00a9\n")
        buf.write("\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7e\2\2\u00ae\f\3\2\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\u00b1\7{\2\2\u00b1\u00b2\7r\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\16\3\2\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9")
        buf.write("\7e\2\2\u00b9\u00ba\7v\2\2\u00ba\20\3\2\2\2\u00bb\u00bc")
        buf.write("\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7e\2\2\u00c3\u00c4\7g\2\2\u00c4\22")
        buf.write("\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7i\2\2\u00cb\24\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\26\3\2\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7v\2\2\u00d5\30\3\2\2\2\u00d6\u00d7")
        buf.write("\7d\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\32\3\2\2\2\u00de\u00df\7e\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\34\3\2\2\2\u00e4\u00e5\7x\2\2\u00e5\u00e6")
        buf.write("\7c\2\2\u00e6\u00e7\7t\2\2\u00e7\36\3\2\2\2\u00e8\u00e9")
        buf.write("\7e\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec")
        buf.write("\7v\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7w\2\2\u00ef\u00f0\7g\2\2\u00f0 \3\2\2\2\u00f1\u00f2")
        buf.write("\7d\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7m\2\2\u00f6\"\3\2\2\2\u00f7\u00f8")
        buf.write("\7t\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7i\2\2\u00fb\u00fc\7g\2\2\u00fc$\3\2\2\2\u00fd\u00fe")
        buf.write("\7p\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7n\2\2\u0100&\3")
        buf.write("\2\2\2\u0101\u0102\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104")
        buf.write("\7w\2\2\u0104\u0105\7g\2\2\u0105(\3\2\2\2\u0106\u0107")
        buf.write("\7h\2\2\u0107\u0108\7c\2\2\u0108\u0109\7n\2\2\u0109\u010a")
        buf.write("\7u\2\2\u010a\u010b\7g\2\2\u010b*\3\2\2\2\u010c\u010d")
        buf.write("\7-\2\2\u010d,\3\2\2\2\u010e\u010f\7/\2\2\u010f.\3\2\2")
        buf.write("\2\u0110\u0111\7,\2\2\u0111\60\3\2\2\2\u0112\u0113\7\61")
        buf.write("\2\2\u0113\62\3\2\2\2\u0114\u0115\7\'\2\2\u0115\64\3\2")
        buf.write("\2\2\u0116\u0117\7?\2\2\u0117\u0118\7?\2\2\u0118\66\3")
        buf.write("\2\2\2\u0119\u011a\7#\2\2\u011a\u011b\7?\2\2\u011b8\3")
        buf.write("\2\2\2\u011c\u011d\7>\2\2\u011d:\3\2\2\2\u011e\u011f\7")
        buf.write(">\2\2\u011f\u0120\7?\2\2\u0120<\3\2\2\2\u0121\u0122\7")
        buf.write("@\2\2\u0122>\3\2\2\2\u0123\u0124\7@\2\2\u0124\u0125\7")
        buf.write("?\2\2\u0125@\3\2\2\2\u0126\u0127\7(\2\2\u0127\u0128\7")
        buf.write("(\2\2\u0128B\3\2\2\2\u0129\u012a\7~\2\2\u012a\u012b\7")
        buf.write("~\2\2\u012bD\3\2\2\2\u012c\u012d\7#\2\2\u012dF\3\2\2\2")
        buf.write("\u012e\u012f\7?\2\2\u012fH\3\2\2\2\u0130\u0131\7-\2\2")
        buf.write("\u0131\u0132\7?\2\2\u0132J\3\2\2\2\u0133\u0134\7/\2\2")
        buf.write("\u0134\u0135\7?\2\2\u0135L\3\2\2\2\u0136\u0137\7,\2\2")
        buf.write("\u0137\u0138\7?\2\2\u0138N\3\2\2\2\u0139\u013a\7\61\2")
        buf.write("\2\u013a\u013b\7?\2\2\u013bP\3\2\2\2\u013c\u013d\7\'\2")
        buf.write("\2\u013d\u013e\7?\2\2\u013eR\3\2\2\2\u013f\u0140\7<\2")
        buf.write("\2\u0140\u0141\7?\2\2\u0141T\3\2\2\2\u0142\u0143\7\60")
        buf.write("\2\2\u0143V\3\2\2\2\u0144\u0145\7*\2\2\u0145X\3\2\2\2")
        buf.write("\u0146\u0147\7+\2\2\u0147Z\3\2\2\2\u0148\u0149\7]\2\2")
        buf.write("\u0149\\\3\2\2\2\u014a\u014b\7_\2\2\u014b^\3\2\2\2\u014c")
        buf.write("\u014d\7}\2\2\u014d`\3\2\2\2\u014e\u014f\7\177\2\2\u014f")
        buf.write("b\3\2\2\2\u0150\u0151\7.\2\2\u0151d\3\2\2\2\u0152\u0153")
        buf.write("\7=\2\2\u0153f\3\2\2\2\u0154\u0155\7<\2\2\u0155h\3\2\2")
        buf.write("\2\u0156\u015a\t\2\2\2\u0157\u0159\t\3\2\2\u0158\u0157")
        buf.write("\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015bj\3\2\2\2\u015c\u015a\3\2\2\2\u015d")
        buf.write("\u0162\5m\67\2\u015e\u0162\5o8\2\u015f\u0162\5q9\2\u0160")
        buf.write("\u0162\5s:\2\u0161\u015d\3\2\2\2\u0161\u015e\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162l\3\2\2\2\u0163")
        buf.write("\u0170\t\4\2\2\u0164\u0166\t\5\2\2\u0165\u0164\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3")
        buf.write("\2\2\2\u0168\u016c\3\2\2\2\u0169\u016b\t\4\2\2\u016a\u0169")
        buf.write("\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2")
        buf.write("\u016f\u0163\3\2\2\2\u016f\u0165\3\2\2\2\u0170n\3\2\2")
        buf.write("\2\u0171\u0172\t\6\2\2\u0172\u0174\t\7\2\2\u0173\u0175")
        buf.write("\t\b\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177p\3\2\2\2\u0178")
        buf.write("\u0179\t\6\2\2\u0179\u017b\t\t\2\2\u017a\u017c\t\n\2\2")
        buf.write("\u017b\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017b\3")
        buf.write("\2\2\2\u017d\u017e\3\2\2\2\u017er\3\2\2\2\u017f\u0180")
        buf.write("\t\6\2\2\u0180\u0182\t\13\2\2\u0181\u0183\t\f\2\2\u0182")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185t\3\2\2\2\u0186\u0187\5w<\2")
        buf.write("\u0187\u018b\5U+\2\u0188\u018a\t\4\2\2\u0189\u0188\3\2")
        buf.write("\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018c\u0194\3\2\2\2\u018d\u018b\3\2\2\2\u018e")
        buf.write("\u0190\5{>\2\u018f\u0191\5y=\2\u0190\u018f\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193\5w<\2\u0193")
        buf.write("\u0195\3\2\2\2\u0194\u018e\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195v\3\2\2\2\u0196\u0198\t\4\2\2\u0197\u0196\3\2\2")
        buf.write("\2\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a")
        buf.write("\3\2\2\2\u019a\u019e\3\2\2\2\u019b\u019d\t\4\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019fx\3\2\2\2\u01a0\u019e\3\2\2")
        buf.write("\2\u01a1\u01a2\t\r\2\2\u01a2z\3\2\2\2\u01a3\u01a4\t\16")
        buf.write("\2\2\u01a4|\3\2\2\2\u01a5\u01a9\7$\2\2\u01a6\u01a8\5\177")
        buf.write("@\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ac\u01ad\7$\2\2\u01ad~\3\2\2\2\u01ae")
        buf.write("\u01b1\n\17\2\2\u01af\u01b1\5\u0081A\2\u01b0\u01ae\3\2")
        buf.write("\2\2\u01b0\u01af\3\2\2\2\u01b1\u0080\3\2\2\2\u01b2\u01b3")
        buf.write("\7^\2\2\u01b3\u01b4\t\20\2\2\u01b4\u0082\3\2\2\2\u01b5")
        buf.write("\u01b6\7^\2\2\u01b6\u01b7\n\21\2\2\u01b7\u0084\3\2\2\2")
        buf.write("\u01b8\u01ba\7\17\2\2\u01b9\u01b8\3\2\2\2\u01b9\u01ba")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\7\f\2\2\u01bc")
        buf.write("\u01bd\bC\2\2\u01bd\u0086\3\2\2\2\u01be\u01c0\t\22\2\2")
        buf.write("\u01bf\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01bf\3")
        buf.write("\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4")
        buf.write("\bD\3\2\u01c4\u0088\3\2\2\2\u01c5\u01c6\7\61\2\2\u01c6")
        buf.write("\u01c7\7\61\2\2\u01c7\u01cb\3\2\2\2\u01c8\u01ca\n\23\2")
        buf.write("\2\u01c9\u01c8\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd")
        buf.write("\u01cb\3\2\2\2\u01ce\u01cf\bE\3\2\u01cf\u008a\3\2\2\2")
        buf.write("\u01d0\u01d1\7\61\2\2\u01d1\u01d2\7,\2\2\u01d2\u01d7\3")
        buf.write("\2\2\2\u01d3\u01d6\5\u008bF\2\u01d4\u01d6\13\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01da\3")
        buf.write("\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01db\7,\2\2\u01db\u01dc")
        buf.write("\7\61\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\bF\3\2\u01de")
        buf.write("\u008c\3\2\2\2\u01df\u01e0\13\2\2\2\u01e0\u01e1\bG\4\2")
        buf.write("\u01e1\u008e\3\2\2\2\u01e2\u01e3\5\u0091I\2\u01e3\u01e4")
        buf.write("\bH\5\2\u01e4\u01e9\3\2\2\2\u01e5\u01e6\5\u0093J\2\u01e6")
        buf.write("\u01e7\bH\6\2\u01e7\u01e9\3\2\2\2\u01e8\u01e2\3\2\2\2")
        buf.write("\u01e8\u01e5\3\2\2\2\u01e9\u0090\3\2\2\2\u01ea\u01ee\7")
        buf.write("$\2\2\u01eb\u01ed\5\177@\2\u01ec\u01eb\3\2\2\2\u01ed\u01f0")
        buf.write("\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef")
        buf.write("\u01f4\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f2\7\17\2")
        buf.write("\2\u01f2\u01f5\7\f\2\2\u01f3\u01f5\t\24\2\2\u01f4\u01f1")
        buf.write("\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5\u0092\3\2\2\2\u01f6")
        buf.write("\u01f7\7$\2\2\u01f7\u01fb\7$\2\2\u01f8\u01fa\5\177@\2")
        buf.write("\u01f9\u01f8\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3")
        buf.write("\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fe\3\2\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fe\u01ff\7$\2\2\u01ff\u0094\3\2\2\2\u0200")
        buf.write("\u0204\7$\2\2\u0201\u0203\5\177@\2\u0202\u0201\3\2\2\2")
        buf.write("\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3")
        buf.write("\2\2\2\u0205\u0207\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0208")
        buf.write("\5\u0083B\2\u0208\u0209\bK\7\2\u0209\u0096\3\2\2\2\34")
        buf.write("\2\u015a\u0161\u0167\u016c\u016f\u0176\u017d\u0184\u018b")
        buf.write("\u0190\u0194\u0199\u019e\u01a9\u01b0\u01b9\u01c1\u01cb")
        buf.write("\u01d5\u01d7\u01e8\u01ee\u01f4\u01fb\u0204\b\3C\2\b\2")
        buf.write("\2\3G\3\3H\4\3H\5\3K\6")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQ = 26
    INEQ = 27
    LT = 28
    LTE = 29
    GT = 30
    GTE = 31
    AND = 32
    OR = 33
    NOT = 34
    ASSIGNINIT = 35
    ASSIGNADD = 36
    ASSIGNSUB = 37
    ASSIGNMUL = 38
    ASSIGNDIV = 39
    ASSIGNMOD = 40
    ASSIGN = 41
    DOT = 42
    LP = 43
    RP = 44
    LSB = 45
    RSB = 46
    LB = 47
    RB = 48
    CM = 49
    SC = 50
    CL = 51
    ID = 52
    INT_LIT = 53
    FLOAT_LIT = 54
    STRING_LIT = 55
    NEWLINE = 56
    WS = 57
    SINGLE_LINE_COMMENT = 58
    MULTIPLE_LINE_COMMENT = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "':='", "'.'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQ", "INEQ", "LT", "LTE", "GT", "GTE", "AND", 
            "OR", "NOT", "ASSIGNINIT", "ASSIGNADD", "ASSIGNSUB", "ASSIGNMUL", 
            "ASSIGNDIV", "ASSIGNMOD", "ASSIGN", "DOT", "LP", "RP", "LSB", 
            "RSB", "LB", "RB", "CM", "SC", "CL", "ID", "INT_LIT", "FLOAT_LIT", 
            "STRING_LIT", "NEWLINE", "WS", "SINGLE_LINE_COMMENT", "MULTIPLE_LINE_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "INEQ", "LT", 
                  "LTE", "GT", "GTE", "AND", "OR", "NOT", "ASSIGNINIT", 
                  "ASSIGNADD", "ASSIGNSUB", "ASSIGNMUL", "ASSIGNDIV", "ASSIGNMOD", 
                  "ASSIGN", "DOT", "LP", "RP", "LSB", "RSB", "LB", "RB", 
                  "CM", "SC", "CL", "ID", "INT_LIT", "DEC_INT", "BIN_INT", 
                  "OCT_INT", "HEX_INT", "FLOAT_LIT", "DIGIT", "SIGN", "EXPO", 
                  "STRING_LIT", "STR", "ESC_CHAR", "ESC_ILL", "NEWLINE", 
                  "WS", "SINGLE_LINE_COMMENT", "MULTIPLE_LINE_COMMENT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "UNCLOSE_1", "UNCLOSE_2", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

        
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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[65] = self.NEWLINE_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if (self.preType == self.ID) or (self.preType == self.INT) or (self.preType == self.FLOAT) or (self.preType == self.STRING) or (self.preType == self.BOOLEAN) or (self.preType == self.NIL) or (self.preType == self.INT_LIT) or (self.preType == self.FLOAT_LIT) or (self.preType == self.STRING_LIT) or (self.preType == self.RP) or (self.preType == self.RB) or (self.preType == self.RSB) or (self.preType == self.RETURN) or (self.preType == self.CONTINUE) or (self.preType == self.BREAK) or (self.preType == self.TRUE) or (self.preType == self.FALSE):
                    self.text = ';' 
                else:
                    self.skip()

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                        raise UncloseString(self.text[0:-2])
                    elif (self.text[-1] == '\n'):
                        raise UncloseString(self.text[0:-1])
                    else:
                        raise UncloseString(self.text[0:])
                
     

        if actionIndex == 3:

                    if (self.text[1] == '"'):
                        raise UncloseString(self.text[1:-1])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(self.text[0:])

     


