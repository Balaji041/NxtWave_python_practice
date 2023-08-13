M=int(input())
N=int(input())
S=M*N
for i in range(M):
    string=""
    for j in range(N):
        string=string+str(S)+" "
        S-=1
    print(string)
"""
input:
2
3
output:
6 5 4 
3 2 1 
"""
