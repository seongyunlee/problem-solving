import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
M = [list(map(int,input().split())) for _ in range(int(input()))]
now = [(0,A)]
goal = sorted(A)
visited = set()
while now:
    cost, nowA = heappop(now)
    if tuple(nowA) in visited:
        continue
    visited.add(tuple(nowA))
    if nowA == goal:
        print(cost)
        exit()
    for a,b,c in M:
        newA = nowA[:]
        newA[a-1],newA[b-1] = newA[b-1],newA[a-1]
        if not tuple(newA) in visited:
            heappush(now,(cost+c,newA))
print(-1)
