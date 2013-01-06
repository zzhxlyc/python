import sys

username = raw_input('please input your username : ');
password = raw_input('please input your password : ');

print username, password

# C printf
print 'username is %s, password is %s' % (username, password)

#redirect
print >> sys.stdout, 'Out'
print >> sys.stderr, 'Error'

#redirect to file
logfile = open('StandardIO.log', 'a')
print >> logfile, 'new record'
logfile.close()