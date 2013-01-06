import struct

'''
Data output/input stream utils

str = pack(str_fmt, v1, v2...)
data_tuple = unpack(str_fmt, str)
length = calcsize(str_fmt)    #byte length

cls = Struct(str_format)
cls.pack(v1, v2)
cls.unpack(str)
cls.format
cls.size
'''

data_str = struct.pack('iil', 1, 2, 1000)
data_tuple = struct.unpack('iil', data_str)
length = struct.calcsize('iil')

'''
Format    C Type            Python Type
c     char                  string of length
b     signed char           integer
B     unsigned char         integer
?     _Bool                 bool 
h     short                 integer
H     unsigned short        integer
i     int                   integer
I     unsigned int          integer 
l     long                  integer 
L     unsigned long         integer 
q     long long             integer 
Q     unsigned long long    integer 
f     float                 float
d     double                float 
s     char[]                string     
p     char[]                string     
P     void *                integer 
'''