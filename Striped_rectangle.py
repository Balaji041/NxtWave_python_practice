Row_M=int(input())
col_N=int(input())
for i in range(1,Row_M+1):
    if i%2==0:
        print("- "*col_N)
    else:
        print("+ "*col_N)
"""
input:5
input:7
output:
+ + + + + + +
- - - - - - -
+ + + + + + +
- - - - - - -
+ + + + + + +

"""
