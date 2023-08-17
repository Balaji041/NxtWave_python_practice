S=int(input())
N=int(input())
start=S
for i in range(1,N+1):
    left="  "*(i-1)
    if i==1:
        eachrow=""
        for j in range(1,N+1):
            eachrow+=str(start)+" "
            start+=1
        print(left+eachrow)
    elif(i==N):
        each=str(start)+" "
        print(left+each)
    else:
        eachrow=str(start)+" "
        holow="  "*(N-i-1)
        start+=1
        eachrow+=holow+str(start)+" "
        start+=1
        print(left+eachrow)
"""
inout:
2
4
output:
2 3 4 5 
  6   7 
    8 9 
      10 
"""
            
