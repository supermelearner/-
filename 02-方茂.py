a=int(input('请输入你的成绩:'))
if a<60 :
    l=0
if a>=60 :
    l=1+(a-60)*0.1
print (f'你的绩点为{l}')
