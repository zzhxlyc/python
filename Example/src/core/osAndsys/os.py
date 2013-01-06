import os

def variable():
    print os.name   #'nt', 'mac'
    print os.environ['path']    #dict, os environment variable
    print os.linesep, os.sep, os.pathsep    #in windows, they are '\r\n'  '\'  ';'
    print os.curdir, os.pardir              #.   ..
    
def actInOS():
#    os.chdir('/home/work')
    print os.getcwd()
    print os.getpid()
    
def doFileAndDirectory():
    print os.access('E:\Downloads', os.F_OK)    #test if exist
    print os.access('E:\Downloads', os.R_OK)    #test if can read
    print os.access('E:\Downloads', os.W_OK)    #test if can write
    print os.access('E:\Downloads', os.X_OK)    #test if can execute
    
    #os.chmod('file.txt', 777)    #only in unix

def walk():
    for path, folderlist, filelist in os.walk('D:\ACM'):
        print path, folderlist, filelist
    
def systemCall():
    cmd = 'dir'
    ret = os.system(cmd)
    if ret != 0:
        print 'error'
    
    #systemCallIntoFile
    cmd = 'dir'
    f = os.popen(cmd)
    for eachLine in f:
        print eachLine,
    
        
#-------------------os.path------------------------

def doFile():
    #now file abs path(include filename)
    print __file__                  #E:\Workplace\Python\Example\src\core\osAndsys\os.py
    
    f = '.'
    f = os.path.abspath(f)          #f = E:\Workplace\Python\Example\src\core\osAndsys
    f = os.path.join(f, 'os.py')    #f = E:\Workplace\Python\Example\src\core\osAndsys\os.py
    print os.path.basename(f)       #os.py
    print os.path.dirname(f)        #E:\Workplace\Python\Example\src\core\osAndsys
    
    name, ext = os.path.splitext('a.tar.gz')
    print name, ext     #name = a.tar, ext = .gz
    
    print os.path.getsize('E:\Downloads\Inception.rmvb'), 'bytes'   #1024 is the base
    f = 'E:\Downloads'
    #getctime : create    getatime : last visit    getmtime : last modify
    print os.path.getctime(f), os.path.getatime(f), os.path.getmtime(f)


#variable()   
#actInOS()
#walk()
doFile()
#systemCall()
#systemCallIntoFile()
