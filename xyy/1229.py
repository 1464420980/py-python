# 定义四个str
str1 = 'abcdabcd1'
str2 = 'abcdabcd2'
str3 = 'abcdabcd3'
str4 = 'abcdabcd4'

# 输出

print('str1类型：', str1)
print('str2类型：', str2)
print('str3类型：', str3)
print('str4类型：', str4)

print('===============================我是一条分割线======================================')

# 将str类型转换成list
list1 = list(str1)
list2 = list(str2)
list3 = list(str3)
list4 = list(str4)

# 输出

print('list1类型：', list1)
print('list2类型：', list2)
print('list3类型：', list3)
print('list4类型：', list4)

print('===============================我是一条分割线======================================')

# 将list转换成tuple类型

tuple1 = tuple(list1)
tuple2 = tuple(list2)
tuple3 = tuple(list3)
tuple4 = tuple(list4)

# 输出

print("tuple1类型：", tuple1)
print("tuple2类型：", tuple2)
print("tuple3类型：", tuple3)
print("tuple4类型：", tuple4)

print('===============================我是一条分割线======================================')

# 给tuple去重
# 利用set的去重属性,先将tuple放入set中
set1 = set(tuple1)
set2 = set(tuple2)
set3 = set(tuple3)
set4 = set(tuple4)

print('set1类型', set1)
print('set2类型', set2)
print('set3类型', set3)
print('set4类型', set4)

print('===============================我是一条分割线======================================')

# 再将set类型转化为tuple类型

tuplestr1 = tuple(set1)
tuplestr2 = tuple(set2)
tuplestr3 = tuple(set3)
tuplestr4 = tuple(set4)

print(tuplestr1)
print(tuplestr2)
print(tuplestr3)
print(tuplestr4)
