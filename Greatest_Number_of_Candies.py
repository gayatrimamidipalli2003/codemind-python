n=int(input())
arr=list(map(int,input().split()))
x=int(input())
max=0
for i in range(0,n):
    if max<arr[i]:
        max=arr[i]
for i in range(0,n):
    if arr[i]+x>=max:
        print(True,end=' ')
    else:
        print(False,end=' ')