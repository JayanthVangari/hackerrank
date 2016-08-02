#!/bin/python

import sys
l=list()
n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
i=0
while i < len(A):
    index=i
    for k in A[i+1:]:
        index=index+1
        if A[i]==k:
            d=abs(i-index)
            l.append(d)
    i=i+1
if len(l)!=0:
    print sorted(l)[0]
else:
    print -1