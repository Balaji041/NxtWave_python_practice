N=int(input())
for i in range(1,N+1):
    if i==1:
        eachrow=""
        for j in range(1,N+1):
            eachrow=eachrow+str(j)+" "
        print(eachrow)
    elif(i==N):
        print("1")
    else:
        hollow="  "*(N-i-1)
        eachrow="1 "+hollow+str(N-i+1)
        print(eachrow)
"""
input:5
output:
1 2 3 4 5 
1     4
1   3
1 2
1
"""
