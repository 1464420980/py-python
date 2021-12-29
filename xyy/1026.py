"""
str的常用方法：字符串"12345678"，输出1357、2468、1、8、87654321
"""

# 定义字符串
str = "12345678"

# 利用for循环输出str中的单数
for i in range(1, 9):

    if i % 2 != 0:
        print('输出单数：', i, end='  ')
    continue
print('    ')

# 利用for循环输出str中的复数
for i in range(1, 9):

    if i % 2 == 0:
        print('输出双数：', i, end='  ')
    continue
print('    ')

# 截取str中第一个字符
print('输出字符串第一个字符：', str[0:1], end='  ')
print('    ')

# 截取str中的最后一个字符
print('输出字符串第一个字符：', str[7:8])

# 反转str
print('输出反转后的字符串：', str[::-1])


