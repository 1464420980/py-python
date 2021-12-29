"""
while循环：循环依次对list中的每个名字打印出Hello，XXX！

['Bart', 'Lisa', 'Adam']
"""

# 声明一个数组
L = ['Bart', 'Lisa', 'Adam']

# 数组L的长度为N
N = len(L)

# 声明一个变量Q
Q = 0

# 方法一
while N > 0:
    print('Hello,', L[Q])
    N = N-1
    Q = Q+1

# 方法二
# while N > Q:
#     print('Hello,', L[Q])
#     Q = Q+1


