# -*- coding: utf-8 -*-
# @Time : 2019/10/12 16:59
# @Author : wangmengmeng
import re
str1 = "Python's features"
str2 = re.match( r'(.*)on(.*?) .*', str1, re.M|re.I)
print(str2.group(1))