import heapq
file=open('input.txt')
f,*lines=file.readlines()
v,e=map(int,f.split())
edges={i:[] for i in range(1,v+1)}
for l in lines:
    s,f,c=map(int,l.split())
    edges[s].append([f,c])
    edges[f].append([s,c])
adj=[]
visit=[False]*(v+1)
visit[1]=True
for v,c in edges[1]:
    heapq.heappush(adj,[c,v])
total=0
while adj:
    c,v=heapq.heappop(adj)
    if visit[v]:continue
    visit[v]=True
    total+=c
    if all(visit[1:]):
        break
    for v,c in edges[v]:
        heapq.heappush(adj,[c,v])
print(total)