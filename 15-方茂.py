ls1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
ls2=[[],[],[]]
#1
for i in range (len(ls1)):
    for j in range (len(ls1[i])):
        if ls1[i][j]>=10 :
            print (f'{ls1[i][j]}',end='  ')
        else:
            print (f'{ls1[i][j]}',end='    ')
    print ()
#转化
for i in range (len(ls1[i])):
    for j in range (len(ls1)):
        ls2[i].append(ls1[j][i])
#
print ()
#2
for i in range (len(ls2)):
    for j in range (len(ls2[i])):
        if ls2[i][j]>=10 :
            print (f'{ls2[i][j]}',end='  ')
        else:
            print (f'{ls2[i][j]}',end='    ')
    print ()
