input()
N = list(map(int,input().split()))
def find(N):
    dp = [1]*len(N)
    for i in range(len(N)):
        for j in range(i):
            if N[i] > N[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return dp
left = find(N)
right = find(N[::-1])[::-1]
print(max(left[i]+right[i]-1 for i in range(len(N))))