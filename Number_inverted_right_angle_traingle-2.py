N=int(input())
K=0
for i in range(1,N+1):
    K=K+i
for j in range(N):
    string=''
    space="  "*j
    for k in range(N-j):
        string=string+str(K)+" "
        K=K-1
    print(space+string)
"""
input:4
output:
10 9 8 7 
  6 5 4 
    3 2 
      1 
"""
