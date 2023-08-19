N=int(input())
for i in range(1,2*N+2):
    if i==1 or i==(2*N+1) or i==(2*N+2)//2:
        print("* "*N)
    elif i>=(2*N+2)//2:
        print("* "+"  "*(N-2)+"*")
    else:
        print("* "+"  "*(N-2)+"*")
"""
input:5
output:
* * * * * 
*       *
*       *
*       *
*       *
* * * * * 
*       *
*       *
*       *
*       *
* * * * * 
"""
