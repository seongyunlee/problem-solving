import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = [list(input().strip()) for _ in range(N)]
dir = {'L':[0,-1],'R':[0,1],'U':[-1,0],'D':[1,0]}
def dfs(r,c,i):
    if type(A[r][c]) == int:
        if A[r][c] == -1:
            return i
        return A[r][c]
    dr,dc = dir[A[r][c]]
    A[r][c] = -1
    A[r][c] = dfs(r+dr,c+dc,i)
    return A[r][c]
ans = 0
for r in range(N):
    for c in range(M):
        if not type(A[r][c]) == int:
            ans += (dfs(r,c,ans) == ans)
print(ans)
