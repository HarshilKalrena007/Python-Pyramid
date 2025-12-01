m=1
n=2
for i in range(5,0,-1):
    for j in range(1,i+1,):
        print("",m,end="")
        m+=2
    m=1+n
    n+=2
    print("")
  
