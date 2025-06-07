# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0304\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\3\2\3\2\7\2\u008d\n\2\f\2\16\2\u0090\13\2\3\2")
        buf.write("\6\2\u0093\n\2\r\2\16\2\u0094\5\2\u0097\n\2\3\3\7\3\u009a")
        buf.write("\n\3\f\3\16\3\u009d\13\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4\u00a5")
        buf.write("\n\4\f\4\16\4\u00a8\13\4\3\5\3\5\3\5\5\5\u00ad\n\5\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00ba\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00c2\n\b\3\t\3\t\3\t\5\t")
        buf.write("\u00c7\n\t\3\n\3\n\5\n\u00cb\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\5\f\u00d6\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00ee\n\20\3\20\3")
        buf.write("\20\5\20\u00f2\n\20\3\20\3\20\7\20\u00f6\n\20\f\20\16")
        buf.write("\20\u00f9\13\20\3\20\5\20\u00fc\n\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0109\n\21")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u010f\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\7\23\u0116\n\23\f\23\16\23\u0119\13\23\3\23\3")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u0126\n\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\5\26\u0134\n\26\3\26\3\26\5\26\u0138")
        buf.write("\n\26\3\26\3\26\7\26\u013c\n\26\f\26\16\26\u013f\13\26")
        buf.write("\3\26\5\26\u0142\n\26\3\26\3\26\3\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\7\27\u014c\n\27\f\27\16\27\u014f\13\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u015e\n\30\3\31\3\31\3\31\5\31\u0163\n\31\3")
        buf.write("\31\3\31\3\31\5\31\u0168\n\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u0172\n\32\3\33\3\33\3\33\3\33\5")
        buf.write("\33\u0178\n\33\3\34\3\34\3\34\3\35\3\35\3\35\5\35\u0180")
        buf.write("\n\35\3\36\3\36\3\36\3\36\5\36\u0186\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3 \3 \3 \3 \3 \5 \u0191\n \3!\3!\5!\u0195\n!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01a0\n\"\3#")
        buf.write("\3#\3#\5#\u01a5\n#\3#\3#\3$\3$\3$\3$\3$\5$\u01ae\n$\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\5&\u01b7\n&\3&\3&\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\5(\u01c4\n(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\7*\u01d6\n*\f*\16*\u01d9\13*\3+\3")
        buf.write("+\3,\3,\3-\3-\3-\3-\3-\3-\7-\u01e5\n-\f-\16-\u01e8\13")
        buf.write("-\3-\5-\u01eb\n-\3-\3-\5-\u01ef\n-\3-\5-\u01f2\n-\3-\3")
        buf.write("-\3.\3.\3.\3.\5.\u01fa\n.\3/\3/\3/\3/\3/\3/\3/\7/\u0203")
        buf.write("\n/\f/\16/\u0206\13/\3/\5/\u0209\n/\3/\3/\3\60\3\60\3")
        buf.write("\60\7\60\u0210\n\60\f\60\16\60\u0213\13\60\3\60\5\60\u0216")
        buf.write("\n\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\5\62")
        buf.write("\u0221\n\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\5\63\u022a")
        buf.write("\n\63\3\63\3\63\3\64\3\64\3\64\3\64\7\64\u0232\n\64\f")
        buf.write("\64\16\64\u0235\13\64\3\64\5\64\u0238\n\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u0244\n\65")
        buf.write("\f\65\16\65\u0247\13\65\3\65\5\65\u024a\n\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\7\66\u0256\n")
        buf.write("\66\f\66\16\66\u0259\13\66\3\66\5\66\u025c\n\66\3\66\3")
        buf.write("\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\7\67")
        buf.write("\u0269\n\67\f\67\16\67\u026c\13\67\3\67\5\67\u026f\n\67")
        buf.write("\3\67\3\67\38\38\38\39\39\39\3:\3:\5:\u027b\n:\3:\3:\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\5<\u0286\n<\3<\3<\5<\u028a\n<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\5<\u0294\n<\3<\3<\3<\3<\3<\3<\7<\u029c")
        buf.write("\n<\f<\16<\u029f\13<\3=\3=\3=\3=\3=\5=\u02a6\n=\3>\3>")
        buf.write("\3>\3>\3>\3>\7>\u02ae\n>\f>\16>\u02b1\13>\3?\3?\3?\3?")
        buf.write("\3?\3?\7?\u02b9\n?\f?\16?\u02bc\13?\3@\3@\3@\3@\3@\3@")
        buf.write("\7@\u02c4\n@\f@\16@\u02c7\13@\3A\3A\3A\3A\3A\3A\7A\u02cf")
        buf.write("\nA\fA\16A\u02d2\13A\3B\3B\3B\3B\3B\3B\7B\u02da\nB\fB")
        buf.write("\16B\u02dd\13B\3C\3C\3C\5C\u02e2\nC\3D\3D\3D\3D\3D\3D")
        buf.write("\3D\3D\3D\3D\3D\5D\u02ef\nD\3D\3D\3D\3D\3D\3D\7D\u02f7")
        buf.write("\nD\fD\16D\u02fa\13D\3E\3E\3E\3E\3E\3E\5E\u0302\nE\3E")
        buf.write("\2\nRvz|~\u0080\u0082\u0086F\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\2\t\3")
        buf.write("\2\13\16\3\2\66\67\3\2&+\3\2\34!\3\2\27\30\3\2\31\33\4")
        buf.write("\2\30\30$$\2\u032b\2\u0096\3\2\2\2\4\u009b\3\2\2\2\6\u00a1")
        buf.write("\3\2\2\2\b\u00ac\3\2\2\2\n\u00ae\3\2\2\2\f\u00b9\3\2\2")
        buf.write("\2\16\u00c1\3\2\2\2\20\u00c6\3\2\2\2\22\u00c8\3\2\2\2")
        buf.write("\24\u00cc\3\2\2\2\26\u00d5\3\2\2\2\30\u00d7\3\2\2\2\32")
        buf.write("\u00dc\3\2\2\2\34\u00e2\3\2\2\2\36\u00e9\3\2\2\2 \u0108")
        buf.write("\3\2\2\2\"\u010e\3\2\2\2$\u0110\3\2\2\2&\u0125\3\2\2\2")
        buf.write("(\u0127\3\2\2\2*\u012a\3\2\2\2,\u0146\3\2\2\2.\u015d\3")
        buf.write("\2\2\2\60\u015f\3\2\2\2\62\u0171\3\2\2\2\64\u0177\3\2")
        buf.write("\2\2\66\u0179\3\2\2\28\u017c\3\2\2\2:\u0181\3\2\2\2<\u0187")
        buf.write("\3\2\2\2>\u0190\3\2\2\2@\u0194\3\2\2\2B\u019f\3\2\2\2")
        buf.write("D\u01a1\3\2\2\2F\u01ad\3\2\2\2H\u01af\3\2\2\2J\u01b3\3")
        buf.write("\2\2\2L\u01ba\3\2\2\2N\u01c3\3\2\2\2P\u01c5\3\2\2\2R\u01ca")
        buf.write("\3\2\2\2T\u01da\3\2\2\2V\u01dc\3\2\2\2X\u01de\3\2\2\2")
        buf.write("Z\u01f9\3\2\2\2\\\u01fb\3\2\2\2^\u020c\3\2\2\2`\u0219")
        buf.write("\3\2\2\2b\u021d\3\2\2\2d\u0229\3\2\2\2f\u022d\3\2\2\2")
        buf.write("h\u023b\3\2\2\2j\u024d\3\2\2\2l\u025f\3\2\2\2n\u0272\3")
        buf.write("\2\2\2p\u0275\3\2\2\2r\u0278\3\2\2\2t\u027e\3\2\2\2v\u0289")
        buf.write("\3\2\2\2x\u02a5\3\2\2\2z\u02a7\3\2\2\2|\u02b2\3\2\2\2")
        buf.write("~\u02bd\3\2\2\2\u0080\u02c8\3\2\2\2\u0082\u02d3\3\2\2")
        buf.write("\2\u0084\u02e1\3\2\2\2\u0086\u02e3\3\2\2\2\u0088\u0301")
        buf.write("\3\2\2\2\u008a\u008e\7\64\2\2\u008b\u008d\7:\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008e\u008f\3\2\2\2\u008f\u0097\3\2\2\2\u0090\u008e\3")
        buf.write("\2\2\2\u0091\u0093\7:\2\2\u0092\u0091\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0097\3\2\2\2\u0096\u008a\3\2\2\2\u0096\u0092\3\2\2\2")
        buf.write("\u0097\3\3\2\2\2\u0098\u009a\7:\2\2\u0099\u0098\3\2\2")
        buf.write("\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e")
        buf.write("\u009f\5\6\4\2\u009f\u00a0\7\2\2\3\u00a0\5\3\2\2\2\u00a1")
        buf.write("\u00a6\5\16\b\2\u00a2\u00a5\5\16\b\2\u00a3\u00a5\7:\2")
        buf.write("\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8")
        buf.write("\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("\7\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ad\5\n\6\2\u00aa")
        buf.write("\u00ad\58\35\2\u00ab\u00ad\7\66\2\2\u00ac\u00a9\3\2\2")
        buf.write("\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\t\3\2")
        buf.write("\2\2\u00ae\u00af\t\2\2\2\u00af\13\3\2\2\2\u00b0\u00ba")
        buf.write("\7\67\2\2\u00b1\u00ba\78\2\2\u00b2\u00ba\79\2\2\u00b3")
        buf.write("\u00ba\7\24\2\2\u00b4\u00ba\7\25\2\2\u00b5\u00ba\7\26")
        buf.write("\2\2\u00b6\u00ba\5\66\34\2\u00b7\u00ba\5D#\2\u00b8\u00ba")
        buf.write("\5J&\2\u00b9\u00b0\3\2\2\2\u00b9\u00b1\3\2\2\2\u00b9\u00b2")
        buf.write("\3\2\2\2\u00b9\u00b3\3\2\2\2\u00b9\u00b4\3\2\2\2\u00b9")
        buf.write("\u00b5\3\2\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2")
        buf.write("\u00b9\u00b8\3\2\2\2\u00ba\r\3\2\2\2\u00bb\u00c2\5\26")
        buf.write("\f\2\u00bc\u00c2\5\24\13\2\u00bd\u00c2\5\36\20\2\u00be")
        buf.write("\u00c2\5$\23\2\u00bf\u00c2\5*\26\2\u00c0\u00c2\5,\27\2")
        buf.write("\u00c1\u00bb\3\2\2\2\u00c1\u00bc\3\2\2\2\u00c1\u00bd\3")
        buf.write("\2\2\2\u00c1\u00be\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c2\17\3\2\2\2\u00c3\u00c7\5\24\13\2\u00c4")
        buf.write("\u00c7\5\26\f\2\u00c5\u00c7\5N(\2\u00c6\u00c3\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\21\3\2")
        buf.write("\2\2\u00c8\u00ca\5\20\t\2\u00c9\u00cb\5\22\n\2\u00ca\u00c9")
        buf.write("\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\23\3\2\2\2\u00cc\u00cd")
        buf.write("\7\17\2\2\u00cd\u00ce\7\66\2\2\u00ce\u00cf\7%\2\2\u00cf")
        buf.write("\u00d0\5z>\2\u00d0\u00d1\5\2\2\2\u00d1\25\3\2\2\2\u00d2")
        buf.write("\u00d6\5\30\r\2\u00d3\u00d6\5\32\16\2\u00d4\u00d6\5\34")
        buf.write("\17\2\u00d5\u00d2\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6\27\3\2\2\2\u00d7\u00d8\7\20\2\2\u00d8\u00d9")
        buf.write("\7\66\2\2\u00d9\u00da\5\b\5\2\u00da\u00db\5\2\2\2\u00db")
        buf.write("\31\3\2\2\2\u00dc\u00dd\7\20\2\2\u00dd\u00de\7\66\2\2")
        buf.write("\u00de\u00df\7%\2\2\u00df\u00e0\5z>\2\u00e0\u00e1\5\2")
        buf.write("\2\2\u00e1\33\3\2\2\2\u00e2\u00e3\7\20\2\2\u00e3\u00e4")
        buf.write("\7\66\2\2\u00e4\u00e5\5\b\5\2\u00e5\u00e6\7%\2\2\u00e6")
        buf.write("\u00e7\5z>\2\u00e7\u00e8\5\2\2\2\u00e8\35\3\2\2\2\u00e9")
        buf.write("\u00ea\7\7\2\2\u00ea\u00eb\7\66\2\2\u00eb\u00ed\7-\2\2")
        buf.write("\u00ec\u00ee\5 \21\2\u00ed\u00ec\3\2\2\2\u00ed\u00ee\3")
        buf.write("\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1\7.\2\2\u00f0\u00f2")
        buf.write("\5\b\5\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\u00f7\7\61\2\2\u00f4\u00f6\7:\2\2")
        buf.write("\u00f5\u00f4\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3")
        buf.write("\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7")
        buf.write("\3\2\2\2\u00fa\u00fc\5\22\n\2\u00fb\u00fa\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\7\62\2")
        buf.write("\2\u00fe\u00ff\5\2\2\2\u00ff\37\3\2\2\2\u0100\u0101\5")
        buf.write("\"\22\2\u0101\u0102\5\b\5\2\u0102\u0103\7\63\2\2\u0103")
        buf.write("\u0104\5 \21\2\u0104\u0109\3\2\2\2\u0105\u0106\5\"\22")
        buf.write("\2\u0106\u0107\5\b\5\2\u0107\u0109\3\2\2\2\u0108\u0100")
        buf.write("\3\2\2\2\u0108\u0105\3\2\2\2\u0109!\3\2\2\2\u010a\u010b")
        buf.write("\7\66\2\2\u010b\u010c\7\63\2\2\u010c\u010f\5\"\22\2\u010d")
        buf.write("\u010f\7\66\2\2\u010e\u010a\3\2\2\2\u010e\u010d\3\2\2")
        buf.write("\2\u010f#\3\2\2\2\u0110\u0111\7\b\2\2\u0111\u0112\7\66")
        buf.write("\2\2\u0112\u0113\7\t\2\2\u0113\u0117\7\61\2\2\u0114\u0116")
        buf.write("\7:\2\2\u0115\u0114\3\2\2\2\u0116\u0119\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011a\3\2\2\2")
        buf.write("\u0119\u0117\3\2\2\2\u011a\u011b\5&\24\2\u011b\u011c\7")
        buf.write("\62\2\2\u011c\u011d\5\2\2\2\u011d%\3\2\2\2\u011e\u011f")
        buf.write("\5(\25\2\u011f\u0120\5\2\2\2\u0120\u0121\5&\24\2\u0121")
        buf.write("\u0126\3\2\2\2\u0122\u0123\5(\25\2\u0123\u0124\5\2\2\2")
        buf.write("\u0124\u0126\3\2\2\2\u0125\u011e\3\2\2\2\u0125\u0122\3")
        buf.write("\2\2\2\u0126\'\3\2\2\2\u0127\u0128\7\66\2\2\u0128\u0129")
        buf.write("\5\b\5\2\u0129)\3\2\2\2\u012a\u012b\7\7\2\2\u012b\u012c")
        buf.write("\7-\2\2\u012c\u012d\7\66\2\2\u012d\u012e\7\66\2\2\u012e")
        buf.write("\u012f\7.\2\2\u012f\u0130\3\2\2\2\u0130\u0131\7\66\2\2")
        buf.write("\u0131\u0133\7-\2\2\u0132\u0134\5 \21\2\u0133\u0132\3")
        buf.write("\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137")
        buf.write("\7.\2\2\u0136\u0138\5\b\5\2\u0137\u0136\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013d\7\61\2")
        buf.write("\2\u013a\u013c\7:\2\2\u013b\u013a\3\2\2\2\u013c\u013f")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0142\5\22\n")
        buf.write("\2\u0141\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143")
        buf.write("\3\2\2\2\u0143\u0144\7\62\2\2\u0144\u0145\5\2\2\2\u0145")
        buf.write("+\3\2\2\2\u0146\u0147\7\b\2\2\u0147\u0148\7\66\2\2\u0148")
        buf.write("\u0149\7\n\2\2\u0149\u014d\7\61\2\2\u014a\u014c\7:\2\2")
        buf.write("\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3")
        buf.write("\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u0150\u0151\5.\30\2\u0151\u0152\3\2\2\2\u0152")
        buf.write("\u0153\7\62\2\2\u0153\u0154\3\2\2\2\u0154\u0155\5\2\2")
        buf.write("\2\u0155-\3\2\2\2\u0156\u0157\5\60\31\2\u0157\u0158\5")
        buf.write("\2\2\2\u0158\u0159\5.\30\2\u0159\u015e\3\2\2\2\u015a\u015b")
        buf.write("\5\60\31\2\u015b\u015c\5\2\2\2\u015c\u015e\3\2\2\2\u015d")
        buf.write("\u0156\3\2\2\2\u015d\u015a\3\2\2\2\u015e/\3\2\2\2\u015f")
        buf.write("\u0160\7\66\2\2\u0160\u0162\7-\2\2\u0161\u0163\5\62\32")
        buf.write("\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164")
        buf.write("\3\2\2\2\u0164\u0165\7.\2\2\u0165\u0167\3\2\2\2\u0166")
        buf.write("\u0168\5\b\5\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168\61\3\2\2\2\u0169\u016a\5\64\33\2\u016a\u016b\5")
        buf.write("\b\5\2\u016b\u016c\7\63\2\2\u016c\u016d\5\62\32\2\u016d")
        buf.write("\u0172\3\2\2\2\u016e\u016f\5\64\33\2\u016f\u0170\5\b\5")
        buf.write("\2\u0170\u0172\3\2\2\2\u0171\u0169\3\2\2\2\u0171\u016e")
        buf.write("\3\2\2\2\u0172\63\3\2\2\2\u0173\u0174\7\66\2\2\u0174\u0175")
        buf.write("\7\63\2\2\u0175\u0178\5\64\33\2\u0176\u0178\7\66\2\2\u0177")
        buf.write("\u0173\3\2\2\2\u0177\u0176\3\2\2\2\u0178\65\3\2\2\2\u0179")
        buf.write("\u017a\58\35\2\u017a\u017b\5<\37\2\u017b\67\3\2\2\2\u017c")
        buf.write("\u017f\5:\36\2\u017d\u0180\5\n\6\2\u017e\u0180\7\66\2")
        buf.write("\2\u017f\u017d\3\2\2\2\u017f\u017e\3\2\2\2\u01809\3\2")
        buf.write("\2\2\u0181\u0182\7/\2\2\u0182\u0183\t\3\2\2\u0183\u0185")
        buf.write("\7\60\2\2\u0184\u0186\5:\36\2\u0185\u0184\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186;\3\2\2\2\u0187\u0188\7\61\2\2\u0188")
        buf.write("\u0189\5> \2\u0189\u018a\7\62\2\2\u018a=\3\2\2\2\u018b")
        buf.write("\u018c\5@!\2\u018c\u018d\7\63\2\2\u018d\u018e\5> \2\u018e")
        buf.write("\u0191\3\2\2\2\u018f\u0191\5@!\2\u0190\u018b\3\2\2\2\u0190")
        buf.write("\u018f\3\2\2\2\u0191?\3\2\2\2\u0192\u0195\5B\"\2\u0193")
        buf.write("\u0195\5<\37\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195A\3\2\2\2\u0196\u01a0\7\66\2\2\u0197\u01a0\7\67")
        buf.write("\2\2\u0198\u01a0\78\2\2\u0199\u01a0\79\2\2\u019a\u01a0")
        buf.write("\7\24\2\2\u019b\u01a0\7\25\2\2\u019c\u01a0\7\26\2\2\u019d")
        buf.write("\u01a0\5D#\2\u019e\u01a0\5J&\2\u019f\u0196\3\2\2\2\u019f")
        buf.write("\u0197\3\2\2\2\u019f\u0198\3\2\2\2\u019f\u0199\3\2\2\2")
        buf.write("\u019f\u019a\3\2\2\2\u019f\u019b\3\2\2\2\u019f\u019c\3")
        buf.write("\2\2\2\u019f\u019d\3\2\2\2\u019f\u019e\3\2\2\2\u01a0C")
        buf.write("\3\2\2\2\u01a1\u01a2\7\66\2\2\u01a2\u01a4\7\61\2\2\u01a3")
        buf.write("\u01a5\5F$\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a7\7\62\2\2\u01a7E\3\2\2\2\u01a8")
        buf.write("\u01a9\5H%\2\u01a9\u01aa\7\63\2\2\u01aa\u01ab\5F$\2\u01ab")
        buf.write("\u01ae\3\2\2\2\u01ac\u01ae\5H%\2\u01ad\u01a8\3\2\2\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01aeG\3\2\2\2\u01af\u01b0\7\66\2\2\u01b0")
        buf.write("\u01b1\7\65\2\2\u01b1\u01b2\5z>\2\u01b2I\3\2\2\2\u01b3")
        buf.write("\u01b4\7\66\2\2\u01b4\u01b6\7-\2\2\u01b5\u01b7\5x=\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2")
        buf.write("\u01b8\u01b9\7.\2\2\u01b9K\3\2\2\2\u01ba\u01bb\5z>\2\u01bb")
        buf.write("M\3\2\2\2\u01bc\u01c4\5P)\2\u01bd\u01c4\5X-\2\u01be\u01c4")
        buf.write("\5d\63\2\u01bf\u01c4\5n8\2\u01c0\u01c4\5p9\2\u01c1\u01c4")
        buf.write("\5r:\2\u01c2\u01c4\5t;\2\u01c3\u01bc\3\2\2\2\u01c3\u01bd")
        buf.write("\3\2\2\2\u01c3\u01be\3\2\2\2\u01c3\u01bf\3\2\2\2\u01c3")
        buf.write("\u01c0\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c2\3\2\2\2")
        buf.write("\u01c4O\3\2\2\2\u01c5\u01c6\5R*\2\u01c6\u01c7\5T+\2\u01c7")
        buf.write("\u01c8\5V,\2\u01c8\u01c9\5\2\2\2\u01c9Q\3\2\2\2\u01ca")
        buf.write("\u01cb\b*\1\2\u01cb\u01cc\7\66\2\2\u01cc\u01d7\3\2\2\2")
        buf.write("\u01cd\u01ce\f\5\2\2\u01ce\u01cf\7/\2\2\u01cf\u01d0\5")
        buf.write("z>\2\u01d0\u01d1\7\60\2\2\u01d1\u01d6\3\2\2\2\u01d2\u01d3")
        buf.write("\f\4\2\2\u01d3\u01d4\7,\2\2\u01d4\u01d6\7\66\2\2\u01d5")
        buf.write("\u01cd\3\2\2\2\u01d5\u01d2\3\2\2\2\u01d6\u01d9\3\2\2\2")
        buf.write("\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8S\3\2\2")
        buf.write("\2\u01d9\u01d7\3\2\2\2\u01da\u01db\t\4\2\2\u01dbU\3\2")
        buf.write("\2\2\u01dc\u01dd\5z>\2\u01ddW\3\2\2\2\u01de\u01df\7\3")
        buf.write("\2\2\u01df\u01e0\7-\2\2\u01e0\u01e1\5L\'\2\u01e1\u01e2")
        buf.write("\7.\2\2\u01e2\u01e6\7\61\2\2\u01e3\u01e5\7:\2\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2")
        buf.write("\u01e6\u01e7\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3")
        buf.write("\2\2\2\u01e9\u01eb\5\22\n\2\u01ea\u01e9\3\2\2\2\u01ea")
        buf.write("\u01eb\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ee\7\62\2")
        buf.write("\2\u01ed\u01ef\5Z.\2\u01ee\u01ed\3\2\2\2\u01ee\u01ef\3")
        buf.write("\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01f2\5^\60\2\u01f1\u01f0")
        buf.write("\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("\u01f4\5\2\2\2\u01f4Y\3\2\2\2\u01f5\u01f6\5\\/\2\u01f6")
        buf.write("\u01f7\5Z.\2\u01f7\u01fa\3\2\2\2\u01f8\u01fa\5\\/\2\u01f9")
        buf.write("\u01f5\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fa[\3\2\2\2\u01fb")
        buf.write("\u01fc\7\4\2\2\u01fc\u01fd\7\3\2\2\u01fd\u01fe\7-\2\2")
        buf.write("\u01fe\u01ff\5L\'\2\u01ff\u0200\7.\2\2\u0200\u0204\7\61")
        buf.write("\2\2\u0201\u0203\7:\2\2\u0202\u0201\3\2\2\2\u0203\u0206")
        buf.write("\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("\u0208\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0209\5\22\n")
        buf.write("\2\u0208\u0207\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020b\7\62\2\2\u020b]\3\2\2\2\u020c\u020d")
        buf.write("\7\4\2\2\u020d\u0211\7\61\2\2\u020e\u0210\7:\2\2\u020f")
        buf.write("\u020e\3\2\2\2\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2")
        buf.write("\u0211\u0212\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3")
        buf.write("\2\2\2\u0214\u0216\5\22\n\2\u0215\u0214\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0218\7\62\2")
        buf.write("\2\u0218_\3\2\2\2\u0219\u021a\7\66\2\2\u021a\u021b\5T")
        buf.write("+\2\u021b\u021c\5V,\2\u021ca\3\2\2\2\u021d\u021e\7\20")
        buf.write("\2\2\u021e\u0220\7\66\2\2\u021f\u0221\5\b\5\2\u0220\u021f")
        buf.write("\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0222\3\2\2\2\u0222")
        buf.write("\u0223\7%\2\2\u0223\u0224\5z>\2\u0224c\3\2\2\2\u0225\u022a")
        buf.write("\5f\64\2\u0226\u022a\5h\65\2\u0227\u022a\5j\66\2\u0228")
        buf.write("\u022a\5l\67\2\u0229\u0225\3\2\2\2\u0229\u0226\3\2\2\2")
        buf.write("\u0229\u0227\3\2\2\2\u0229\u0228\3\2\2\2\u022a\u022b\3")
        buf.write("\2\2\2\u022b\u022c\5\2\2\2\u022ce\3\2\2\2\u022d\u022e")
        buf.write("\7\5\2\2\u022e\u022f\5L\'\2\u022f\u0233\7\61\2\2\u0230")
        buf.write("\u0232\7:\2\2\u0231\u0230\3\2\2\2\u0232\u0235\3\2\2\2")
        buf.write("\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0237\3")
        buf.write("\2\2\2\u0235\u0233\3\2\2\2\u0236\u0238\5\22\n\2\u0237")
        buf.write("\u0236\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239\3\2\2\2")
        buf.write("\u0239\u023a\7\62\2\2\u023ag\3\2\2\2\u023b\u023c\7\5\2")
        buf.write("\2\u023c\u023d\5b\62\2\u023d\u023e\5\2\2\2\u023e\u023f")
        buf.write("\5L\'\2\u023f\u0240\5\2\2\2\u0240\u0241\5`\61\2\u0241")
        buf.write("\u0245\7\61\2\2\u0242\u0244\7:\2\2\u0243\u0242\3\2\2\2")
        buf.write("\u0244\u0247\3\2\2\2\u0245\u0243\3\2\2\2\u0245\u0246\3")
        buf.write("\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245\3\2\2\2\u0248\u024a")
        buf.write("\5\22\n\2\u0249\u0248\3\2\2\2\u0249\u024a\3\2\2\2\u024a")
        buf.write("\u024b\3\2\2\2\u024b\u024c\7\62\2\2\u024ci\3\2\2\2\u024d")
        buf.write("\u024e\7\5\2\2\u024e\u024f\5`\61\2\u024f\u0250\5\2\2\2")
        buf.write("\u0250\u0251\5L\'\2\u0251\u0252\5\2\2\2\u0252\u0253\5")
        buf.write("`\61\2\u0253\u0257\7\61\2\2\u0254\u0256\7:\2\2\u0255\u0254")
        buf.write("\3\2\2\2\u0256\u0259\3\2\2\2\u0257\u0255\3\2\2\2\u0257")
        buf.write("\u0258\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257\3\2\2\2")
        buf.write("\u025a\u025c\5\22\n\2\u025b\u025a\3\2\2\2\u025b\u025c")
        buf.write("\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025e\7\62\2\2\u025e")
        buf.write("k\3\2\2\2\u025f\u0260\7\5\2\2\u0260\u0261\7\66\2\2\u0261")
        buf.write("\u0262\7\63\2\2\u0262\u0263\7\66\2\2\u0263\u0264\7+\2")
        buf.write("\2\u0264\u0265\7\23\2\2\u0265\u0266\5z>\2\u0266\u026a")
        buf.write("\7\61\2\2\u0267\u0269\7:\2\2\u0268\u0267\3\2\2\2\u0269")
        buf.write("\u026c\3\2\2\2\u026a\u0268\3\2\2\2\u026a\u026b\3\2\2\2")
        buf.write("\u026b\u026e\3\2\2\2\u026c\u026a\3\2\2\2\u026d\u026f\5")
        buf.write("\22\n\2\u026e\u026d\3\2\2\2\u026e\u026f\3\2\2\2\u026f")
        buf.write("\u0270\3\2\2\2\u0270\u0271\7\62\2\2\u0271m\3\2\2\2\u0272")
        buf.write("\u0273\7\22\2\2\u0273\u0274\5\2\2\2\u0274o\3\2\2\2\u0275")
        buf.write("\u0276\7\21\2\2\u0276\u0277\5\2\2\2\u0277q\3\2\2\2\u0278")
        buf.write("\u027a\7\6\2\2\u0279\u027b\5z>\2\u027a\u0279\3\2\2\2\u027a")
        buf.write("\u027b\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u027d\5\2\2\2")
        buf.write("\u027ds\3\2\2\2\u027e\u027f\5v<\2\u027f\u0280\5\2\2\2")
        buf.write("\u0280u\3\2\2\2\u0281\u0282\b<\1\2\u0282\u0283\7\66\2")
        buf.write("\2\u0283\u0285\7-\2\2\u0284\u0286\5x=\2\u0285\u0284\3")
        buf.write("\2\2\2\u0285\u0286\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u028a")
        buf.write("\7.\2\2\u0288\u028a\7\66\2\2\u0289\u0281\3\2\2\2\u0289")
        buf.write("\u0288\3\2\2\2\u028a\u029d\3\2\2\2\u028b\u028c\f\7\2\2")
        buf.write("\u028c\u028d\7,\2\2\u028d\u029c\7\66\2\2\u028e\u028f\f")
        buf.write("\6\2\2\u028f\u0290\7,\2\2\u0290\u0291\7\66\2\2\u0291\u0293")
        buf.write("\7-\2\2\u0292\u0294\5x=\2\u0293\u0292\3\2\2\2\u0293\u0294")
        buf.write("\3\2\2\2\u0294\u0295\3\2\2\2\u0295\u029c\7.\2\2\u0296")
        buf.write("\u0297\f\4\2\2\u0297\u0298\7/\2\2\u0298\u0299\5z>\2\u0299")
        buf.write("\u029a\7\60\2\2\u029a\u029c\3\2\2\2\u029b\u028b\3\2\2")
        buf.write("\2\u029b\u028e\3\2\2\2\u029b\u0296\3\2\2\2\u029c\u029f")
        buf.write("\3\2\2\2\u029d\u029b\3\2\2\2\u029d\u029e\3\2\2\2\u029e")
        buf.write("w\3\2\2\2\u029f\u029d\3\2\2\2\u02a0\u02a1\5z>\2\u02a1")
        buf.write("\u02a2\7\63\2\2\u02a2\u02a3\5x=\2\u02a3\u02a6\3\2\2\2")
        buf.write("\u02a4\u02a6\5z>\2\u02a5\u02a0\3\2\2\2\u02a5\u02a4\3\2")
        buf.write("\2\2\u02a6y\3\2\2\2\u02a7\u02a8\b>\1\2\u02a8\u02a9\5|")
        buf.write("?\2\u02a9\u02af\3\2\2\2\u02aa\u02ab\f\4\2\2\u02ab\u02ac")
        buf.write("\7#\2\2\u02ac\u02ae\5|?\2\u02ad\u02aa\3\2\2\2\u02ae\u02b1")
        buf.write("\3\2\2\2\u02af\u02ad\3\2\2\2\u02af\u02b0\3\2\2\2\u02b0")
        buf.write("{\3\2\2\2\u02b1\u02af\3\2\2\2\u02b2\u02b3\b?\1\2\u02b3")
        buf.write("\u02b4\5~@\2\u02b4\u02ba\3\2\2\2\u02b5\u02b6\f\4\2\2\u02b6")
        buf.write("\u02b7\7\"\2\2\u02b7\u02b9\5~@\2\u02b8\u02b5\3\2\2\2\u02b9")
        buf.write("\u02bc\3\2\2\2\u02ba\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2")
        buf.write("\u02bb}\3\2\2\2\u02bc\u02ba\3\2\2\2\u02bd\u02be\b@\1\2")
        buf.write("\u02be\u02bf\5\u0080A\2\u02bf\u02c5\3\2\2\2\u02c0\u02c1")
        buf.write("\f\4\2\2\u02c1\u02c2\t\5\2\2\u02c2\u02c4\5\u0080A\2\u02c3")
        buf.write("\u02c0\3\2\2\2\u02c4\u02c7\3\2\2\2\u02c5\u02c3\3\2\2\2")
        buf.write("\u02c5\u02c6\3\2\2\2\u02c6\177\3\2\2\2\u02c7\u02c5\3\2")
        buf.write("\2\2\u02c8\u02c9\bA\1\2\u02c9\u02ca\5\u0082B\2\u02ca\u02d0")
        buf.write("\3\2\2\2\u02cb\u02cc\f\4\2\2\u02cc\u02cd\t\6\2\2\u02cd")
        buf.write("\u02cf\5\u0082B\2\u02ce\u02cb\3\2\2\2\u02cf\u02d2\3\2")
        buf.write("\2\2\u02d0\u02ce\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u0081")
        buf.write("\3\2\2\2\u02d2\u02d0\3\2\2\2\u02d3\u02d4\bB\1\2\u02d4")
        buf.write("\u02d5\5\u0084C\2\u02d5\u02db\3\2\2\2\u02d6\u02d7\f\4")
        buf.write("\2\2\u02d7\u02d8\t\7\2\2\u02d8\u02da\5\u0084C\2\u02d9")
        buf.write("\u02d6\3\2\2\2\u02da\u02dd\3\2\2\2\u02db\u02d9\3\2\2\2")
        buf.write("\u02db\u02dc\3\2\2\2\u02dc\u0083\3\2\2\2\u02dd\u02db\3")
        buf.write("\2\2\2\u02de\u02df\t\b\2\2\u02df\u02e2\5\u0084C\2\u02e0")
        buf.write("\u02e2\5\u0086D\2\u02e1\u02de\3\2\2\2\u02e1\u02e0\3\2")
        buf.write("\2\2\u02e2\u0085\3\2\2\2\u02e3\u02e4\bD\1\2\u02e4\u02e5")
        buf.write("\5\u0088E\2\u02e5\u02f8\3\2\2\2\u02e6\u02e7\f\6\2\2\u02e7")
        buf.write("\u02e8\7,\2\2\u02e8\u02f7\7\66\2\2\u02e9\u02ea\f\5\2\2")
        buf.write("\u02ea\u02eb\7,\2\2\u02eb\u02ec\7\66\2\2\u02ec\u02ee\7")
        buf.write("-\2\2\u02ed\u02ef\5x=\2\u02ee\u02ed\3\2\2\2\u02ee\u02ef")
        buf.write("\3\2\2\2\u02ef\u02f0\3\2\2\2\u02f0\u02f7\7.\2\2\u02f1")
        buf.write("\u02f2\f\4\2\2\u02f2\u02f3\7/\2\2\u02f3\u02f4\5z>\2\u02f4")
        buf.write("\u02f5\7\60\2\2\u02f5\u02f7\3\2\2\2\u02f6\u02e6\3\2\2")
        buf.write("\2\u02f6\u02e9\3\2\2\2\u02f6\u02f1\3\2\2\2\u02f7\u02fa")
        buf.write("\3\2\2\2\u02f8\u02f6\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9")
        buf.write("\u0087\3\2\2\2\u02fa\u02f8\3\2\2\2\u02fb\u0302\7\66\2")
        buf.write("\2\u02fc\u0302\5\f\7\2\u02fd\u02fe\7-\2\2\u02fe\u02ff")
        buf.write("\5z>\2\u02ff\u0300\7.\2\2\u0300\u0302\3\2\2\2\u0301\u02fb")
        buf.write("\3\2\2\2\u0301\u02fc\3\2\2\2\u0301\u02fd\3\2\2\2\u0302")
        buf.write("\u0089\3\2\2\2O\u008e\u0094\u0096\u009b\u00a4\u00a6\u00ac")
        buf.write("\u00b9\u00c1\u00c6\u00ca\u00d5\u00ed\u00f1\u00f7\u00fb")
        buf.write("\u0108\u010e\u0117\u0125\u0133\u0137\u013d\u0141\u014d")
        buf.write("\u015d\u0162\u0167\u0171\u0177\u017f\u0185\u0190\u0194")
        buf.write("\u019f\u01a4\u01ad\u01b6\u01c3\u01d5\u01d7\u01e6\u01ea")
        buf.write("\u01ee\u01f1\u01f9\u0204\u0208\u0211\u0215\u0220\u0229")
        buf.write("\u0233\u0237\u0245\u0249\u0257\u025b\u026a\u026e\u027a")
        buf.write("\u0285\u0289\u0293\u029b\u029d\u02a5\u02af\u02ba\u02c5")
        buf.write("\u02d0\u02db\u02e1\u02ee\u02f6\u02f8\u0301")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "':='", "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQ", "INEQ", "LT", "LTE", "GT", "GTE", "AND", 
                      "OR", "NOT", "ASSIGNINIT", "ASSIGNADD", "ASSIGNSUB", 
                      "ASSIGNMUL", "ASSIGNDIV", "ASSIGNMOD", "ASSIGN", "DOT", 
                      "LP", "RP", "LSB", "RSB", "LB", "RB", "CM", "SC", 
                      "CL", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "NEWLINE", "WS", "SINGLE_LINE_COMMENT", "MULTIPLE_LINE_COMMENT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_end_statement1 = 0
    RULE_program = 1
    RULE_list_declaration = 2
    RULE_data_type = 3
    RULE_primitive_type = 4
    RULE_literal = 5
    RULE_declaration = 6
    RULE_block_statement = 7
    RULE_list_block_statement = 8
    RULE_const_declare = 9
    RULE_variable_declare = 10
    RULE_var_decl1 = 11
    RULE_var_decl2 = 12
    RULE_var_decl3 = 13
    RULE_function_declare = 14
    RULE_input_param = 15
    RULE_list_input_variable = 16
    RULE_struct_declare = 17
    RULE_list_struct_type = 18
    RULE_struct_type = 19
    RULE_method_declare = 20
    RULE_interface_declare = 21
    RULE_list_interface_method = 22
    RULE_interface_method = 23
    RULE_param_method_interface = 24
    RULE_list_input_method = 25
    RULE_array_literal = 26
    RULE_type_array = 27
    RULE_array_index = 28
    RULE_list_array = 29
    RULE_list_array_block = 30
    RULE_array_block = 31
    RULE_array_element = 32
    RULE_struct_literal = 33
    RULE_list_struct_element = 34
    RULE_struct_element = 35
    RULE_function_literal = 36
    RULE_condition = 37
    RULE_statement = 38
    RULE_assign_statement = 39
    RULE_lhs_assign_statement = 40
    RULE_assign_sign = 41
    RULE_rhs_assign_statement = 42
    RULE_if_statement = 43
    RULE_multiple_else_if = 44
    RULE_else_if_statement = 45
    RULE_else_statement = 46
    RULE_assign_scalar = 47
    RULE_var_scalar = 48
    RULE_for_statement = 49
    RULE_for1 = 50
    RULE_for2 = 51
    RULE_for3 = 52
    RULE_for4 = 53
    RULE_break_statement = 54
    RULE_continue_statement = 55
    RULE_return_statement = 56
    RULE_call_statement = 57
    RULE_call_component = 58
    RULE_list_expression = 59
    RULE_expression = 60
    RULE_expression1 = 61
    RULE_expression2 = 62
    RULE_expression3 = 63
    RULE_expression4 = 64
    RULE_expression5 = 65
    RULE_expression6 = 66
    RULE_expression7 = 67

    ruleNames =  [ "end_statement1", "program", "list_declaration", "data_type", 
                   "primitive_type", "literal", "declaration", "block_statement", 
                   "list_block_statement", "const_declare", "variable_declare", 
                   "var_decl1", "var_decl2", "var_decl3", "function_declare", 
                   "input_param", "list_input_variable", "struct_declare", 
                   "list_struct_type", "struct_type", "method_declare", 
                   "interface_declare", "list_interface_method", "interface_method", 
                   "param_method_interface", "list_input_method", "array_literal", 
                   "type_array", "array_index", "list_array", "list_array_block", 
                   "array_block", "array_element", "struct_literal", "list_struct_element", 
                   "struct_element", "function_literal", "condition", "statement", 
                   "assign_statement", "lhs_assign_statement", "assign_sign", 
                   "rhs_assign_statement", "if_statement", "multiple_else_if", 
                   "else_if_statement", "else_statement", "assign_scalar", 
                   "var_scalar", "for_statement", "for1", "for2", "for3", 
                   "for4", "break_statement", "continue_statement", "return_statement", 
                   "call_statement", "call_component", "list_expression", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQ=26
    INEQ=27
    LT=28
    LTE=29
    GT=30
    GTE=31
    AND=32
    OR=33
    NOT=34
    ASSIGNINIT=35
    ASSIGNADD=36
    ASSIGNSUB=37
    ASSIGNMUL=38
    ASSIGNDIV=39
    ASSIGNMOD=40
    ASSIGN=41
    DOT=42
    LP=43
    RP=44
    LSB=45
    RSB=46
    LB=47
    RB=48
    CM=49
    SC=50
    CL=51
    ID=52
    INT_LIT=53
    FLOAT_LIT=54
    STRING_LIT=55
    NEWLINE=56
    WS=57
    SINGLE_LINE_COMMENT=58
    MULTIPLE_LINE_COMMENT=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class End_statement1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SC(self):
            return self.getToken(MiniGoParser.SC, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_statement1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_statement1" ):
                return visitor.visitEnd_statement1(self)
            else:
                return visitor.visitChildren(self)




    def end_statement1(self):

        localctx = MiniGoParser.End_statement1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_end_statement1)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(MiniGoParser.SC)
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 137
                        self.match(MiniGoParser.NEWLINE) 
                    self.state = 142
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 143
                        self.match(MiniGoParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 146 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_declarationContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 150
                self.match(MiniGoParser.NEWLINE)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.list_declaration()
            self.state = 157
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclarationContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declaration" ):
                return visitor.visitList_declaration(self)
            else:
                return visitor.visitChildren(self)




    def list_declaration(self):

        localctx = MiniGoParser.List_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.declaration()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 162
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 160
                    self.declaration()
                    pass
                elif token in [MiniGoParser.NEWLINE]:
                    self.state = 161
                    self.match(MiniGoParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_data_type)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.type_array()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def function_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Function_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 180
                self.array_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 181
                self.struct_literal()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 182
                self.function_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declareContext,0)


        def const_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declareContext,0)


        def function_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declareContext,0)


        def struct_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declareContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declareContext,0)


        def interface_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declareContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaration)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.variable_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.const_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.function_declare()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.struct_declare()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.method_declare()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.interface_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declareContext,0)


        def variable_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declareContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MiniGoParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block_statement)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.const_declare()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.variable_declare()
                pass
            elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_block_statement" ):
                return visitor.visitList_block_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_block_statement(self):

        localctx = MiniGoParser.List_block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.block_statement()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 199
                self.list_block_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(MiniGoParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declare" ):
                return visitor.visitConst_declare(self)
            else:
                return visitor.visitChildren(self)




    def const_declare(self):

        localctx = MiniGoParser.Const_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_const_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MiniGoParser.CONST)
            self.state = 203
            self.match(MiniGoParser.ID)
            self.state = 204
            self.match(MiniGoParser.ASSIGNINIT)
            self.state = 205
            self.expression(0)
            self.state = 206
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl1(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl1Context,0)


        def var_decl2(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl2Context,0)


        def var_decl3(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl3Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variable_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declare" ):
                return visitor.visitVariable_declare(self)
            else:
                return visitor.visitChildren(self)




    def variable_declare(self):

        localctx = MiniGoParser.Variable_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable_declare)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.var_decl1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.var_decl2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.var_decl3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl1" ):
                return visitor.visitVar_decl1(self)
            else:
                return visitor.visitChildren(self)




    def var_decl1(self):

        localctx = MiniGoParser.Var_decl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_decl1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(MiniGoParser.VAR)
            self.state = 214
            self.match(MiniGoParser.ID)
            self.state = 215
            self.data_type()
            self.state = 216
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(MiniGoParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl2" ):
                return visitor.visitVar_decl2(self)
            else:
                return visitor.visitChildren(self)




    def var_decl2(self):

        localctx = MiniGoParser.Var_decl2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var_decl2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(MiniGoParser.VAR)
            self.state = 219
            self.match(MiniGoParser.ID)
            self.state = 220
            self.match(MiniGoParser.ASSIGNINIT)
            self.state = 221
            self.expression(0)
            self.state = 222
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def ASSIGNINIT(self):
            return self.getToken(MiniGoParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl3" ):
                return visitor.visitVar_decl3(self)
            else:
                return visitor.visitChildren(self)




    def var_decl3(self):

        localctx = MiniGoParser.Var_decl3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var_decl3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MiniGoParser.VAR)
            self.state = 225
            self.match(MiniGoParser.ID)
            self.state = 226
            self.data_type()
            self.state = 227
            self.match(MiniGoParser.ASSIGNINIT)
            self.state = 228
            self.expression(0)
            self.state = 229
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def input_param(self):
            return self.getTypedRuleContext(MiniGoParser.Input_paramContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declare" ):
                return visitor.visitFunction_declare(self)
            else:
                return visitor.visitChildren(self)




    def function_declare(self):

        localctx = MiniGoParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MiniGoParser.FUNC)
            self.state = 232
            self.match(MiniGoParser.ID)
            self.state = 233
            self.match(MiniGoParser.LP)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 234
                self.input_param()


            self.state = 237
            self.match(MiniGoParser.RP)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 238
                self.data_type()


            self.state = 241
            self.match(MiniGoParser.LB)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 242
                self.match(MiniGoParser.NEWLINE)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 248
                self.list_block_statement()


            self.state = 251
            self.match(MiniGoParser.RB)
            self.state = 252
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_input_variable(self):
            return self.getTypedRuleContext(MiniGoParser.List_input_variableContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def input_param(self):
            return self.getTypedRuleContext(MiniGoParser.Input_paramContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_input_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_param" ):
                return visitor.visitInput_param(self)
            else:
                return visitor.visitChildren(self)




    def input_param(self):

        localctx = MiniGoParser.Input_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_input_param)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.list_input_variable()
                self.state = 255
                self.data_type()
                self.state = 256
                self.match(MiniGoParser.CM)
                self.state = 257
                self.input_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.list_input_variable()
                self.state = 260
                self.data_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_input_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_input_variable(self):
            return self.getTypedRuleContext(MiniGoParser.List_input_variableContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_input_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_input_variable" ):
                return visitor.visitList_input_variable(self)
            else:
                return visitor.visitChildren(self)




    def list_input_variable(self):

        localctx = MiniGoParser.List_input_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_input_variable)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(MiniGoParser.ID)
                self.state = 265
                self.match(MiniGoParser.CM)
                self.state = 266
                self.list_input_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def list_struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_typeContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declare" ):
                return visitor.visitStruct_declare(self)
            else:
                return visitor.visitChildren(self)




    def struct_declare(self):

        localctx = MiniGoParser.Struct_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_struct_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(MiniGoParser.TYPE)
            self.state = 271
            self.match(MiniGoParser.ID)
            self.state = 272
            self.match(MiniGoParser.STRUCT)
            self.state = 273
            self.match(MiniGoParser.LB)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 274
                self.match(MiniGoParser.NEWLINE)
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 280
            self.list_struct_type()
            self.state = 281
            self.match(MiniGoParser.RB)
            self.state = 282
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def list_struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_type" ):
                return visitor.visitList_struct_type(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_type(self):

        localctx = MiniGoParser.List_struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_struct_type)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.struct_type()
                self.state = 285
                self.end_statement1()
                self.state = 286
                self.list_struct_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.struct_type()
                self.state = 289
                self.end_statement1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MiniGoParser.ID)
            self.state = 294
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def input_param(self):
            return self.getTypedRuleContext(MiniGoParser.Input_paramContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = MiniGoParser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(MiniGoParser.FUNC)

            self.state = 297
            self.match(MiniGoParser.LP)
            self.state = 298
            self.match(MiniGoParser.ID)
            self.state = 299
            self.match(MiniGoParser.ID)
            self.state = 300
            self.match(MiniGoParser.RP)
            self.state = 302
            self.match(MiniGoParser.ID)
            self.state = 303
            self.match(MiniGoParser.LP)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 304
                self.input_param()


            self.state = 307
            self.match(MiniGoParser.RP)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 308
                self.data_type()


            self.state = 311
            self.match(MiniGoParser.LB)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 312
                self.match(MiniGoParser.NEWLINE)
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 318
                self.list_block_statement()


            self.state = 321
            self.match(MiniGoParser.RB)
            self.state = 322
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def list_interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_methodContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declare" ):
                return visitor.visitInterface_declare(self)
            else:
                return visitor.visitChildren(self)




    def interface_declare(self):

        localctx = MiniGoParser.Interface_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_interface_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(MiniGoParser.TYPE)
            self.state = 325
            self.match(MiniGoParser.ID)
            self.state = 326
            self.match(MiniGoParser.INTERFACE)

            self.state = 327
            self.match(MiniGoParser.LB)

            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 328
                self.match(MiniGoParser.NEWLINE)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 334
            self.list_interface_method()
            self.state = 336
            self.match(MiniGoParser.RB)
            self.state = 338
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def list_interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_methodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_method" ):
                return visitor.visitList_interface_method(self)
            else:
                return visitor.visitChildren(self)




    def list_interface_method(self):

        localctx = MiniGoParser.List_interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_interface_method)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.interface_method()
                self.state = 341
                self.end_statement1()
                self.state = 342
                self.list_interface_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.interface_method()
                self.state = 345
                self.end_statement1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def param_method_interface(self):
            return self.getTypedRuleContext(MiniGoParser.Param_method_interfaceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(MiniGoParser.ID)

            self.state = 350
            self.match(MiniGoParser.LP)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 351
                self.param_method_interface()


            self.state = 354
            self.match(MiniGoParser.RP)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 356
                self.data_type()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_method_interfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_input_method(self):
            return self.getTypedRuleContext(MiniGoParser.List_input_methodContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def param_method_interface(self):
            return self.getTypedRuleContext(MiniGoParser.Param_method_interfaceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_method_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_method_interface" ):
                return visitor.visitParam_method_interface(self)
            else:
                return visitor.visitChildren(self)




    def param_method_interface(self):

        localctx = MiniGoParser.Param_method_interfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_param_method_interface)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.list_input_method()
                self.state = 360
                self.data_type()
                self.state = 361
                self.match(MiniGoParser.CM)
                self.state = 362
                self.param_method_interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.list_input_method()
                self.state = 365
                self.data_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_input_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_input_method(self):
            return self.getTypedRuleContext(MiniGoParser.List_input_methodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_input_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_input_method" ):
                return visitor.visitList_input_method(self)
            else:
                return visitor.visitChildren(self)




    def list_input_method(self):

        localctx = MiniGoParser.List_input_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_input_method)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(MiniGoParser.ID)
                self.state = 370
                self.match(MiniGoParser.CM)
                self.state = 371
                self.list_input_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def list_array(self):
            return self.getTypedRuleContext(MiniGoParser.List_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.type_array()
            self.state = 376
            self.list_array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_index(self):
            return self.getTypedRuleContext(MiniGoParser.Array_indexContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_array" ):
                return visitor.visitType_array(self)
            else:
                return visitor.visitChildren(self)




    def type_array(self):

        localctx = MiniGoParser.Type_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_type_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.array_index()
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 379
                self.primitive_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 380
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_index(self):
            return self.getTypedRuleContext(MiniGoParser.Array_indexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = MiniGoParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_array_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(MiniGoParser.LSB)
            self.state = 384
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 385
            self.match(MiniGoParser.RSB)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LSB:
                self.state = 386
                self.array_index()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def list_array_block(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_blockContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array" ):
                return visitor.visitList_array(self)
            else:
                return visitor.visitChildren(self)




    def list_array(self):

        localctx = MiniGoParser.List_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_list_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(MiniGoParser.LB)
            self.state = 390
            self.list_array_block()
            self.state = 391
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_block(self):
            return self.getTypedRuleContext(MiniGoParser.Array_blockContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_array_block(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_block" ):
                return visitor.visitList_array_block(self)
            else:
                return visitor.visitChildren(self)




    def list_array_block(self):

        localctx = MiniGoParser.List_array_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_list_array_block)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.array_block()
                self.state = 394
                self.match(MiniGoParser.CM)
                self.state = 395
                self.list_array_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.array_block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def list_array(self):
            return self.getTypedRuleContext(MiniGoParser.List_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_block" ):
                return visitor.visitArray_block(self)
            else:
                return visitor.visitChildren(self)




    def array_block(self):

        localctx = MiniGoParser.Array_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_block)
        try:
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.array_element()
                pass
            elif token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.list_array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def function_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Function_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_element)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 407
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 408
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 409
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 410
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 411
                self.struct_literal()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 412
                self.function_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def list_struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.ID)
            self.state = 416
            self.match(MiniGoParser.LB)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 417
                self.list_struct_element()


            self.state = 420
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_element" ):
                return visitor.visitList_struct_element(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_element(self):

        localctx = MiniGoParser.List_struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_list_struct_element)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.struct_element()
                self.state = 423
                self.match(MiniGoParser.CM)
                self.state = 424
                self.list_struct_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.struct_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def CL(self):
            return self.getToken(MiniGoParser.CL, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_element" ):
                return visitor.visitStruct_element(self)
            else:
                return visitor.visitChildren(self)




    def struct_element(self):

        localctx = MiniGoParser.Struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_struct_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.ID)
            self.state = 430
            self.match(MiniGoParser.CL)
            self.state = 431
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_literal" ):
                return visitor.visitFunction_literal(self)
            else:
                return visitor.visitChildren(self)




    def function_literal(self):

        localctx = MiniGoParser.Function_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_function_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(MiniGoParser.ID)
            self.state = 434
            self.match(MiniGoParser.LP)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 435
                self.list_expression()


            self.state = 438
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_statement)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 444
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 445
                self.break_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 446
                self.continue_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 447
                self.return_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 448
                self.call_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs_assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_assign_statementContext,0)


        def assign_sign(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_signContext,0)


        def rhs_assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Rhs_assign_statementContext,0)


        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.lhs_assign_statement(0)
            self.state = 452
            self.assign_sign()
            self.state = 453
            self.rhs_assign_statement()
            self.state = 454
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs_assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_assign_statementContext,0)


        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_assign_statement" ):
                return visitor.visitLhs_assign_statement(self)
            else:
                return visitor.visitChildren(self)



    def lhs_assign_statement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Lhs_assign_statementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_lhs_assign_statement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 469
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 467
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Lhs_assign_statementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_assign_statement)
                        self.state = 459
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 460
                        self.match(MiniGoParser.LSB)
                        self.state = 461
                        self.expression(0)
                        self.state = 462
                        self.match(MiniGoParser.RSB)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Lhs_assign_statementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_assign_statement)
                        self.state = 464
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 465
                        self.match(MiniGoParser.DOT)
                        self.state = 466
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 471
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assign_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ASSIGNADD(self):
            return self.getToken(MiniGoParser.ASSIGNADD, 0)

        def ASSIGNSUB(self):
            return self.getToken(MiniGoParser.ASSIGNSUB, 0)

        def ASSIGNMUL(self):
            return self.getToken(MiniGoParser.ASSIGNMUL, 0)

        def ASSIGNDIV(self):
            return self.getToken(MiniGoParser.ASSIGNDIV, 0)

        def ASSIGNMOD(self):
            return self.getToken(MiniGoParser.ASSIGNMOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_sign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_sign" ):
                return visitor.visitAssign_sign(self)
            else:
                return visitor.visitChildren(self)




    def assign_sign(self):

        localctx = MiniGoParser.Assign_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assign_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGNADD) | (1 << MiniGoParser.ASSIGNSUB) | (1 << MiniGoParser.ASSIGNMUL) | (1 << MiniGoParser.ASSIGNDIV) | (1 << MiniGoParser.ASSIGNMOD) | (1 << MiniGoParser.ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rhs_assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rhs_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs_assign_statement" ):
                return visitor.visitRhs_assign_statement(self)
            else:
                return visitor.visitChildren(self)




    def rhs_assign_statement(self):

        localctx = MiniGoParser.Rhs_assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_rhs_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def multiple_else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Multiple_else_ifContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(MiniGoParser.IF)
            self.state = 477
            self.match(MiniGoParser.LP)
            self.state = 478
            self.condition()
            self.state = 479
            self.match(MiniGoParser.RP)
            self.state = 480
            self.match(MiniGoParser.LB)

            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 481
                self.match(MiniGoParser.NEWLINE)
                self.state = 486
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            self.state = 488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 487
                self.list_block_statement()


            self.state = 490
            self.match(MiniGoParser.RB)

            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 491
                self.multiple_else_if()


            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 494
                self.else_statement()


            self.state = 497
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statementContext,0)


        def multiple_else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Multiple_else_ifContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_multiple_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_else_if" ):
                return visitor.visitMultiple_else_if(self)
            else:
                return visitor.visitChildren(self)




    def multiple_else_if(self):

        localctx = MiniGoParser.Multiple_else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_multiple_else_if)
        try:
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.else_if_statement()
                self.state = 500
                self.multiple_else_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.else_if_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_statement" ):
                return visitor.visitElse_if_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_if_statement(self):

        localctx = MiniGoParser.Else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_else_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(MiniGoParser.ELSE)
            self.state = 506
            self.match(MiniGoParser.IF)
            self.state = 507
            self.match(MiniGoParser.LP)
            self.state = 508
            self.condition()
            self.state = 509
            self.match(MiniGoParser.RP)
            self.state = 510
            self.match(MiniGoParser.LB)

            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 511
                self.match(MiniGoParser.NEWLINE)
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 517
                self.list_block_statement()


            self.state = 520
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(MiniGoParser.ELSE)
            self.state = 523
            self.match(MiniGoParser.LB)

            self.state = 527
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 524
                self.match(MiniGoParser.NEWLINE)
                self.state = 529
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            self.state = 531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 530
                self.list_block_statement()


            self.state = 533
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_scalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_sign(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_signContext,0)


        def rhs_assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Rhs_assign_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_scalar" ):
                return visitor.visitAssign_scalar(self)
            else:
                return visitor.visitChildren(self)




    def assign_scalar(self):

        localctx = MiniGoParser.Assign_scalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_assign_scalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(MiniGoParser.ID)
            self.state = 536
            self.assign_sign()
            self.state = 537
            self.rhs_assign_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_scalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(MiniGoParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_scalar" ):
                return visitor.visitVar_scalar(self)
            else:
                return visitor.visitChildren(self)




    def var_scalar(self):

        localctx = MiniGoParser.Var_scalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_var_scalar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(MiniGoParser.VAR)
            self.state = 540
            self.match(MiniGoParser.ID)
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 541
                self.data_type()


            self.state = 544
            self.match(MiniGoParser.ASSIGNINIT)
            self.state = 545
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def for1(self):
            return self.getTypedRuleContext(MiniGoParser.For1Context,0)


        def for2(self):
            return self.getTypedRuleContext(MiniGoParser.For2Context,0)


        def for3(self):
            return self.getTypedRuleContext(MiniGoParser.For3Context,0)


        def for4(self):
            return self.getTypedRuleContext(MiniGoParser.For4Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 547
                self.for1()
                pass

            elif la_ == 2:
                self.state = 548
                self.for2()
                pass

            elif la_ == 3:
                self.state = 549
                self.for3()
                pass

            elif la_ == 4:
                self.state = 550
                self.for4()
                pass


            self.state = 553
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor1" ):
                return visitor.visitFor1(self)
            else:
                return visitor.visitChildren(self)




    def for1(self):

        localctx = MiniGoParser.For1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_for1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(MiniGoParser.FOR)
            self.state = 556
            self.condition()
            self.state = 557
            self.match(MiniGoParser.LB)
            self.state = 561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 558
                self.match(MiniGoParser.NEWLINE)
                self.state = 563
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 564
                self.list_block_statement()


            self.state = 567
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def var_scalar(self):
            return self.getTypedRuleContext(MiniGoParser.Var_scalarContext,0)


        def end_statement1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.End_statement1Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.End_statement1Context,i)


        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def assign_scalar(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_scalarContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor2" ):
                return visitor.visitFor2(self)
            else:
                return visitor.visitChildren(self)




    def for2(self):

        localctx = MiniGoParser.For2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_for2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.FOR)
            self.state = 570
            self.var_scalar()
            self.state = 571
            self.end_statement1()
            self.state = 572
            self.condition()
            self.state = 573
            self.end_statement1()
            self.state = 574
            self.assign_scalar()
            self.state = 575
            self.match(MiniGoParser.LB)
            self.state = 579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 576
                self.match(MiniGoParser.NEWLINE)
                self.state = 581
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 582
                self.list_block_statement()


            self.state = 585
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def assign_scalar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assign_scalarContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assign_scalarContext,i)


        def end_statement1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.End_statement1Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.End_statement1Context,i)


        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor3" ):
                return visitor.visitFor3(self)
            else:
                return visitor.visitChildren(self)




    def for3(self):

        localctx = MiniGoParser.For3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_for3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.match(MiniGoParser.FOR)
            self.state = 588
            self.assign_scalar()
            self.state = 589
            self.end_statement1()
            self.state = 590
            self.condition()
            self.state = 591
            self.end_statement1()
            self.state = 592
            self.assign_scalar()
            self.state = 593
            self.match(MiniGoParser.LB)
            self.state = 597
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 594
                self.match(MiniGoParser.NEWLINE)
                self.state = 599
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 600
                self.list_block_statement()


            self.state = 603
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor4" ):
                return visitor.visitFor4(self)
            else:
                return visitor.visitChildren(self)




    def for4(self):

        localctx = MiniGoParser.For4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_for4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(MiniGoParser.FOR)
            self.state = 606
            self.match(MiniGoParser.ID)
            self.state = 607
            self.match(MiniGoParser.CM)
            self.state = 608
            self.match(MiniGoParser.ID)
            self.state = 609
            self.match(MiniGoParser.ASSIGN)
            self.state = 610
            self.match(MiniGoParser.RANGE)
            self.state = 611
            self.expression(0)
            self.state = 612
            self.match(MiniGoParser.LB)
            self.state = 616
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 613
                self.match(MiniGoParser.NEWLINE)
                self.state = 618
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 620
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 619
                self.list_block_statement()


            self.state = 622
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(MiniGoParser.BREAK)
            self.state = 625
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.match(MiniGoParser.CONTINUE)
            self.state = 628
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self.match(MiniGoParser.RETURN)
            self.state = 632
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 631
                self.expression(0)


            self.state = 634
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_component(self):
            return self.getTypedRuleContext(MiniGoParser.Call_componentContext,0)


        def end_statement1(self):
            return self.getTypedRuleContext(MiniGoParser.End_statement1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
            self.call_component(0)
            self.state = 637
            self.end_statement1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_componentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def call_component(self):
            return self.getTypedRuleContext(MiniGoParser.Call_componentContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_component

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_component" ):
                return visitor.visitCall_component(self)
            else:
                return visitor.visitChildren(self)



    def call_component(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Call_componentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_call_component, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.state = 640
                self.match(MiniGoParser.ID)
                self.state = 641
                self.match(MiniGoParser.LP)
                self.state = 643
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 642
                    self.list_expression()


                self.state = 645
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.state = 646
                self.match(MiniGoParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 667
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 665
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Call_componentContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_call_component)
                        self.state = 649
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 650
                        self.match(MiniGoParser.DOT)
                        self.state = 651
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Call_componentContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_call_component)
                        self.state = 652
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 653
                        self.match(MiniGoParser.DOT)
                        self.state = 654
                        self.match(MiniGoParser.ID)
                        self.state = 655
                        self.match(MiniGoParser.LP)
                        self.state = 657
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 656
                            self.list_expression()


                        self.state = 659
                        self.match(MiniGoParser.RP)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Call_componentContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_call_component)
                        self.state = 660
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 661
                        self.match(MiniGoParser.LSB)
                        self.state = 662
                        self.expression(0)
                        self.state = 663
                        self.match(MiniGoParser.RSB)
                        pass

             
                self.state = 669
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_list_expression)
        try:
            self.state = 675
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 670
                self.expression(0)
                self.state = 671
                self.match(MiniGoParser.CM)
                self.state = 672
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 674
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 685
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 680
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 681
                    self.match(MiniGoParser.OR)
                    self.state = 682
                    self.expression1(0) 
                self.state = 687
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 696
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 691
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 692
                    self.match(MiniGoParser.AND)
                    self.state = 693
                    self.expression2(0) 
                self.state = 698
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def INEQ(self):
            return self.getToken(MiniGoParser.INEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GTE(self):
            return self.getToken(MiniGoParser.GTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 700
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 707
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 702
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 703
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.INEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 704
                    self.expression3(0) 
                self.state = 709
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 711
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 718
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 713
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 714
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 715
                    self.expression4(0) 
                self.state = 720
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 729
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,71,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 724
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 725
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 726
                    self.expression5() 
                self.state = 731
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 735
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 732
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 733
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 734
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 738
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 758
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 756
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 740
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 741
                        self.match(MiniGoParser.DOT)
                        self.state = 742
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 743
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 744
                        self.match(MiniGoParser.DOT)
                        self.state = 745
                        self.match(MiniGoParser.ID)
                        self.state = 746
                        self.match(MiniGoParser.LP)
                        self.state = 748
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 747
                            self.list_expression()


                        self.state = 750
                        self.match(MiniGoParser.RP)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 751
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 752
                        self.match(MiniGoParser.LSB)
                        self.state = 753
                        self.expression(0)
                        self.state = 754
                        self.match(MiniGoParser.RSB)
                        pass

             
                self.state = 760
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_expression7)
        try:
            self.state = 767
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 761
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 762
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 763
                self.match(MiniGoParser.LP)
                self.state = 764
                self.expression(0)
                self.state = 765
                self.match(MiniGoParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[40] = self.lhs_assign_statement_sempred
        self._predicates[58] = self.call_component_sempred
        self._predicates[60] = self.expression_sempred
        self._predicates[61] = self.expression1_sempred
        self._predicates[62] = self.expression2_sempred
        self._predicates[63] = self.expression3_sempred
        self._predicates[64] = self.expression4_sempred
        self._predicates[66] = self.expression6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def lhs_assign_statement_sempred(self, localctx:Lhs_assign_statementContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def call_component_sempred(self, localctx:Call_componentContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




