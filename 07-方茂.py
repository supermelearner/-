import random as r
l=[]
for i in range (10):
    l.append(r.randint(1,100))
a=max(l)
b=min(l)

print (l)
print (f'最大值为{a}')
print (f'最小值为{b}')
