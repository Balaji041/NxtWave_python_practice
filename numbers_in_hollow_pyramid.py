N=int(input())
for i in range(1,N):
    leftspace=N-i
    middlespace=(2*N-1)-((2*leftspace)+2)
    if i==1:
        print(" "*leftspace+"5")
    else:
        print(" "*leftspace+"5"+" "*middlespace+str(5+i-1))
final=""
for j in range(N):
    final=final+str(5+j)+" "
print(final)

"""
input:5
output:
    5
   5 6
  5   7
 5     8
5 6 7 8 9 
"""
