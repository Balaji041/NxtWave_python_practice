N=int(input())
coun=0
for i in range(1,N+1):
    s="True"
    for j in range(2,11):
        if (i%j==0):
            s="False"
            break
    if s=="True":
        coun+=1
print(coun)

"""
input:12
output:2
"""
