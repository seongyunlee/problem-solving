import sys
from collections import defaultdict
from heapq import heappop,heappush
input = sys.stdin.readline
N = int(input())
M = int(input())
E = defaultdict(list)
for _ in range(M):
    a,b,c = map(int,input().split())
    E[a].append([b,c])
S,T = map(int,input().split())
H = [[0,S,[S]]]
D  = [int(1e11)]*(N+1)
D[S] = 0
while H:
    d,n,r = heappop(H)
    if D[n] < d: continue
    if n == T:
        print(d)
        print(len(r))
        print(*r)
        break
    for i,j in E[n]:
        if D[i] > j+d:
            D[i] = j+d
            heappush(H,[D[i],i,r+[i]])
            


