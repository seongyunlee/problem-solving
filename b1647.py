import sys
from heapq import heappop,heappush
input = sys.stdin.readline
N,M = map(int,input().split())
E = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    E[a].append((c,b))
    E[b].append((c,a))
def makeMST(a):
    visit = [False]*(N+1)
    visit[a] = True
    q = []
    for e in E[a]:
        heappush(q,e)
    ans = 0
    maxCost = 0
    while q:
        cost,child = heappop(q)
        if not visit[child]:
            visit[child] = True
            ans += cost
            maxCost = max(maxCost,cost)
            for e in E[child]:
                if not visit[e[1]]:
                    heappush(q,e)
    return ans-maxCost
print(makeMST(1))


