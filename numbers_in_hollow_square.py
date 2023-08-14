N=int(input())
for i in range(1,N+1):
    string=""
    for j in range(1,N+1):
        if i==1 or i==N:
            string=string+str(j)+" "
        else:
            if j==1 or j==N:
                string=string+str(j)+" "
            else:
                string=string+"  "
    print(string)
"""
input:4
output:
1 2 3 4 
1     4 
1     4 
1 2 3 4 
"""
