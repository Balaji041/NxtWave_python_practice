N=int(input())
count=0
for i in range(1,N):
    for j in range(2,N+1):
        if i+j==N and i<j:
            count+=1
print(count)

"""
input:7
output:3
"""
