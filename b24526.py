import sys
sys.setrecursionlimit(100001)
input=sys.stdin.readline
N,M=map(int,input().split())
E={i:[] for i in range(1,N+1)}
for _ in range(M):
    f,t=map(int,input().split())
    E[f].append(t)
dp=[None]*(N+1)
def hasCycle(idx,route):
    if dp[idx]!=None:return dp[idx]
    route.add(idx)
    for t in E[idx]:
        if t in route:
            dp[idx]=True
            return True
        dp[idx]=hasCycle(t,route)
        if dp[idx]==True:
            return True
    dp[idx]=False
    route.remove(idx)
    return False
cycle=[hasCycle(i,set()) for i in range(1,N+1)]
print(cycle.count(False))