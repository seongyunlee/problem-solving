import sys
input = sys.stdin.readline
M = [list(map(int, input().split())) for _ in range(int(input()))]
dp = [[None]*len(M) for _ in range(len(M))]
def calc(i,j):
    if i==j:
        return 0
    if i+1==j:
        return M[i][0]*M[i][1]*M[j][1]
    if dp[i][j] is not None:
        return dp[i][j]
    dp[i][j] = int(2e31)
    for k in range(i,j):
        dp[i][j] = min(dp[i][j],calc(i,k)+calc(k+1,j)+M[i][0]*M[k][1]*M[j][1])
    return dp[i][j]
print(calc(0,len(M)-1))