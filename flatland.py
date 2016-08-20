#!/bin/python

import sys
import math

def init_large(a,b,c):
    temp1=a
    if b<c:
        if c-b>temp1:
            temp1=c-b
    return temp1    
    
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
k = sorted(map(int,raw_input().strip().split(' ')))
prev=0
temp=init_large(k[0],k[len(k)-1],n-1)
for i in k:
    med=(i-prev)/2
    if med>=1:
        med=int(math.ceil(med))
    else:
        med=0
    prev=i
    if med > temp:
        temp=med
print temp        
    
    