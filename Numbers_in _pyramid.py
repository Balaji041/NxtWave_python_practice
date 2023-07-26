N=int(input())
for i in range(1,N+1):
    string=""
    for j in range(N):
        string=string+str(N-j)+" "
    print(string)
"""
input:7 5
output:7 
   7 8 
  7 8 9 
 7 8 9 10 
7 8 9 10 11 
"""
