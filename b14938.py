import sys
from heapq import heappop,heappush
N,M,R = map(int,sys.stdin.readline().split())
D = list(map(int,sys.stdin.readline().split()))
E = {i:[] for i in range(N)}
for _ in range(R):
    a,b,c = map(int,sys.stdin.readline().split())
    E[a-1].append((b-1,c))
    E[b-1].append((a-1,c))
def dijkstra(start):
    dist = [float('inf')]*(N+1)
    dist[start] = 0
    q = [(0,start)]
    while q:
        c,x = heappop(q)
        if dist[x] < c:
            continue
        for nx,nc in E[x]:
            if dist[nx] > c+nc:
                dist[nx] = c+nc
                heappush(q,(c+nc,nx))
    return dist
S = [dijkstra(d) for d in range(N)]
print(max(sum([D[i] for i in range(N) if S[d][i] <= M]) for d in range(N)))
