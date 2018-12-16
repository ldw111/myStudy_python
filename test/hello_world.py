#!/usr/bin/python
#coding=utf-8

print u"hello world!"
print u"你好，世界！"

import sys

print sys.getdefaultencoding()

a="测试"

b=u"测试"

print a
print b
print repr(a)
print b.encode('gbk')

print a.decode('utf-8')
