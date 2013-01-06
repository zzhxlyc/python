str = 'My first python'

#first(include) : end(exclude) : step
print 1, str[3]

print 2, str[3:len(str)]

print 3, str[3:]

print 4, str[:8]

print 5, str[-12:-7]

print 6, str[-12:]

print 7, str[:-7]

#step, first:final:step, if step < 0, from the tail
print 8, str[::-1]

print 9, str[3:8:2]

print 10, str[:None]    #The same as str[:], just like you delete the None
