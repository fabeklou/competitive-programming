from collections import deque
import sys

dq=deque()
l = int(input())
val=0

for _ in range(l):
    dq.append(input())

L=R=0
STACK=[]
SS=0
loop=0

for ins in dq:
    if loop==0 and 'add' in ins:
        val+=1
        continue
    STACK.append(ins)
    loop=loop+1 if ins=='end' else loop-1
    SS+=1
    if loop==0:
        curr=0
        L=R=SS//2
        # Evaluate expression in the stack
        if curr + val > 2**32-1:
            print('OVERFLOW!!!')
            sys.exit()
        val+=curr
        STACK=[]
print(val)
