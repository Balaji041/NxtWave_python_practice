M=int(input())
N=int(input())
string=""
for num in range(M,N+1):
    count=0
    for j in range(1,num):
        if num%j==0:
            count+=1
    if count==1:
        string=string+str(num)+" "
if len(string)==0:
    print("No Prime Numbers Found")
else:
    print(string)

"""
input:3
15
output:3 5 7 11 13 

"""
        
 

        
