N=int(input())
for i in range(1,N+1):
    eachrow=""
    left=" "*(N-i)
    for j in range(1,i+1):
        eachrow+=str(j)+" "
    print(left+eachrow)
"""
input:5
output:
    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5 

"""
