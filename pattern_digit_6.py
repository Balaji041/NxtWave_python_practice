N=int(input())
for i in range(1,2*N):
    if i==1 or i==(N*2)/2 or i==(2*N)-1:
        print("* "*N)
    elif i<(2*N)/2:
        print("* ")
    else:
        print("* "+"  "*(N-2)+"* ")
"""
input:4
output:
* * * * 
* 
* 
* * * * 
*     * 
*     * 
* * * *
"""
