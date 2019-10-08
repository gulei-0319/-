#1用python.输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E

score = int(input("请输入一个分数："))
if 100 >= score >= 90:
        print("A")
elif 90 > score >= 80:
        print("B")
elif 80 > score >= 70:
        print("C")
elif 70 > score >= 60:
        print("D")
elif 60 > score >= 0:
        print("E")
else:
    print("输入错误！")

#2定义一个列表，从键盘输入一个随机数，判断该数是否在列表中

a=[1,2,3,4,5,6,7,8,9]
b=int(input('输入一个值：'))
if b in a:
    print('true')
else:
    print('fasle')


#3求10阶乘

a = 1
i = 1
while i <= 10:
    a = a * i
    i += 1
print('10的阶乘为：',a)

#4求100以内能被3整除的数，并将作为列表输出

n = 1
for i in range(1,100):
    if i % 3 == 0:
        print(i)
    else:
        n += 1

