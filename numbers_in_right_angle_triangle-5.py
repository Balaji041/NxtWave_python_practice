S=int(input())
N=int(input())
K=0
for i in range(1,N+1):
    K=K+i
for j in range(1,N+1):
    string=""
    for k in range(j):
        string=string+str(K+S-1)+" "
        S-=1
    print(string)
  """
  input:
  6
  4
  output:
15 
14 13 
12 11 10 
9 8 7 6
  """
