#coding=utf-8

'''
C.__name__     类名
C.__doc__      文档字符串
C.__bases__    所有父类组成的元组
C.__subclasses__()    返回子类
C.__dict__     所有属性
C.__module__   模块
C.__class__    对应的类
C.__metaclass__    类的元类, 用来改变类的某些默认行为, 默认为types.ClassType
                                                  元类在类的申明时期（即代码被编译时）就初始化完毕（远早于实例产生）
'''

class MyClass(object):
    'My classdocs'
    
    name = 'oo'     #The class field, the static field

    def __init__(self):
        self.data = 0
    
    #destructor
    def __del__(self):
        pass
        
    #bool(obj) call this, default is True
    def __nonzero__(self):
        return False
    
    def __hash__(self):
        return id(self)
    
#------------------override operators
    #override obj(), obj(param)
    def __call__(self, num = None):
        return '__call__ ' + str(num) 
    
    #not work?
    def __getattr__(self, name):
        print '__getattr__ %s' % (name)
        return self.data
    
    #override all the assignment with .
    def __setattr__(self, name, value):
#        print '__setattr__ %s is %s' % (name,value)
        #must use __dict__ to assign value, or come an infinte loop
        self.__dict__['data'] = value
    
    #override compare with < <= = >= >
    def __cmp__(self, other):
        if isinstance(other, MyClass):
            return self.data - other.data
        else:
            raise Exception('can not compare to not MyClass object')
    
    #override ==, priority high than __cmp__
    def __eq__(self, other):
        return '__eq__'
    
#------------------override operators
    
#------------------override iterator
    '''
    exist __iter__(), call next()
        no __iter__(), exist __getitem__(), call __getitem__()
            no neither __iter__() and __getitem__(), obj is not iterable
    __iter__() should return a wappered obj, contains now_index, end_index, and a value list, 
        or will be only one iterator can work
    '''
    def __iter__(self):
        return self
    
    def next(self):
        if isinstance(self.data, int):
            self.data += 1
            return self.data 
#------------------override iterator

#------------------override presentation
    #friendly to user, prioity higher than __repr__
    def __str__(self):
        return '__str__ ' + str(self.data)
    
    #friendly to computer, as-code string
    #no __str__, __repr__ is called
    def __repr__(self):
        return '__repr__ ' + `self.data`
#------------------override presentation
    
    @staticmethod
    def staticMethod():     #静态函数，没有任何参数
        print 'staticMethod'
        
    @classmethod
    def classMethod(cls):   #类函数，带类作为第一个参数
        print 'classMethod', cls.__name__
    
    def showSelfParam(self):
        print 'Function showSelfParam : '
        print '__class__', self.__class__.__name__
        print '__dict__', self.__dict__
        
    def showClassParam(self):
        print 'Function showClassParam : '
        print 'Class.__dict__', MyClass.__dict__
        print 'Class.__doc__', MyClass.__doc__
        print 'Class.__module__', MyClass.__module__
        print 'Class.__weakref__', MyClass.__weakref__
    
    
m = MyClass()
n = MyClass()
#print (m.__class__.__dict__)
#m.data = 5
#print m
#print `m`
#m.data = 1;
#for i in m:
#    if i > 10 : break
#    for j in m:
#        if j > 10 : break
#        print i, j

#MyClass.staticMethod()
#MyClass.classMethod()
#        
#m.showSelfParam()
#m.showClassParam()
