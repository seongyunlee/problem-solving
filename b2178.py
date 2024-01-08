N,M=map(int,input().split())
A=[list(input()) for _ in range(N)]
bfs=[[0,0]]
cnt=1
dr=[-1,0,0,1]
dc=[0,1,-1,0]
while bfs:
    if [N-1,M-1] in bfs:
        break
    nb=[]
    for r,c in bfs:
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if 0<=nr<N and 0<=nc<M and A[nr][nc]=="1":
                nb.append([nr,nc])
                A[nr][nc]="2"
    bfs=nb
    cnt+=1
print(cnt)