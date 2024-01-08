file=open('input.txt')
for _ in range(int(next(file))):
    n,m,w=map(int,next(file).split())
    E=[]
    for i in range(m):
        s,e,t=map(int,next(file).split())
        E.append([s,e,t])
        E.append([e,s,t])
    for i in range(w):
        s,e,t=map(int,next(file).split())
        E.append([e,s,-t])
    find=False
    visit=[False]*(n+1)
    for v in range(1,n+1):
        if visit[v]:continue
        visit[v]=True
        if find:break
        cost=[None]*(n+1)
        cost[v]=0
        for i in range(1,n+1):
            for fr,to,C in E:
                if None!=cost[fr] and ( None==cost[to] or cost[to]>cost[fr]+C):
                    cost[to]=cost[fr]+C
                    visit[to]=True
                    if i==n:
                        find=True
    if find:
        print("YES")
    else:print("NO")