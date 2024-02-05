N,M=map(int,input().split())
D = [[N]*N for _ in range(N)]
for _ in range(M):
    f,t=map(int,input().split())
    D[f-1][t-1] = 1
    D[t-1][f-1] = 1    
for i in range(N):
    D[i][i] = 0
# floyd-warshall
for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])
print(min([[sum(x),i] for i,x in enumerate(D)])[1]+1)
