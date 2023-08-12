S=int(input())
N=int(input())
for i in range(1,N+1):
    string=""
    for j in range(1,i+1):
        string=string+str(S)+" "
        S+=1
    print(string)
"""
input:
10
5
output:
10 
11 12 
13 14 15 
16 17 18 19 
20 21 22 23 24
"""
