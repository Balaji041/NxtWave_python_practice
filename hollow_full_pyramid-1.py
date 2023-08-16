N=int(input())
for i in range(1,N+1):
    left=" "*(N-i)
    if i>=2 and i<N:
        hollow="  "* (i-2)
        each=left+"* "+hollow+"* "
        print(each)
    else:
        print(left+"* "*i)
"""
input:5
output:
    * 
   * * 
  *   * 
 *     * 
* * * * * 
"""
