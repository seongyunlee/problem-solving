F,*L=open(0).readlines()
M,N=map(int,F.split())
B=[list(map(int,x.split())) for x in L]
answer=0
didj=[[1,0],[-1,0],[0,1],[0,-1]]
r=[]
for i in range(N):
    for j in range(M):
        if B[i][j]==1:
            r.append([i,j])
while True:
    nr=[]
    if r==[]:break
    for i,j in r:
        for di,dj in didj:
            if 0<=i+di<N and 0<=j+dj<M and B[i+di][j+dj]==0:
                nr.append((i+di,j+dj))
    for a,b in nr:
        B[a][b]=1
    r=nr
    if r:answer+=1
for line in B:
    for l in line:
        if l==0:
            answer=-1
print(answer)
