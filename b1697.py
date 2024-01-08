M,N=map(int,input().split())
dp=[None]*200001
bfs=[N]
t=0
while bfs:
    nb=[]
    for b in bfs:
        if not dp[b]: dp[b]=t
        if b==M:
            nb.clear()
            break
        if b%2==0 and not dp[b//2]:nb.append(b//2)
        if b>0 and not dp[b-1]: nb.append(b-1)
        if not dp[b+1]: nb.append(b+1)
    bfs=nb
    t+=1
print(dp[M])