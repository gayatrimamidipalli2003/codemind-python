n=int(input())
sq_n=n**2
rev_n=0
while n:
    rem=n%10
    rev_n=rev_n*10+rem
    n//=10
sq_rev_n=rev_n**2
adam=0
while sq_rev_n:
    rem=sq_rev_n%10
    adam=adam*10+rem
    sq_rev_n//=10
if sq_n == adam:
    print(True)
else:
    print(False)
    