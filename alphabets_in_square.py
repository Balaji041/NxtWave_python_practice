N=int(input())
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,N+1):
    name=""
    for j in range(N):
        name+=string[j]+" "
    print(name)
"""
input:4
output:
A B C D 
A B C D 
A B C D 
A B C D 
"""
