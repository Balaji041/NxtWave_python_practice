n = int(input())

for row_num in range(n+1):
    row_output = ""
    seq_num = n-row_num
    while seq_num > 0:
        row_output = row_output + str(seq_num)
        seq_num = seq_num - 1
    print(row_output)
"""
input:5
output:
54321
4321
321
21
1
"""
