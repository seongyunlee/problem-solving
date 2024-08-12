import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,M,K = map(int,input().split())
C = list(map(int,input().split()))
E = {i: [] for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    E[a].append(b)
    E[b].append(a)
group = {}
visit = [False]*(N+1)
def dfs(now,idx):
    group[idx].append(now)
    visit[now] = True
    for nxt in E[now]:
        if not visit[nxt]:
            dfs(nxt,idx)
idx = 0
for i in range(1,N+1):
    if not visit[i]:
        group[idx] = []
        dfs(i,idx)
        idx += 1
sums = [sum([C[group[g][i]-1] for i in range(len(group[g]))]) for g in range(idx)]
dp = [0]*(K)
nxt_dp = [0]*(K)
for g in range(idx):
    for k in range(K):
        nxt_dp[k] = max(dp[k],dp[k-len(group[g])]+sums[g]) if k >= len(group[g]) else dp[k]
    dp,nxt_dp = nxt_dp,dp
print(dp[-1])