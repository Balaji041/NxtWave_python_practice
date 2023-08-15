M=int(input())
N=int(input())
num=1
for i in range(1,M+1):
    
    if i==1 or i==M:
        string=""
        for j in range(1,N+1):
            string+=str(num)+" "
            num+=1
        print(string)  
    else:
        eachrow=(str(num)+" ")
        hollow="  "*(N-2)
        num=num+int(len(hollow)/2)+1
        eachrow=eachrow+hollow+(str(num)+" ")
        num+=1
        print(eachrow)
"""
input:
4
5
output:
1 2 3 4 5 
6       10 
11       15 
16 17 18 19 20 
"""
        
    
