from sys import setrecursionlimit
setrecursionlimit(10**5)
C=[list(map(int,input().split())) for _ in range(int(input()))]
dp=[[1000*1000]*3 for _ in range(len(C))]
dp[-1]=C[-1]
def minC(N,color):
    if N==len(C)-1:
        return dp[N][color]
    if dp[N][color]!= 1000*1000:return dp[N][color]
    dp[N][color]=C[N][color]+min([minC(N+1,cc) for cc in range(3) if not cc==color])
    return dp[N][color]
print(min([minC(0,cc) for cc in range(3)]))