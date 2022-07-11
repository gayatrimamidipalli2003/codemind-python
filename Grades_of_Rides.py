h,sn,sd=map(int,input().split())
if h>50 and sn>60 and sd>100:
    print(10)
elif h>50 and sn>60:
    print(9)
elif sn>60 and sd>100:
    print(8)
elif h>50 and sd>100:
    print(7)
elif h>50 or sn>60 or sd>100:
    print(6)
else:
    print(5)