"""
str的常用方法：字符串“ab_cdef123”，从b开始查找，并截取输出"b_cdef1"（限定用find关键字）
"""
# 定义原始字符串str1
str1 = "ab_cdef123"
# 定义需要截取的字符串str2
str2 = "b_cdef1"
# 使用find确定str中有需要的str2
x1 = str1.find(str2, 1)
# 计算长度，从x1第一个截图位子，到最后一个截图位，总长度
x2 = x1+len(str2)
# 使用切片方式，切取我们所需要的str2
x3 = str1[x1:x2]
# 最后输出，我们的结果
print("使用find关键字输出'b_cdef1'==>", x3)
