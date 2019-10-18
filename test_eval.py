# -*- coding: utf-8 -*-
# @Time : 2019/10/18 14:15
# @Author : wangmengmeng
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
aa = eval(a)
print(type(a))
print(type(aa))
b = "{1: 'a', 2: 'b'}"
bb = eval(b)
print(type(b))
print(type(bb))
c = "([1,2], [3,4], [5,6], [7,8], (9,0))"
cc = eval(c)
print(type(c))
print(type(cc))
d = "3+5"
dd = eval(d)
print(dd)