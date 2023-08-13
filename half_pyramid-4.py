N=int(input())
k=int(input())
s=N+int((k*(k+1))/2)-1
m=s
for i in range(1,k+1):
    string=""
    for j in range(i):
        string=string+str(m)+" "
        m-=1
    print(string)
"""
input:
10
5
output:
24 
23 22 
21 20 19 
18 17 16 15 
14 13 12 11 10 
"""
