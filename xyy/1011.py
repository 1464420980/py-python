#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 21
b = 10
c = 0

c = a + b
print ("1 - c 的值为：", c)

c = a - b
print ("2 - c 的值为：", c)

c = a * b
print ("3 - c 的值为：", c)

c = a / b
print ("4 - c 的值为：", c)

c = a % b
print ("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print ("6 - c 的值为：", c)

a = 10
b = 5
c = a//b
print ("7 - c 的值为：", c)

print('=======================我是一条分割线====================================')


"""
将4个str类型的字符串(有重复)放入list后输出、再转成tuple输出、最后去重输出

输出结果示例：

['name', 'old', 'name', 'sex']
('name', 'old', 'name', 'sex')
{'name', 'sex', 'old'}

"""


# 创建list集合
list = ['name', 'old', 'sex', 'old']

# 将list转换成tuple元组
tuple = tuple(list)

# 将list内数据，进行去重操作
set = set(list)

# 依次输出结果
print('集合', list)
print('元组', tuple)
print('去重', set)