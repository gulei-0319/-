#coding:utf-8
'''
a=5
b=2.5
c='hello'
print(type(a))
print(type(b))
print(type(c))
'''
#a,b=input('please input a value :').split(',')
#print('The value of a is :',a,b,type(a),type(b))

#s=[11,13,5,7,0,56,23,34,72]

#print (max(s))
#print(min(s))
#print (len(s))
#print s.index(5)
#print s.append(7)
#print del s[4],
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



