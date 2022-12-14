a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
arr=set(arr)
brr=set(brr)
c=0
for i in arr:
    if i in brr:
        c+=1
print(c)