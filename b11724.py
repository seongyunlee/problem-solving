N,M=map(int,input().split())
E={i:[] for i in range(1,N+1)}
for _ in range(M):
    u,v=map(int,input().split())
    E[u].append(v)
    E[v].append(u)
visit=[False]*(N+1)
def dfs(node):
    global visit
    if visit[node]:return
    visit[node]=True
    for n in E[node]:
        dfs(n)
answer=0
for i in range(1,N+1):
    if not visit[i]:
        answer+=1
        dfs(i)
print(answer)