n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    for j in range(0,i+1):
        if i==j*j:
            s+=i
print(s)