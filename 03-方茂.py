a=int(input('请输入你的成绩:'))
print ('成绩等级:',end=' ')
if a<60 :
    print ('不及格')
if 70>a>=60 :
    print ('及格')
if 80>a>=70 :
    print ('一般')
if 90>a>=80 :
    print ('良好')
if 100>a>=90 :
    print ('优秀')
if a==100 :
    print ('满分')
