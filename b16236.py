import sys
input = sys.stdin.readline
N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]
cnt = {i:[] for i in range(1,7)}
S = [-1,-1]
for r in range(N):
    for c in range(N):
        if M[r][c] == 9:
            S = [r,c]
            M[r][c] = 0
        elif M[r][c] > 0:
            cnt[M[r][c]].append((r,c))
size = 2
eat = cnt[1]
ans = 0
def move(fx,fy,tx,ty):
    visit = [[0]*N for _ in range(N)]
    q = [(fx,fy,0)]
    visit[fx][fy] = 1
    while q:
        nq = []
        for x,y,cnt in q:
            if x == tx and y == ty:
                return cnt
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                nx,ny = x+dx,y+dy
                if 0<=nx<N and 0<=ny<N and not visit[nx][ny] and M[nx][ny] <= size:
                    visit[nx][ny] = 1
                    nq.append((nx,ny,cnt+1))
        q = nq
    return N*N+1
acc = 0
while True:
    if not eat:
        break
    eat.sort(key=lambda x:(-move(S[0],S[1],x[0],x[1]),-x[0],-x[1]))
    r,c = eat.pop()
    if move(S[0],S[1],r,c) == N*N+1:
        break
    acc += 1
    ans += move(S[0],S[1],r,c)
    if acc == size and size < 7:
        eat += cnt[size]
        acc = 0
        size += 1
    S = [r,c]
print(ans)

        