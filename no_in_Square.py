N=int(input())
for i in range(1,N+1):
    string=""
    for j in range(N):
        string=string+str(N-j)+" "
    print(string)
"""
input:3
output:3 2 1 
3 2 1 
3 2 1
"""
