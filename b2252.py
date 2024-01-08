import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N,M = map(int,input().split())
parent = {i:[] for i in range(1,N+1)}
child = {i:[] for i in range(1,N+1)}
for _ in range(M):
    f,t = map(int,input().split())
    child[f].append(t)
    parent[t].append(f)
visited = [False]*(N+1)
ans = []
def visitParent(node):
    if visited[node]:return
    visited[node] = True
    for p in parent[node]:
        visitParent(p)
    ans.append(node)
def visit(node):
    if visited[node]:return
    visited[node] = True
    for p in parent[node]:
        visitParent(p)
    ans.append(node)
    for c in child[node]:
        visit(c)
for i in range(1,N+1):
    visit(i)
print(*ans)