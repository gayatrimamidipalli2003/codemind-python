n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    if i%2!=0:
        sum+=i
    if i%2==0:
        break
    i+=1
print(sum)