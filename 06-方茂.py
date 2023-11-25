l=[12,40,10,9,8,-1,21,6]
a=0
for i in range (len(l)-1,0,-1):
    for j in range (i):
        if l[j]>l[j+1] :
            l[j],l[j+1]=l[j+1],l[j]
            a+=1
print (l,f'交换次数为{a}')






