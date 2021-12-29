"""
输出下列元素个数、倒数第一个元素、删除php后输出：

['python', 'java', ['asp', 'php'], 'scheme']

"""


# 创建需要操作的数组
list = ['python', 'java', ['asp', 'php'], 'scheme']

# 先取出list中的元素加上嵌套list内的元素个数，最后再减去嵌套list内所占用的元素位置
listStr = len(list+list[2])-1

# 输出
print('原数组：', list)
print('list中元素个数：', listStr)

# 取出数组中最后一个元素
listIndex = list[-1]

# 输出
print('数组中最后一个元素：', listIndex)

# 删除数组中的'php'元素
del list[2][1]

print("删除'php'后的数组：", list)