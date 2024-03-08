N,K = map(int,input().split())
visit = [1000000]*100001
q = [(N,0)]
ans = 0
while q and ans == 0:
    nq = []
    for x,cnt in q:
        if x == K:
            if ans == 0:
                print(cnt)
            ans+=1
        if 0<=x-1<=100000 and visit[x-1] >= cnt:
            nq.append((x-1,cnt+1))
            visit[x-1] = cnt
        if 0<=x+1<=100000 and visit[x+1] >= cnt:
            nq.append((x+1,cnt+1))
            visit[x+1] = cnt
        if 0<=x*2<=100000 and visit[x*2] >= cnt:
            nq.append((x*2,cnt+1))
            visit[x*2] = cnt
    q = nq
print(ans)