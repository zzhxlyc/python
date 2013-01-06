#coding=utf-8

#赋值语句没有返回值，所以不属于表达式

#允许多重赋值
a = b = c = 2

x ,y ,z = 1, 2, 3 
#==>
(x, y, z) = (1, 2, 3)

#三元表达式
x = True if a < b else False

#除法
a / b   #普通除法
a // b  #任何情况下都是地板除，包括浮点数，6 / 2.5 = 2.0

#swap
x, y = y, x

# 3 < 4 and 4 < 5
print 3 < 4 < 5

#no support for a++ a--

#no support for switch case

#字符串表示, 一般为适合计算机表示的字符串，可通过eval()求值重新得到该对象
`a`, repr(a)

#适合print的可阅读字符串
str(a)

#值比较
print a == b
#id 比较  => id(a) == id(b)
print a is b

#Python使用引用计数, 此举引用计数减1
del a

#函数默认值
def function(default = None):
    pass