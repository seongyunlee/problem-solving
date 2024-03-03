import sys
input = sys.stdin.readline
N,M = map(int,input().split())
I = None
A = [input() for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j] == 'I':
            I = (i,j)
            break
    if I: break
P = [I]
visit = [[False]*M for _ in range(N)]
visit[I[0]][I[1]] = True
cnt = 0
while P:
    nP = []
    for i,j in P:
        for ni,nj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
            if not (0<=ni<N and 0<=nj<M): continue
            if A[ni][nj] == 'X': continue
            if visit[ni][nj]: continue
            if A[ni][nj] == 'P':
                cnt+=1
            visit[ni][nj] = True
            nP.append((ni,nj))
    P = nP
print(cnt if cnt else 'TT')