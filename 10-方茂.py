def nk(n):
    if n==0 :
        return 0.1*(10**(-3))
    else:
        return nk(n-1)*2

for i in range (2,1000):
    l=nk(i)
    if l>8848.18 :
        break
print (f'需要{i}次')
