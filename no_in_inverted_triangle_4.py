S=int(input())
N=int(input())
sum=0
for k in range(1,N+1):
    sum+=k
S=(sum+S-1)
for i in range(1,N+1):
    left="  "*(i-1)
    if i==1:
        eachrow=""
        for j in range(1,N+1):
            eachrow=eachrow+str(S)+" "
            S-=1
        print(left+eachrow)
    elif i==N:
        eachrow=left+str(S)
        print(eachrow)
    else:
        eachrow=str(S)+" "
        hollow="  "*(N-i-1)
        S=(S-int(len(hollow)/2)-1)
        eachrow=left+eachrow+hollow+str(S)
        S-=1
        print(eachrow)
"""
input:2
4
output:
11 10 9 8 
  7   5
    4 3
      2
"""
