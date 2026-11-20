#Hollow square
for i in range(1,6):                    #this loop define the number of rows
    for j in range(1,6):                #this loop control the column
        if i==1 or i==5 or j==1 or j==5:#print the star on boundary
            print("*",end="")
        else:
            print(" ",end="")           #print the spaces inside the rectangle
    print()                             #move to next line