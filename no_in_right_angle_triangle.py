N=int(input())
for i in range(1,N+1):
    string=""
    left_space="  "*(N-i)
    for j in range(1,i+1):
        string=str(j)+" "+string
    print(left_space+string)
  """
  input:4
  output:
      1 
    2 1 
  3 2 1 
4 3 2 1 
  """
