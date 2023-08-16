N=int(input())
for i in range(1,N+1):
    leftspace=" "*(N-i)
    if i==1 or i==N:
        eachrow=""
        for j in range(1,i+1):
            eachrow=eachrow+str(j)+" "
        print(leftspace+eachrow)
    else:
        holow=" "*(2*(i-2))
        eachrow="1 "+holow+str(i)
        print(leftspace+eachrow)
"""
input:5
output:
    1 
   1 2
  1   3
 1     4
1 2 3 4 5
"""
