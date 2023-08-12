N=int(input())
s=1
for i in range(N):
    string=""
    for j in range(i+1):
        string=string+str(s)+" "
        s+=1
    print(string)
"""
input:5
output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""
