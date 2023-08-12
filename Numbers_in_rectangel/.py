M=int(input())
N=int(input())
num=1
for i in range(M):
    string=""
    for j in range(N):
        string=string+str(num)+" "
        num+=1
    print(string)
        
    
"""
input:
2
3
output:
1 2 3 
4 5 6 
"""
