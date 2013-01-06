# -*- coding: utf8 -*-
import quopri

'''
quoted-printable is good for string do not have much none ASC char, 3 char(=**) for one these char
'''

str = '– Fly ぁ 梦 –'

print quopri.encodestring(str)

print quopri.decodestring(quopri.encodestring(str))
