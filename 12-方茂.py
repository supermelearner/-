k=int(input('请输入需要判断的数字：'))
for i in range(2,k):
    flag=0
    if (k%i==0):
        flag+=1
        print (f'{k}不是素数')
        break

if flag==0 :
    print (f'{k}是素数')


