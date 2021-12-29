"""
break：可以提前退出循环；continue：跳过当前的循环，直接开始下一次循环。

用break和continue各自写一个示例，内容不限
"""

# break:可以提前退出循环
# 示例
N = 1

while N <= 100:
    if N > 10:
        break
    print(N, end="  ")
    N = N + 1
print('跳出了本次循环：', "END")


# continue：跳过当前的循环，直接开始下一次循环
# 示例
n = 0

while n < 10:
    n = n + 1
    if n % 2 != 0:
        continue
    print(f'当{n}被2整除时输出n的值：', n)




