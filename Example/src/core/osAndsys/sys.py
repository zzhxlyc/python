import sys
import getopt

print sys.path  #list, can use append to add path
print sys.exec_prefix, sys.executable, sys.prefix, sys.version
print sys.maxint, sys.platform

#argv[0] is filename, argv[i] is for ith param
for param in sys.argv:
    print param

# : and = is for value input
args = ['-n','10','-ax','--debugLevel','10','filename']
opts, others = getopt.getopt(args, 'n:ax', ['debugLevel='])
print opts, others