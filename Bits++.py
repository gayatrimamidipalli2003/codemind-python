n=int(input())
c=0
for i in range(0,n):
    a=input()
    for j in a:
        if j=='+':
            c+=1
    else:
        c-=1
print(c)