import sys
N=int(input())
K=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[-1]*(N-1)+[K[-1][1] if K[-1][0]==1 else 0]
for i in range(len(K)-2,-1,-1):
    dp[i]=max((K[i][1] if K[i][0]+i<=N else 0)+(dp[i+K[i][0]] if i+K[i][0]<len(K) else 0),dp[i+1])
print(dp[0])