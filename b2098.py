N=int(input())
C=[list(map(int,input().split())) for _ in range(N)]
dp=[[-1]*(2**(N)) for _ in range(N)]
def getDp(idx,mask):
    if dp[idx][mask]!=-1:return dp[idx][mask]
    if mask==(2**(N)-1):dp[idx][mask]= C[idx][0] if C[idx][0]!=0 else 16000001
    else:
        P=[getDp(x,mask|(2**x))+C[idx][x] for x in range(N) if x!=idx and C[idx][x]!=0 and mask&(2**x)==0]
        dp[idx][mask]=min(P) if P else 16000001
    return dp[idx][mask]
print(getDp(0,1))