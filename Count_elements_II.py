a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
arr=set(arr)
brr=set(brr)
r=[]
for i in arr:
    if i not in brr:
        r.append(i)
for i in brr:
    if i not in arr:
        r.append(i)
print(len(r))