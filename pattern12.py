for i in range(1,6):                  # upper half of butterfly
    
    for j in range(1,i+1):            # Print increasing stars on the left side
        print("*", end=" ")

    for j in range(1,(5-i)*2+1):      # Print spaces between the two wings
        print(" ", end=" ")

    
    for j in range(1,i+1):            # Print increasing stars on the right side
        print("*",end=" ")

    print()


for i in range(4,0,-1):               # Lower half of butterfly

    
    for j in range(1,i+1):             # Print decreasing stars on the left side
        print("*",end=" ")

    
    for j in range(1, (5-i)*2+1):       # Print spaces between the two wings
        print(" ",end=" ")

    
    for j in range(1,i+1):             # Print decreasing stars on the right side
        print("*",end=" ")

    print()
