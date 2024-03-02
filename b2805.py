import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = list(map(int,input().split()))
left = 0
right = 1000000000
while left<right:
    mid = (left+right)//2 + (left+right)%2
    total = 0
    for a in A:
        total += max(0,a-mid)
    if total>=M:
        left = mid
    else:
        right = mid-1
print(left)
