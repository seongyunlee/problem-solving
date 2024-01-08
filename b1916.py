import heapq
file=open("input.txt").readlines()
n,m=map(int,file[:2])
E={i:[] for i in range(1,n+1)}
for l in file[2:-1]:
    s,e,t=map(int,l.split())
    E[s].append([e,t])
fr,to=map(int,file[-1].split())
hq=[[0,fr]]
cost=[1e9]*(n+1)
visit=[False]*(n+1)
while hq:
    c,v=heapq.heappop(hq)
    if visit[v]:continue
    visit[v]=True
    if v==to:
        print(c)
        break
    for nv,nc in E[v]:
        if cost[nv]>c+nc:
            cost[nv]=c+nc
            heapq.heappush(hq,[c+nc,nv])
 
