n=int(input())
for i in range(0,n):
    a=int(input())
    temp=a
    rev=0
    while a:
        rem=a%10
        rev=rev*10+rem
        a//=10
    if temp==rev:
        print(True)
    else:
        print(False)
    

    
    