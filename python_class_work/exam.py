# user = {}
# name = input("请输入姓名：")
# gender = input("请输入性别：")
# age = input("请输入年龄：")
# user = dict(name=name, gender=gender, age=age)
# print("我的名字叫{}, 今年{}岁, 性别{}, 喜欢敲代码".format(name, age, gender))
#
# user['height'] = input('请输入身高：')
# user['phone'] = input('请输入联系方式：')
# print('用户信息如下:', user)
#
# user.pop('phone')
num = []
sum_i = 0
for i in range(0,101,2):
    num.append(i)
    sum_i+=i
    if i ==100:
        print(num, sum_i)

