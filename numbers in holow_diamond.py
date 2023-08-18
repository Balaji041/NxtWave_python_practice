N=int(input())
if N==1:
    first_last=" "*(N-1)
    print(first_last+"1")
else: 
    first_last=" "*(N-1)
    print(first_last+"1")
    holo=-1
    for i in range(2,N+1):
        left=" "*(N-i)
        holo=holo+2
        holow=" "*holo
        print(left+"1"+holow+str(i))
    for j in range(1,N-1):
        left=" "*(j)
        holo=holo-2
        holow=" "*holo
        print(left+"1"+holow+str(N-j))
    first_last=" "*(N-1)
    print(first_last+"1")
    
    

"""
input:5
output:
    1
   1 2
  1   3
 1     4
1       5
 1     4
  1   3
   1 2
    1
"""
