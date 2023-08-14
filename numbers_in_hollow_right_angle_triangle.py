N=int(input())
for i in range(1,N+1):
    if i>2 and i<N:
        holow="  "*(i-2)
        number="1 "+holow+str(i)+" "
        print(number)
    else:
        numner=""
        for j in range(1,i+1):
            numner=numner+str(j)+" "
        print(numner)

"""
input:5
output:
1 
1 2 
1   3 
1     4 
1 2 3 4 5
"""
