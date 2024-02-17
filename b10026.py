import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())
M = [input() for _ in range(N)]
def dfsA(x,y,visit,color):
    if visit[x][y]: return 0
    visit[x][y] = True
    for dx,dy in (0,1),(1,0),(-1,0),(0,-1):
        nx,ny = x+dx,y+dy
        if not (0<=nx<N and 0<=ny<N) or visit[nx][ny]:
            continue
        if M[nx][ny] in color:
            dfsA(nx,ny,visit,color)
    return 1
visit = [[False]*N for _ in range(N)]
print(sum(dfsA(i,j,visit,M[i][j]) for i in range(N) for j in range(N)),end=' ')
visit = [[False]*N for _ in range(N)]
print(sum(dfsA(i,j,visit,"B" if M[i][j]=="B" else "RG") for i in range(N) for j in range(N)))
