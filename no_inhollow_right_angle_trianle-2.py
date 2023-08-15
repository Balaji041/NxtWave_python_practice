N=int(input())
for i in range(1,N+1):
    if i==N:
        eachrow=""
        for j in range(N):
            eachrow=eachrow+str(N-j)+" "
        print(eachrow)
    elif i==1:
        leftspace=" "*(N*2-2)
        eachrow=leftspace+"1 "
        print(eachrow)
    else:
        spacce=" "*(2*(N-i))
        holow="  "*(i-2)
        each=spacce+(str(i)+" ")+holow+"1 "
        print(each)
"""
input:6
output:
          1 
        2 1 
      3   1 
    4     1 
  5       1 
6 5 4 3 2 1 
"""
            
