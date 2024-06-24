import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,R,Q = map(int, input().split()) 
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a].append([b,1])
    G[b].append([a,1])
def doDown(p,cur):
    for idx,g in enumerate(G[cur]):
        if g[0]==p: continue
        G[cur][idx][1] = 0
        doDown(cur,g[0])
cnt = [0]*(N+1)
def count(cur):
    child = 1
    for g in G[cur]:
        if g[1]==0:
            child += count(g[0])
    cnt[cur] = child
    return child
doDown(0, R)
count(R)
for _ in range(Q):
    print(cnt[int(input())])
