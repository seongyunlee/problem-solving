import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
dp = {}
def calc(A,B):
    R = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                R[i][j] += A[i][k]*B[k][j]
            R[i][j] %= 1000
    return R
def mult(p):
    if dp.get(p) != None:
        return dp[p]
    if p == 1:
        return [[i%1000 for i in j] for j in A]
    H = mult(p//2)
    dp[p] = calc(H,H)
    if p%2 == 1:
        dp[p] = calc(A,dp[p])
    return dp[p]
print('\n'.join(' '.join(map(str,i)) for i in mult(B)))