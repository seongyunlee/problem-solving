import heapq
file=open('input.txt').readlines()
N,E=map(int,file[0].split())
edge={i:[] for i in range(1,N+1)}
v1=int(file[1])
for l in file[2:]:
    f,t,c=map(int,l.split())
    edge[f].append([t,c])
cost=["INF"]*(N+1)
visit=[False]*(N+1)
cost[v1]=0
hq=[[0,v1]]
while hq:
    toFC,f=heapq.heappop(hq)
    if visit[f]:continue
    visit[f]=True
    cost[f]=toFC
    for t,c in edge[f]:
        if not visit[t]:heapq.heappush(hq,[toFC+c,t])
print(*cost[1:],sep="\n")