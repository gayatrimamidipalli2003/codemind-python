n=int(input())
a=list(map(int,input().split()))
x=int(input())
t=-1
for i in range(0,n):
    if a[i]==x:
        print(i)
        break
else:
    print(t)
    
    