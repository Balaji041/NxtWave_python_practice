N=int(input())
count=0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if i**2+j**2==k**2 and i<j<k:
                count+=1
print(count)

"""
input:5
output:1
"""
