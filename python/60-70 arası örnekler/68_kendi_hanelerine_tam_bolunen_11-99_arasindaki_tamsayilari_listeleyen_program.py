for i in range(1,9,1):
    for j in range(1,9,1):
        ts=10*i+j
        if (ts%i==0 and ts%j==0) :
            print(ts)
            