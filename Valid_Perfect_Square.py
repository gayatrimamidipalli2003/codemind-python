n=int(input())
for i in range(0,n):
    a=int(input())
    for i in range(0,a):
        if a==i*i:
            print('True')
            break
    else:
        print('False')