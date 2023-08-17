N=int(input())
startnumber=0
for i in range(N):
    startnumber+=(N-i)
for j in range(1,N+1):
    if j==1:
        eachrow=""
        for k in range(1,N+1):
            eachrow+=str(startnumber)+" "
            startnumber-=1
        print(eachrow)
    elif(j==N):
        eachrow=str(startnumber)
        print(eachrow)
    else:
        eachrow=str(startnumber)+" "
        holow="  "*(N-j-1)
        startnumber=(startnumber-int(len(holow)/2))-1
        eachrow+=holow+str(startnumber)
        startnumber-=1
        print(eachrow)
"""
input:4
output:
10 9 8 7 
6   4
3 2
1
"""
