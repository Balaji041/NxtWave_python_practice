N=int(input())
count=0
for i in range(1,N+1):
    if N%i==0:
        count+=1
if count>2:
    print("True")
else:
    print("False")
"""
input:12
output:True
"""
