import sys
sys.setrecursionlimit(10**6)
N,M,V=map(int,input().split())
E={}
for _ in range(M):
    f,t=map(int,input().split())
    if not E.get(f):
        E[f]=[t]
    else:
        E[f].append(t)
    if not E.get(t):
        E[t]=[f]
    else:
        E[t].append(f)
for e in E.values():
    e.sort()
dfs_=[]
visit=[False]*(N+1)
def dfs(now):
    global visit
    global dfs_
    if visit[now]:return
    dfs_.append(now)
    visit[now]=True
    if not E.get(now):return
    for i in E[now]:
        dfs(i)
dfs(V)
print(*dfs_)
now=[V]
visit=[False]*(N+1)
bfs=[]
while now:
    next_=[]
    for b in now:
        if visit[b]:continue
        bfs.append(b)
        visit[b]=True
        if not E.get(b):continue
        for e in E[b]:
            if visit[e]:continue
            next_.append(e)
    now=next_
print(*bfs)

        