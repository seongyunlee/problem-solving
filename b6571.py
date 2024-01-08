import sys
input=sys.stdin.readline
fib=[1,1]
def findMaxLeft(tar):
    left=0
    right=len(fib)-1
    while left<right:
        mid=(left+right)//2
        if fib[mid]<tar:
            left=mid+1
        elif fib[mid]>tar:
            right=mid
    return right
def findMinRight(tar):
    left=0
    right=len(fib)-1
    while left<right:
        mid=(left+right)//2
        if fib[mid]<tar:
            left=mid
        elif fib[mid]>tar:
            right=mid-1
    return right
while True:
    fib.append(fib[-2]+fib[-1])
    if fib[-1]>10000000000:break
while True:
    A,B=map(int,input().split())
    if A==0 and B==0:break


