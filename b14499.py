N,M,x,y,K = map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
D=[0,0,[0,0,0,0]] # L,R,[F,U,B,D]
drdc = [[0,1],[0,-1],[-1,0],[1,0]]
for i in list(map(int,input().split())):
    dr,dc = drdc[i-1]
    if not (0<=x+dr<N and 0<=y+dc<M):continue
    x,y=x+dr,y+dc
    if i==3:
        print(D[2][3])
        D[2]=[D[2][3]]+D[2][:3]
    elif i==4:
        print(D[2][1])
        D[2]=D[2][1:]+[D[2][0]]
    elif i==1:
        print(D[0])
        D=[D[2][2],D[2][0],[D[0],D[2][1],D[1],D[2][3]]]
    elif i==2:
        print(D[1])
        D=[D[2][0],D[2][2],[D[1],D[2][1],D[0],D[2][3]]]
    if A[x][y]==0:
        A[x][y]=D[2][2]
    else:
        D[2][2]=A[x][y]
        A[x][y]=0

