import heapq
file=open('input.txt').readlines()
N,E=map(int,file[0].split())
edge={i:[] for i in range(1,N+1)}
for l in file[1:-1]:
    f,t,c=map(int,l.split())
    edge[f].append([t,c])
    edge[t].append([f,c])
v1,v2=map(int,file[-1].split())
def calcDis(fr,to):
    cost=[999999999999999]*(N+1)
    visit=[False]*(N+1)
    cost[fr]=0
    hq=[[0,fr]]
    while hq:
        toFC,f=heapq.heappop(hq)
        if visit[f]:continue
        if f==to:
            return (toFC)
        visit[f]=True
        for t,c in edge[f]:
            if not visit[t]:heapq.heappush(hq,[toFC+c,t])
v1First= -1 if None in (K:=[calcDis(1,v1),calcDis(v1,v2),calcDis(v2,N)]) else sum(K)
v2First= -1 if None in (K:=[calcDis(1,v2),calcDis(v2,v1),calcDis(v1,N)]) else sum(K)
if v1First==-1 and v2First==-1: print(-1)
else:print(min([v1First,v2First]))