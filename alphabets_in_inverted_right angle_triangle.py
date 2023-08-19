N=int(input())
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,N+1):
    name=""
    for j in range(N-i+1):
        name+=string[j]+" "
    print(name)
"""
input:5
output:
A B C D E 
A B C D 
A B C 
A B 
A 
"""
