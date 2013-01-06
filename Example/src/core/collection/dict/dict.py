map = {'DS':90, 'ADS':99, 'OS':86, 'Java':89}

#dict is iterable, iter(map) is called default, each time call it.next(), return a key
for key in map:
    pass
for key, value in map.items():
    pass
 
map.keys(), map.values(), map.items()

#init
newmap = {}.fromkeys(('a', 'b'), 0)    #all value is 0, if no value, default is None

#contain, delete
if 'DS' in map and 'ADS' in map:     #the same as has_key()
    value = map.pop('DS')   #or, del map['DS']
    del map['ADS']

#add element
map['C++'] = 90

#[] for None will get an Error, get() for None return None or default
map['Java'], map.get('Python', 99)

#merge
map.update({'DS':99, 'C++':90})

map.clear()

'''
obj必须支持__hash__() 
'''