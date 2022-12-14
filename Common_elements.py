a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
k=[]
for i in arr:
    for j in brr:
        if i not in k and i==j:
            k.append(i)
print(*k)