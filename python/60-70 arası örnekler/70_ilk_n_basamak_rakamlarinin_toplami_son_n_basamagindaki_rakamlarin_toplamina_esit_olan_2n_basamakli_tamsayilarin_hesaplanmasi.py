for i in range(1,9,1):
    for j in range(0,9,1):
        for k in range(0,9,1):
            for m in range(0,9,1):
                if (i+j==k+m):
                    print(1000*i+100*j+10*k+m)
                    
                