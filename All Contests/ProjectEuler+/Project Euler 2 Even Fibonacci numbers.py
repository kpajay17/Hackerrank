#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    
    n = int(input().strip())
    prv=0
    nxt=1
    s=0
    f=0
    while nxt<n:
        if nxt%2==0:
            s+=nxt
        f=prv+nxt
        prv=nxt
        nxt=f
    print(s)