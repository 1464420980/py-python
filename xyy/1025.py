"""
str的常用方法：检查"abCDeFG"字符串中是否有大、小写字母，有的话小写转换成大写，大写转换成小写
"""
import re
# 大写转小写lower()
# 小写转大写upper()

#定义str字符串
str = "abCDeFG";

# print(bool(re.match('^[a-zA-Z]+$', str)))
# 用正则表达式来判断str中是否包含大小写字母
if bool(re.match('^[a-zA-Z]+$', str)) == True:
    print("判断str中存在大小写字母:", "abCDeFG字符串中包含大小写字母")
    print("大小写反转：", str.swapcase());

else:
    print("输出结果","abCDeFG字符串中不包含大小写字母")



