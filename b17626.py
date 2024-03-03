N = int(input())
minP = 0
dp = [0] + [-1]*N
P = set([i**2 for i in range(0,int(N**.5)+2)])
def getMin(n,dep):
    if dp[n]!=-1:
        return dp[n]
    if dep==1:
        return 1 if n in P else 4
    if n in P: return 1
    k = 0
    a = 4
    while k**2<=n:
        a = min(a,1+getMin(n-k**2,dep-1))
        k += 1
    dp[n] = a
    return a
print(getMin(N,4))