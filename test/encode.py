#!/usr/bin/python
#coding=utf-8

s = raw_input("input something:")

print s
print type(s)
print repr(s)

s = raw_input("请输入中文字符：".decode('utf-8'))

print s
print type(s)
print repr(s)

s = raw_input(u"请输入中文字符：".encode("gbk"))

print s
print type(s)
print repr(s)
