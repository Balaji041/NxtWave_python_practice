N=int(input())
for i in range(1,N+1):
    if i==1:
        eachrow=""
        for j in range(1,N+1):
            eachrow=eachrow+str(j)+" "
        print(eachrow)
    elif i==N:
        left=" "*(i-1)
        eachrow=left+str(1)
        print(eachrow)
    else:
        left=" "*(i-1)
        hollow="  "*(N-i-1)
        eachrow=left+"1 "+hollow+str(N-i+1)
        print(eachrow)
"""
input:5
output:
1 2 3 4 5 
 1     4
  1   3
   1 2
    1
"""
