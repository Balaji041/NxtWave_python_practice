S=int(input())
N=int(input())
for i in range(1,N+1):
    string=""
    Sr=S
    left_space=" "*(N-i)
    for j in range(1,i+1):
        string+=str(Sr)+" "
        Sr+=1
    print(left_space+string)
   
        
        
    
"""
input:7 5
output:7 
   7 8 
  7 8 9 
 7 8 9 10 
7 8 9 10 11 
"""
