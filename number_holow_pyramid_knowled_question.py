number  = int(input())
rows = int(input())

for i in range(rows):
    row = ""
    if i == 0 or i == rows-1:
        if i == 0:
            for j in range(rows):
                row += str(number) + " "
                number += 1
        else:
            left_space = " " * i
            row += left_space + str(number) + " "
    else:
        left_space = " " * i
        row += left_space + str(number) + " "
        hollow_space = "  " * (rows-2-i)
        number += (rows-2-i)+1
        row += hollow_space + str(number) +" "
        number += 1
    print(row)
"""
input:
3
4
output:
3 4 5 6 
 7   9
  10 11
   12
"""
