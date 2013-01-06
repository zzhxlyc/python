from ConfigParser import ConfigParser

def read():
    config = ConfigParser()
    config.read('config.conf')
    #config.readfp(file('config.conf', 'r'))
    print config.get('setting', 'a')

def read1():
    config = ConfigParser()
    config.read('set.conf')
    print config.get(None, 'a')

def write():
    config = ConfigParser()
    config.read('config.conf')
    config.add_section('sub')
    config.set('sub', 'a', 2)
    config.write(file('config.conf', 'w'))
    
read()