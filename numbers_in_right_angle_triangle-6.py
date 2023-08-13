N=int(input())
s=1
for i in range(1,N+1):
    string=""
    for j in range(1,i+1):
        string=string+str(j)+" "
    for j in range(1,i):
        string=string+str(j)+" "
    print(string)
"""
input:4
output:
1 
1 2 1 
1 2 3 1 2 
1 2 3 4 1 2 3 
"""
