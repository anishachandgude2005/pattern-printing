for i in range(1,6):# upper half diamond
    for j in range(1,6-i):# print spaces before stars
        print(" ",end="")
    for k in range(1,i*2):# print increasing odd number of stars
        print("*",end="")
    print()
for i in range(1,5):# lower half diamond
    for j in range(0,i):#This print spaces before stars
        print(" ",end="")
    for k in range(1,(5-i)*2):# print decreasing odd  number of stars 
        print("*",end="")
    print()