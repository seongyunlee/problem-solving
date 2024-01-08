N,M=map(int,input().split())
r,c,d=map(int,input().split())
gap=[[0,-1],[-1,0],[0,1],[1,0]]
visit=[]
for _ in range(N):
    visit.append(list(map(int,input().split())))
finish=False
cnt=0
while not finish:
    if visit[r][c]==0:
        cnt+=1
        visit[r][c]=3
    for i in range(4):
        lr=r+gap[d][0]
        lc=c+gap[d][1]
        d=(d-1) if d>0 else 3
        if visit[lr][lc]==0:
            r,c=lr,lc
            break
        if i==3:
            if d==0:
                br=r+1
                bc=c
            if d==1:
                br=r
                bc=c-1
            if d==2:
                br=r-1
                bc=c
            if d==3:
                br=r
                bc=c+1
            if visit[br][bc]==1:
                finish=True
            else: 
                r=br
                c=bc
print(cnt)