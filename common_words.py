a=input().lower()
b=input().lower()
a,b=a.split(),b.split()
for i in b:
    if i in a:
        print(i,end=' ')
        
    