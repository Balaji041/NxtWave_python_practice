N=int(input())
for i in range(1,N+1):
    eachrow=str(N)+" "
    if i==1 or i==N:
        for j in range(2,N+1):
            eachrow=eachrow+str(N-j+1)+" "
        print(eachrow)
    else:
        hollow=N-2
        eachrow=eachrow+"  "*hollow+str(1)
        print(eachrow)
"""
input:5
output:
5 4 3 2 1 
5       1
5       1
5       1
5 4 3 2 1 
"""
