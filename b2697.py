N,M=map(int,input().split())
bfs=[N]
visit=[False]*(10**10)
if N==M:bfs=[]
cnt=0
while bfs:
    nb=[]
    for b in bfs:
        x,y,z=b*2,b+1,b-1
        if M in [x,y,z]:
            nb=[]
            break
        else:
            if not visit[x]:
                visit[x]=True
                nb.append(x)
            if not visit[y]:
                visit[y]=True
                nb.append(y)
            if z>-1 and not visit[z]:
                visit[z]=True
                nb.append(z)
    nb.sort(reverse=True)
    bfs=nb
    cnt+=1
print(cnt)