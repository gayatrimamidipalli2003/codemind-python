n=int(input())
b=[]
for i in range(n):
    a=list(map(int,input().split()))
    b.append(a)
l,r=0,0
for i in range(n):
    for j in range(n):
        if i==j:
            l+=b[i][j]
        if i+j==n-1:
            r+=b[i][j]
print("Principal Diagonal:"+str(l))
print("Secondary Diagonal:"+str(r))