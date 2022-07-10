n=input()
num=int(n)
s=str(num**2)
if s.endswith(n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')