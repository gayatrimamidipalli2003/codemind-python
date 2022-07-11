n=int(input())
c=0
for i in range(0,n):
    a=input()
    if a.isdecimal():
        print('True')
    else:
        print('False')