"""
tuple嵌套list，修改下列list的值并输出

将('a', 'b','c', ['A', 'B','c'],'d')修改为('a', '1','b','c',['X', 'Y'，'Z'])
"""


# 创建集合['A', 'B', 'C']
liststr = ['A', 'B', 'C']

# 创建元组('a', 'b', 'c', 'd')
tuplestr = ('a', 'b', 'c', 'd')

# 将元组转换成list，便于对数据进行操作
tuplestr1 = list(tuplestr)

# 将list嵌套进tuplestr1中
tuplestr1.insert(3, liststr)

# 再将tuplestr1转换成tuples类型
tuplestrResult = tuple(tuplestr1)

# 输出原始数据
print("原始数据为：", tuplestrResult)


# 开始修改原始数据

# list中插入数据
tuplestr1.insert(1, '1')

# 删除list末尾元素
tuplestr1.pop()

# 根据下标替换list中元素
tuplestr1[4][0] = 'X'
tuplestr1[4][1] = 'Y'
tuplestr1[4][2] = 'Z'

# 将tuplestr1转换成tuple类型
tuplestrResult = tuple(tuplestr1)

# 输出修改后的数据
print("修改后的数据：", tuplestrResult)


