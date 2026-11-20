#Hollow Right-Angled Triangle
for i in range(1,6):                    #this loop handle number of rows
    for j in range(1,6):                #this loop handle number of columns
        if j==1 or i==5 or j==i:        #print first column ,5th row and diagonal line
            print("*",end="")
        else:
            print(" ",end="")           #print Spaces inside the triangle
    print()                             #move to next line