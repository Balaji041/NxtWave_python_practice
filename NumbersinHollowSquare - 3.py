S=int(input())
N=int(input())
start=S
for i in range(1,N+1):
    if i==1 or i==N:
        each=""
        for j in range(1,N+1):
            each=each+str(start)+" "
            start+=1
        print(each)
    else:
        eachrow=str(start)+" "
        holow="  "*(N-2)
        start+=int(len(holow)/2)+1
        eachrow=eachrow+holow+str(start)
        start+=1
        print(eachrow)
"""
input:
2
3
output:
2 3 4 
5   7
8 9 10
"""
