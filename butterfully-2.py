N=int(input())
for i in range(1,N+1):
    print("* "*(i)+"  "*(N-i)+"  "*(N-i)+"* "*(i))
for i in range(N+1):    
    print("* "*(N-i)+"    "*i+"* "*(N-i))

"""
input:5
output:
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

"""
