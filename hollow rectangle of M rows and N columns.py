M=int(input())
N=int(input())
K=M*N
for i in range(1,M+1):
    if i==1 or i==M:
        eachrow=""
        for j in range(1,N+1):
            eachrow+=str(K)+" "
            K-=1
        print(eachrow)
    else:
        eachrow=str(K)+" "
        holow="  "*(N-2)
        K=(K-int(len(holow)/2)-1)
        eachrow=eachrow+holow+str(K)
        K-=1
        print(eachrow)

"""
input:3
6
output:
18 17 16 15 14 13 
12         7
6 5 4 3 2 1 
"""
  
