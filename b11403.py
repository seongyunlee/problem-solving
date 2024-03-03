import sys
input = sys.stdin.readline
N = int(input())
ADJ = [list(map(int,input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if ADJ[i][k] and ADJ[k][j]:
                ADJ[i][j] = 1
for i in range(N):
    print(*ADJ[i])