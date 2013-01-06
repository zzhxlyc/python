#coding=utf-8
import math, fractions

divmod(10, 3) #(3, 1)

pow(2, 3),    #2 ** 3 = 8
pow(2, 3, 3)  #2 ** 3 % 3 = 2

#round(num, point)
round(3.555),     #4.0
round(3.555, 1)   #3.6

print math.pi, math.e

math.sqrt(4.0)

math.ceil(3.5)      #4.0
math.floor(3.55),   #3.0
math.floor(-3.55),  #-4.0
int(-3.55)          #-3

#精确浮点计算，不会丢失精度；math.fsum[iterator]
math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])     #1.0

fractions.gcd(4, 6)
