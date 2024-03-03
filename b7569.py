import sys
input = sys.stdin.readline
M,N,H = map(int,input().split())
A = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
R = []
cnt = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if A[z][y][x]==1:
                R.append((z,y,x))
            elif A[z][y][x]==0:
                cnt += 1     
day = 0
if cnt==0:
    print(0)
    exit()
while R:
    day+=1
    nR = []
    for z,y,x in R:
        for dz,dy,dx in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
            Z,Y,X = z+dz,y+dy,x+dx
            if not (0<=Z<H and 0<=Y<N and 0<=X<M and A[Z][Y][X]==0):continue
            if A[Z][Y][X]==1 or A[Z][Y][X]==-1:continue
            A[Z][Y][X]=1
            nR.append((Z,Y,X))
            cnt -=1
    if cnt==0:
        print(day)
        exit()
    R = nR
print(-1)

