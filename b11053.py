input()
N=list(map(int,input().split()))
dp=[1]*len(N)
for i in range(len(N)-1,-1,-1):
    for j in range(i,len(N)):
        if N[i]<N[j]:
            dp[i]=max(dp[j]+1,dp[i])
print(max(dp))
