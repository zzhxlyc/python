import pickle

'''
序列化list dict之类的数据，类似php的serialize
'''

conf = {
    'name' : 'stariy',
    'age' : 22,
    'web' : 'stariy.org'
}

def saveConf(conf):
    confObj = pickle.Pickler(file('my.conf', 'w'))
    confObj.dump(conf)
    
def loadConf():
    confObj = pickle.Unpickler(file('my.conf', 'r'));
    return confObj.load()

def testLoad():
    conf = loadConf()
    print conf
    print conf.get('name'), conf.get('age')

#saveConf(conf)
testLoad()
    