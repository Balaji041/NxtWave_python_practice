M=int(input())
N=int(input())
sum=0
for i in range(M,N+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        sum+=i
print(sum)
"""
input:
3
7

output:
15
"""
