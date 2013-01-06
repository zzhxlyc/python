import types

def getVar(var):
    tp = type(var)
    #type object is unique of global
    if tp is types.IntType:
        pass
    elif tp is types.LongType:
        pass
    elif tp is types.TypeType:
        pass
    elif isinstance(var, int):
        pass

print isinstance('a', str)
print isinstance(['a', 'b'], list)
print isinstance(('a', 'b'), tuple)
print isinstance({'a':1, 'b':2}, dict)