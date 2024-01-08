import sys
sys.setrecursionlimit(10**6)
pos=None
dxdy=[[-1,0],[1,0],[0,1],[0,-1]]
def adj(x,y):
    for dx,dy in dxdy:
        if 0<=x+dx<len(pos) and 0<=y+dy<len(pos[0]):
            if pos[x+dx][y+dy]==1:
                pos[x+dx][y+dy]=2
                adj(x+dx,y+dy)
for _ in range(int(input())):
    M,N,K=map(int,input().split())
    pos=[[-1]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        pos[y][x]=1
    cnt=0
    for row in range(N):
        for col in range(M):
            if pos[row][col]==1:
                adj(row,col)
                cnt+=1
    print(cnt)

