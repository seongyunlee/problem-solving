A = [list(map(int, list(input()))) for _ in range(int(input()))]
visit = [[False]*len(A) for _ in range(len(A))]
def dfs(x, y):
    visit[x][y] = True
    C = 1
    for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        nx, ny = x+dx, y+dy
        if not (0<=nx<len(A) and 0<=ny<len(A)):continue
        if visit[nx][ny]:continue
        if A[nx][ny] == 0:continue
        C += dfs(nx, ny)
    return C
T = sorted([dfs(i,j) for i in range(len(A)) for j in range(len(A)) if A[i][j]==1 and not visit[i][j]])
print(len(T))
print(*T, sep='\n')
    