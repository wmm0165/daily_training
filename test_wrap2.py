# -*- coding: utf-8 -*-
# @Time : 2019/10/14 9:45
# @Author : wangmengmeng
def adder(x):
    def wrapper(y):
        return x + y
    return wrapper
adder5 = adder(5)
print(adder5(adder5(6)))
