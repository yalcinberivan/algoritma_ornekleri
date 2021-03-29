for i in range(2,7,1):
    for j in range(2,7,1):
        if ((i==2) or (i==3) or (i==5) or (i==7) and (j==2) or (j==3) or (j==5) or (j==7)):
            print(10*j+i)
            