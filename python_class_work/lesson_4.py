'''
string = "asdfghjkl"
list_1 = list(string)
print(list_1)
'''

'''
sum = 0
for i in range(101):
    sum+=i
    if i ==100:
        print(sum)
'''
def judge_5(*args):
    if len(*args) > 5:
        return True
    else:
        return False
content = input('please enter something here:')
print(judge_5(content))

