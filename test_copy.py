# -*- coding: utf-8 -*-
# @Time : 2019/10/14 11:17
# @Author : wangmengmeng
import copy
a = [1, 2, 3, 4, ['a', 'b', 'c']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
a.append(5)
a[4].append('hello')
print(a)
print(b)
print(c)
print(d)
