# name = input("请输入姓名：")
# age = input("请输入年龄：")
# sex = input("请输入性别：")
#
# print('''******************
# 姓名: {0}
# 性别：{1}
# 年龄：{2}
# ******************
# '''.format(name, sex, age))

str1 = 'python hello aaa 123123aabb'

print(str1[:4:])  #1）请取出并打印字符串中的'python'。

print("o a" in str1, "he" in str1, "ab" in str1)  #2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？

print(str1.replace("python", "lemon"))  #3）替换python为 “lemon”.

print(int(str1.find('aaa')) + 1)  #4) 找到aaa的起始位置--aaa在这串字符的第14位出现（因为字符头从0开始计数所以我加了1）
