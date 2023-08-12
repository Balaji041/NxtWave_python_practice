N=int(input())
for i in range(N):
    string=""
    for j in range(1,N-i+1):
        string=string+str(j)+" "
    print(string)
  """
  input:5
  output:
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
  """
