import sys
input=sys.stdin.readline
N,K=map(int,input().split())
I=[list(map(int,input().split())) for _ in range(N)]
dp=[[-1]*(K+1) for _ in range(N)]
def getDp(idx,r):
    global dp
    if dp[idx][r]!=-1:return dp[idx][r]
    if idx==(N-1):
        if r>=I[idx][0]:return I[idx][1]
        else: return 0
    if r>=I[idx][0]:dp[idx][r]=max(getDp(idx+1,r-I[idx][0])+I[idx][1],getDp(idx+1,r))
    else:dp[idx][r]=getDp(idx+1,r)
    return dp[idx][r]
print(getDp(0,K)) 
