from queue import heappop,heappush
N,K=map(int,input().split())
dp=[-1]*100001
V=[False]*100001
C=[(0,N)]
while C:
    cost,now=heappop(C)
    if K==now:
        print(cost)
        exit()
    if K<now:
        heappush(C,(cost+now-K,K))
        continue
    if V[now]:continue
    V[now]=True
    heappush(C,(cost+1,now+1))
    if now>0:heappush(C,(cost+1,now-1))
    heappush(C,(cost,now*2))
