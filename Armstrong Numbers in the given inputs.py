N=int(input())
for i in range(1,N+1):
    digit=int(input())
    digit=str(digit)
    l=len(digit)
    sum=0
    for i in digit:
        sum=sum+(int(i)**l)
    if sum==int(digit):
        print(digit)
"""
input:4
8
27
153
374
output:
8
153
"""
