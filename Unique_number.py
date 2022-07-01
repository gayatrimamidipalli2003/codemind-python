s=input()
n=list(s)
n=set(n)
if len(s)==len(n):
    print('Unique Number')
else:
    print('Not Unique Number')