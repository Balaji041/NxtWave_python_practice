N=int(input())
sum=0
for i in range(1,N+1):
    digit=int(input())
    count=0
    for j in range(1,digit+1):
        if digit%j==0:
            count+=1
    if count==2:
        sum=sum+digit
print(sum)

"""
input: 5
2
5
6
8
3
output:10
"""
