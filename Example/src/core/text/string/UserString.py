from UserString import UserString, MutableString

'''
UserString是str的类包装
MutableString只是继承自UserString，添加了修改的API（重新构造String实现），本质不是StringBuilder性质的
'''

UserString, MutableString