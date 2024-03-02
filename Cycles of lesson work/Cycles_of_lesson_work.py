from math import *


# for x in range(10):
#     R=float(input("{0} R: ").format(x+1))
#     if R>0:
#         S=pi*R**2
#     else:
#         S="R peab> kui 0 olema"
#     print("S={0}".format(S))
    

# x=0

# while True:
#     x+=1
#     R=float(input("{0} R: ").format(x+1))
#     if R>0:
#         S=pi*R**2
#     else:
#         S="R peab> kui 0 olema"
#     print("S={0}".format(S))
#     if x==10:
#         break
    

# #10 R
# x=0
# while x<10:
#     x+=1
#     R=float(input("{0} R: ").format(x+1))
#     if R>0:
#         S=pi*R**2
#     else:
#         S="R peab> kui 0 olema"
#     print("S={0}".format(S))
    

#10 
x=0
while x < 10:
    R = float(input("{0} R: ").format(x+1))
    if R > 0:
        S= pi * R ** 2
        x+=1
    else:
        S="R peab> kui 0 olema"
    print("S={0}".format(S))
