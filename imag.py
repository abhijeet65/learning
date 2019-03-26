
from collections import *
import heapq

while(True):
    s="hello"
    l=list(s)
    print(l)
    p=":".join(l)
    print(p)

    print("Input The values")
    l=[]
    l=list(map(int,input().split(" ")))
    print(l)
    high=max(l)
    low=min(l)
    print("high is = {} and low is= {}".format(high,low))
    print("Top 3 elements")

    c=Counter(l)
    top_three=c.most_common(3)
    print(top_three)
    print(c)

    newlist=map(int,input("Enter the list of 2:").split(" "))
    n=int(input("which largest"))
    print(heapq.nlargest(n,newlist))

    p=int(input("which smallest"))
    print(heapq.nsmallest(p,newlist))

