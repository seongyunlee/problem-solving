import sys
input = sys.stdin.readline
N = int(input())
M = [input().strip() for _ in range(N)]
E = {i:[] for i in range(N*N)}
for r in range(N):
    for c in range(N):
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            if not (0<=r+dr<N and 0<=c+dc<N): continue
            if M[r+dr][c+dc]=="#":
                E[r*N+c].append((r+dr)*N+c+dc)
cycles = []
visit = set()
def findCycle(u,p,color=[0]*(N*N),parent=[-1]*(N*N)):
    if color[u] == 2: return
    if color[u] == 1:
        v = []
        cur = p
        v.append(cur)
        while cur != u:
            cur = parent[cur]
            v.append(cur)
        cycles.append(v)
        return
    parent[u] = p

    color[u] = 1

    for v in E[u]:
        if v == parent[u]: continue
        #if (u,v) in visit or (v,u) in visit: continue
        visit.add((u,v))
        findCycle(v,u,color,parent)
    color[u] = 2
for i in range(N*N):
    findCycle(i,-1)
    print(cycles)
cycles = [set(c) for c in cycles]
if len(cycles) == 0:
    print(0)
    exit()
common = cycles.pop()
for c in cycles:
    common &= c
print(len(common))
LL = [[k//N+1,k%N+1] for k in common]
print("\n".join([f"{r} {c}" for r,c in LL]))