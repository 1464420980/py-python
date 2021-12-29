"""
输出下列dict的87，放入一个新的key和value并输出、判断Bob是否存在

{'Michael' : 95,'Bob ': 87,'Jack' : 66,1:50}
"""

# 声明一个dict
dict = {'Michael': 95, 'Bob': 87, 'Jack': 66, 1: 50}

# 输出'Bob'的值
print('Bob的值为：', dict['Bob'])

# 新添加一个key和value
dict['xu'] = '123456'

# 输出添加后的dict
print('添加key和value后：', dict)

# print(dict.keys())
# 判断'Bob'是否存在
print("'Bob'是否存在：", 'Bob' in dict.keys())