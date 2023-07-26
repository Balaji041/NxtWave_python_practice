M_rows=int(input())
N_cols=int(input())
for i in range(M_rows):
    string=""
    num=7
    for j in range(N_cols):
        string=string+str(num)+" "
        num+=1
    print(string)

"""
input:2

input:3
output:7 8 9 
7 8 9
"""
