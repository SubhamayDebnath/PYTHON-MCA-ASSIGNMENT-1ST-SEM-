num=5
g=1
for i in range(num,0,-1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(g):
        if k % 2==0:
            print("0",end="")
        else:
            print("1",end="")
    g+=1
    print("")
