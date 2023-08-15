M=int(input())
N=int(input())
for i in range(1,M+1):
    nextnum=8
    string="7 "
    if i==1 or i==M:
        for j in range(2,N+1):
            string=string+str(nextnum)+" "
            nextnum+=1
        print(string)
    else:
        hollow="  "*(N-2)
        string=string+hollow+str(7+N-1)+" "
        print(string)
      """
      input:
      4
      3
      output:

7 8 9 
7   9 
7   9 
7 8 9 
      """
