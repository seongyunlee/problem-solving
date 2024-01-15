import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N,M = map(int,input().split())
L = [list(map(int,input().split()))[1:] for _ in range(M)]
child = [[] for _ in range(N+1)]
parent = [[] for _ in range(N+1)]
for l in L:
    for i in range(len(l)-1):
        f,t = l[i:i+2]
        parent[t].append(f)
        child[f].append(t)  
visit = [False]*(N+1) 
indegree = [len(parent[idx]) for idx in range(N+1)]
Q = deque()
ans = []
def checkCycle(here,V):
    if V[here]:
        return V[here]==-1
    V[here] = -1
    for c in child[here]:
        if checkCycle(c,V):
            return True
    V[here] = 1
    return False
for i in range(1,N+1):
    if indegree[i]==0:
        Q.append(i)
        visit[i]=True
if any([checkCycle(idx,[0]*(N+1)) for idx in range(1,N+1)]):
    print(0)
    exit()
while Q:
    k = Q.popleft()
    ans.append(k)
    for c in child[k]:
        if not visit[c]:
            indegree[c]-=1
            if indegree[c]==0:
                Q.append(c)
                visit[c]=True
print(*ans,sep="\n")