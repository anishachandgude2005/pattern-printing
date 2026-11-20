for i in range(1,6):
    for j in range(1,i):#This print space
        print(" ",end="")
    for k in range(1,(6-i)*2):#This print star
        print("*",end="")
    print()