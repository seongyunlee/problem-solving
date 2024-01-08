import sys
input= sys.stdin.readline
N,M=map(int,input().split())
raw=[list(map(int,input().split())) for _ in range(N)]
T=int(input())
P=[]
for line in raw:
    p=[]
    for i in range(0,len(line),3):
        p.append(1 if sum(line[i:i+3])/3>=T else 0)
    P.append(p)
print(P)
def dfs(r,c):
    if P[r][c]==2:return
    P[r][c]=2
    for dr,dc in [[-1,0],[0,1],[0,-1],[1,0]]:
        if not (0<=r+dr<N and 0<=c+dc<M):continue
        if P[r+dr][c+dc]==1: dfs(r+dr,c+dc)
ans=0
for r in range(N):
    for c in range(M):
        if P[r][c]==1:
            ans+=1
            dfs(r,c)
print(ans)