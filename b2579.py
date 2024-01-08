S=[int(input()) for _ in range(int(input()))]
dp=[[-1,-1] for _ in range(len(S))]
dp[-1]=[S[-1],S[-1]]
def dfs(N,C):
    if N!=-1 and not dp[N][C]==-1:
        return dp[N][C]
    p=[]
    if C<1 and N+1<len(S) and (r:=dfs(N+1,C+1))>=0:p.append(r)
    if N+2<len(S) and (r:=dfs(N+2,0))>=0:p.append(r)
    if p:dp[N][C]=max(p)+(S[N] if N!=-1 else 0)
    else:p=-2
    return dp[N][C]
print(dfs(-1,-1))