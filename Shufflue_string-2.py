S1=input()
S2=input()
string=""
for i in range(len(S1)):
    if i%2==0:
        string+=S1[i]
    else:
        string+=S2[i]
print(string)
"""
input:bring
camel
output:baieg
"""
