l=[12,40,10,9,8,-1,21,6]
a=0
for i in range (len(l)-1):
    for j in range (i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
            a+=1
print (l,f'交换次数为{a}')
