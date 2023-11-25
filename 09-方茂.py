def cou(n):
    if n==1 :
        return (1)
    if n>1 :
        return (cou(n-1)+n)

a=cou(100)
print (a)
