N=int(input())
start=1
for i in range(1,N+1):
    if i==1:
        each=""
        for j in range(1,N+1):
            each+=str(start)+" "
            start+=1
        print(each)
    elif i==N:
        print(str(start))
    else:
        eachrow=str(start)+" "
        hollow="  "*(N-i-1)
        eachrow=eachrow+hollow
        start=int(start)+int(len(hollow)/2)+1
        print(eachrow+str(start))
        start+=1
"""
input:4
output:
1 2 3 4 
5   7
8 9
10

"""
