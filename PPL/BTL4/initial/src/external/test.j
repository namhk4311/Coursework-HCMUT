;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Tue May 06 21:35:26 ICT 2025

.source test.java
.class public test
.super java/lang/Object

.field  a [[I

.method public <init>()V
.limit stack 3
.limit locals 1
.var 0 is this Ltest; from Label0 to Label1

Label0:
.line 1
	aload_0
	invokespecial java/lang/Object/<init>()V
.line 2
	aload_0
	iconst_3
	iconst_4
	multianewarray [[I 2
	putfield test.a [[I
Label1:
	return

.end method

.method  main([Ljava/lang/String;)I
.limit stack 3
.limit locals 2
.var 0 is this Ltest; from Label0 to Label1
.var 1 is arg0 [Ljava/lang/String; from Label0 to Label1

Label0:
.line 3
	aload_0
	getfield test.a [[I
	iconst_1
	aaload
	iconst_0
	iaload
	aload_0
	getfield test.a [[I
	iconst_2
	aaload
	iconst_1
	iaload
	iadd
Label1:
	ireturn

.end method
