#coding=utf-8

str = 'My first python'

len(str)

ord('A'),     #65
chr(ord('A')) #A

max(str), min(str)  #返回max或min的char值

str.count('substr')

str.startswith('prefix')
str.endswith('suffix')

str.find('sub')     #不存在返回-1
str.rfind('sub')
str.index('first')    #不存在抛出ValueError
str.rindex('first')

str.replace('old', 'new')

','.join(['a', 'b', 'c'])
str.split(',')
str.splitlines()    #split by \n

str.lstrip()    #left trim
str.rstrip()

str.lower()
str.upper()
str.swapcase()

str.isalnum()
str.isdigit()
str.isalpha()
str.isspace()
str.isupper()
str.islower()

str.translate(None, 'aeiou')    #删除后个字符串中指定的字符

#omission '+' is ok, but only for const string, variable is not allowed
'My' "first" 'python'

#paste
str * 2   #str + str

#multiline string
'''first line
second line
third line'''

#substring
if 'lv' in 'love':
    'even love has lv'
elif 'lov' in 'love':
    'oh, lov is the substring of love'
    
'''
%r        repr()输出
%s        str()输出
%d/%i     有符号十进制
%u        无符号十进制
%o        八进制
%x        十六进制
%f        浮点数
%e        科学技术法

%u/%o/%x   遇到负数，输出负号+绝对值的字符串

%+d        输出符号(+或-)
%2d        填充空格
%02d       填充0
%#o/%#x    输出标识符0或0X
%(var1)s %(var2)d    使用dict填充
'''

#原始字符串操作符r, 阻止\转义
r'\n'

#Unicode操作符u
u'\u1234'


