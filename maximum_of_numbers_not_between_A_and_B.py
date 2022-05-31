n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
max=0
for i in range(0,n):
    if arr[i]<a or arr[i]>b:
        if max<arr[i]:
            max=arr[i]
if max==0:
    print('-1')
else:
    print(max)
        