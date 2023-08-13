M=int(input())
N=int(input())
string=""
for i in range(M,N+1):
    l=len(str(i))
    strword=str(i)
    sum=0
    for j in strword:
        sum=sum+int(j)**l
    if sum==i:
        string=string+str(i)+" "
print(string)

"""
input:
150
200
output:
153 
"""
