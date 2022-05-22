n=int(input())
sq=n*n
s=0
while sq:
    rem=sq%10
    s+=rem
    sq//=10
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')
    