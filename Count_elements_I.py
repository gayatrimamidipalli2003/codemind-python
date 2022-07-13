x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
count=0
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
            count+=1
print(count)