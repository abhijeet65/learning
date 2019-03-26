from itertools import *
#permutaions of size k
lst=list(map(str,input().split(" ")))
print(lst)
print("Permuations are:")
perm=permutations(lst,2)
for i in perm:
    print(i)