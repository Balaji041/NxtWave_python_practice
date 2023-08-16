N=int(input())
startnumber=int(input())
second=startnumber
for i in range(1,N+1):
    if i==1:
        eachrow=""
        for j in range(1,N+1):
            eachrow=eachrow+str(startnumber)+" "
            startnumber+=1
        print(eachrow)
    elif i==N:
        space=" "*(i-1)
        each=""
        for j in range(N-i+1):
            each=space+str(second)+" "
        print(each)
    else:
        space=" "*(i-1)
        hollow="  "*(N-i-1)
        eachrow=space+str(second)+" "+hollow+str(second+N-i)+" "
        print(eachrow)
        startnumber+=1
"""
input:
5
7
output:
7 8 9 10 11 
 7     10 
  7   9 
   7 8 
    7
"""
