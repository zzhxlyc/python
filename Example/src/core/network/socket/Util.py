import socket

print socket.gethostname()  #Stariy-PC

print socket.gethostbyname('blog.stariy.org')   #173.192.220.101

#return (host, cnameList, ipList)
print socket.gethostbyname_ex('google.com')   #('google.com', [], ['66.249.89.104', '66.249.89.99'])

#return as same with gethostbyname_ex(), but the input is ip
print socket.gethostbyaddr('173.192.220.101')   