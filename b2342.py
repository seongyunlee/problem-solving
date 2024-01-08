import sys
sys.setrecursionlimit(10**6)
L=list(map(int,input().split()))[:-1]
dp = [[[None]*5 for _ in range(5)] for _ in range(len(L))]
def cost(now,nxt):
    if now == 0: return 2
    if abs(now-nxt) == 2:return 4
    else : return 3
def move(nowL,nowR,tar):
    if tar in [nowL,nowR]:
        return [[nowL,nowR,1]]
    return [[tar,nowR,cost(nowL,tar)],[nowL,tar,cost(nowR,tar)]]
def getDP(left,right,idx):
    if idx==len(dp)-1:
        return min([x[2] for x in move(left,right,L[idx])])
    if dp[idx][left][right] !=None: return dp[idx][left][right]
    dp[idx][left][right]= min([getDP(x,y,idx+1)+z for x,y,z in move(left,right,L[idx])])
    return dp[idx][left][right]
print(getDP(0,0,0))