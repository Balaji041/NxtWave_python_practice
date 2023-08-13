S=int(input())
N=int(input())
m=2
for i in range(2,N+2):
    string=""
    for j in range(m):
        string=string+str(S)+" "
        S+=1
    m=m+2
    print(string)

"""
input:
2
4
output:
2 3 
4 5 6 7 
8 9 10 11 12 13 
14 15 16 17 18 19 20 21 
"""
