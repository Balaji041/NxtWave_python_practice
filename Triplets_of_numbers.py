N=int(input())
count=0
for i in range(1,N+1):
    for j in range(2,N+1):
        for k in range(3,N+1):
            if i+j+k==N and i<j<k:
                count+=1
print(count)

"""
input:10
output:4
"""
