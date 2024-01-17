A = {}
N = int(input())
E = {i:[] for i in range(1,N+1)}
for _ in range(N):
    f,t,c = map(int,input().split())
    E[f].append([t,c])
    E[t].append([f,c])
P = {i:[] for i in range(1,N+1)}
AC = [0]*(N+1)
L = [0]*(N+1)
P = [None]*(N+1)
def dfs(prev,idx,cost,level):
    L[idx]=level
    AC[idx] = cost
    for ch,co in E[idx]:
        P[ch] = [idx,co]
        if ch==prev:continue
        dfs(idx,ch,cost+co,level+1)
dfs(-1,1,0,0)
for _ in range(int(input(()))):
    a,b = map(int,input().split())
    ans = 0
    while L[a]==L[b]:
        if L[a]<L[b]:
            cost += P[b][1]
            b = P[b][0]