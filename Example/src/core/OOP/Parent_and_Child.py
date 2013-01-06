
class Parent:
    staticField = 'Parent staticField'
    
    def __init__(self):
        self.data = 'Parent public data'
        self.parentData = 'Parent parentData'
        self._private = 'Parent private'
        print 'Parent __init__'
    
    def __del__(self):
        print 'Parent __del__'
    
    def func(self):
        print 'Parent func'
        
    def parentFunc(self):
        print 'Parent parentFunc'
        
    @staticmethod
    def staticMethod():
        print 'Parent staticMethod'

class Child(Parent):
    staticField = 'Child staticField'
    
    def __init__(self):
        #parent __init__ is not must, the line is also arbitrary
        Parent.__init__(self)
        self.data = 'Child public data'
        self._private = 'Child private'
        print 'Child __init__'
    
    def __del__(self):
        print 'Child __del__'
        #parent __del__ is not must, the line is also arbitrary
        Parent.__del__(self)
    
    def func(self):
        print 'Child func'
        
    @staticmethod
    def staticMethod():
        print 'Child staticMethod'

c = Child()
print isinstance(c, Child)      #True
print isinstance(c, Parent)     #True
print c.data                    #child data
print c.staticField             #child staticField
c.func()                        #child function
c.staticMethod()                #child staticMethod
c.parentFunc()                  #parent function comes from extend
