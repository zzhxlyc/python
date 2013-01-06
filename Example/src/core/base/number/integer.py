#coding=utf-8
n1 = 33
n2 = -33

print n1.bit_length()   #6
print n2.bit_length()   #6, 只算绝对值的位数

print bin(n1)   #0b100001
print bin(n2)   #-0b100001, 符号+数值

print hex(n1)   #0x21
print hex(n2)   #-0x21

print oct(n1)   #041
print oct(n2)   #-041