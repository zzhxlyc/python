#coding=utf-8
class MetaClass(type):
    
    def __init__(self, name, bases, attrd):
        super(MetaClass, self).__init__(name, bases, attrd)
        print 'MetaClass __init__'
        if '__str__' not in attrd:
            print name, 'has no __str__ method, suggest one'
    
    def __new__(cls, name, bases, attrd):
        mcls = super(MetaClass, cls).__new__(cls, name, bases, attrd)
        print 'MetaClass __new__'
        return mcls
    
    @classmethod
    def register(cls):
        print 'MetaClass register', cls

class ObjClass:
    __metaclass__ = MetaClass       #只要碰到这句话，MetaClass就会被初始化并被赋值
    
    def __init__(self):
        print 'ObjClass __init__'
        

obj = ObjClass()
ObjClass.register()
