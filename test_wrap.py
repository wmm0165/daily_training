# -*- coding: utf-8 -*-
# @Time : 2019/10/12 16:52
# @Author : wangmengmeng
def dec(f):
    n = 3
    def wrapper(*args,**kw):
        return f(*args,**kw) * n
    return wrapper

@dec
def foo(n):
    return n * 2

foo(2)
