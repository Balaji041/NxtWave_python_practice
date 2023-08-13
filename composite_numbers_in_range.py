M=int(input())
N=int(input())
for i in range(M,N+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count>2:
        print(i)

"""
input:
2
9
output:
4
6
8
9
"""
