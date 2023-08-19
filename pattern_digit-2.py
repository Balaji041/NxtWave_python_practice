N=int(input())
for i in range(1,2*N):
    if i==1 or i==(2*N-1) or i==((2*N)/2):
        print("* "*N)
    elif(i<(2*N)/2):
        print("  "*(N-1)+"* ")
    else:
        print("* ")
"""
input:5
output:
* * * * * 
        * 
        * 
        * 
* * * * * 
* 
* 
* 
* * * * *
"""
