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
'''
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
'''
'''
a=5
b=2.5
c="hello"

print (type(a))

print (type(b))

print (type(c))
'''
'''
a,b=input('please input a value:').split(',')

print('the value of a is :',a,b,type(a),type(b))

print('xxx={}'.format(a))
'''
'''
s=[1,2,3,4,5,6,7,8,9]
print(s[-3])
#print(s[2],s[4],s[6],s[8])

print(s[2:7:3])
'''
'''
print(list(range(9)))
print(list(range(1,9)))
print(list(range(1,9,4)))
'''
'''
s=[11,13,5,7,0,56,23,34,72]
print(max(s))
print(min(s))
print(len(s))
print(s.index(56))
s.append(7)
print(s)
del s [4]
print(s)
s.sort()
s.reverse()
print(s)

s1=[11,13,5,7,0,56,23,34,72]
s2=[66,67,68]
s1.extend(s2)
print(s1)
'''






#s2=['a','b']

#s.reverse()#逆序存放改变原来元组的值
#s.sort()#排序存放改变原来元组的值
#sorted(s)#排序不改变原来元组的值，只返回一个排序结果
#s.insert(0,0)
#s.append(5)
#s1.extend(s2)
#s1.pop(1)
# s1.remove(3)
# s1.count(88)
# min(s)
# print(len(s))
#del s[0]
# s.clear()
# print(s)
'''
s=[1,2,3,4,5]
s.sort()
print(s)
'''
'''
s = {1,2,3}
#s.add(4)
s.remove(1)
print(s)

'''

#s ={'a':10,'b':20,'c':30,}

#print (s['c'])
'''
a=0
if a==0:
    a+=1
print (a)

'''
'''
a=int(input('请输入一个值:'))
if a>0:
    a+=1
else:
    a-=1
print (a)
'''
'''
a=int(input('输入一个值：'))
if a>0:
    a+=1
elif a==0:
    a-=1
elif a<0:
    a+=2
print (a)
'''
'''
a=[1,2,3,4,5,6,7,8,9]
b=int(input('输入一个值：'))
if b in a:
    print('true')
else:
    print('fasle')
'''
'''
i=0
while i<5:
    print(i)
    i=i+1

'''
'''
a = 1
i = 1
while i <= 10:
    a = a * i
    i += 1
print('10的阶乘为：',a)

'''
#求100以内能被3整除的数
'''
n = 1
for i in range(1,100):
    if i % 3 == 0:
        print(i)
    else:
        n += 1
'''

lists = []
i = 2
for i in range(2,1000):
    n = 2
    for n in range(2,i):
        if i % n == 0:
            break
    else:
        lists.append(i)
print(lists)