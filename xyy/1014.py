"""
将str类型转为list输出，再转回str输出，输出示例：

['9', '6']
9.6
"""

# 定义一个str为9.6
str = '9.6'

# 使用split将'.'去除
str = str.split('.')

# 将str类型转换成list
str = list(str)

# 输出转换后的结果
print('list类型：', str)

# 再将list类型转换回str
list = '.'.join(str)

# 输出转换后的结果
print('str类型：', list)