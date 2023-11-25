ls1=[12,40,10,9,8,-1,21,-6]
ls2=[12,7,10,9,88,-1,21,-6,10]

yes=[]#12,10,9,-1,21,-6
no=[]#7,40,88,8
s=[0]

for i in range (len(ls1)):
    flag=0
    for j in range (len(ls2)):
        if ls1[i]==ls2[j] :
            if (ls1[i] not in yes) and (ls2[j] not in yes):
                yes.append(ls1[i])
            flag+=1
    if flag==0 :
        no.append(ls1[i])

for i in range (len(ls2)):
    flag=0
    for j in range (len(ls1)):
        if ls2[i]==ls1[j] :
            flag+=1
    if flag==0 :
        no.append(ls2[i])

print (f'相同元素为{yes}')
print (f'不同为{no}')
