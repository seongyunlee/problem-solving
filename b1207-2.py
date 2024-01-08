import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
G = [[0]*M for _ in range(N)]
def dfs(r,c,g):
    G[r][c]=g
    for dr,dc in [[-1,0],[0,-1],[0,1],[1,0]]:
        if not (0<=r+dr<N and 0<=c+dc<M):continue
        if G[r+dr][c+dc]!=0:continue
        if abs(A[r+dr][c+dc]-A[r][c])>K:continue
        dfs(r+dr,c+dc,g)
ans = 0
for r in range(N):
    for c in range(M):
        if G[r][c]==0:
            ans+=1
            dfs(r,c,r*M+c+1)
print(ans)
