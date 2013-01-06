#coding=utf-8
print '\tclassic style'
class P1:
    def foo(self):
        print 'P1 foo'
class P2:
    def foo(self):
        print 'P2 foo'
    def bar(self):
        print 'P2 bar'
class C1(P1, P2):
    pass
class C2(P1, P2):
    def bar(self):
        print 'C2 bar'
class PC(C1, C2):
    pass

pc = PC()   #深度优先搜索, classic经典形式
pc.foo()    #P1 foo
pc.bar()    #P2 bar

print '\tnew object style'
class Q1(object):
    def foo(self):
        print 'Q1 foo'
class Q2(object):
    def foo(self):
        print 'Q2 foo'
    def bar(self):
        print 'Q2 bar'
class D1(Q1, Q2):
    pass
class D2(Q1, Q2):
    def bar(self):
        print 'D2 bar'
class QD(D1, D2):
    pass

qd = QD()   #宽度优先搜索, 从object继承的形式
qd.foo()    #Q1 foo
qd.bar()    #D2 bar