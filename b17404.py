import sys
input = sys.stdin.readline
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
ans = 1001*1001
for i in range(3):
    # R, G, B for first house
    dp = [1001*1001]*3
    dp[i] = A[0][i]
    for r,g,b in A[1:]:
        # R, G, B for current house
        dp = [r+min(dp[1],dp[2]),g+min(dp[0],dp[2]),b+min(dp[0],dp[1])]
    ans = min([ans]+[dp[x] for x in range(3) if not x == i])
print(ans)