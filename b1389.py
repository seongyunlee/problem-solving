N,M=map(int,input().split())
e={}
for _ in range(M):
    f,t=map(int,input().split())
    if e.get(f):e[f].append(t)
    else: e[f]=[t]
    if e.get(t):e[t].append(f)
    else: e[t]=[f]
s=[]
for i in range(1,N):
    dis=[N+2]*(N+1)
    dis[i]=0
    node=[i]
    d=1
    while node:
        next_node=[]
        for now in node:
            for f in e[now]:
                if dis[f]>d:
                    dis[f]=d
                    next_node.append(f)
        d+=1
        node=next_node
    s.append([sum(dis[1:]),i])
print(min(s)[1])
