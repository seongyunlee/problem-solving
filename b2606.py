N=int(input())
E={i:[False]*(N+1) for i in range(1,N+1)}
for _ in range(int(input())):
    f,t=map(int,input().split())
    E[f][t]=True
    E[t][f]=True
bfs=[1]
visit=[False]*(len(E)+1)
visit[1]=True
while bfs:
    nb=[]
    for b in bfs:
        for i,n in enumerate(E[b]):
            if n and not visit[i]:
                nb.append(i)
                visit[i]=True
    bfs=nb
print(visit.count(True)-1)
