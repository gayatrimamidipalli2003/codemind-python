n=int(input())
arr=list(map(int,input().split()))
min=arr[0]
c=0
for i in range(0,n):
    if min>arr[i]:
        min=arr[i]
while min:
    c=0
    for j in range(0,n):
        if arr[j]%min==0:
            c+=1
    if c==n:
        print(min)
        break
    min-=1