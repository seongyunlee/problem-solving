import sys

sys.setrecursionlimit(100)
input = sys.stdin.readline
N = int(input())
E = [[None] * (N + 1) for _ in range(N + 1)]
for _ in range(int(input())):
    f, t, c = map(int, input().split())
    E[f][t] = min(E[f][t], c) if E[f][t] != None else c
for i in range(1, N + 1):
    for f in range(1, N + 1):
        for t in range(1, N + 1):
            if f == t:
                E[f][t] = 0
            elif E[f][i] is not None and E[i][t] is not None:
                E[f][t] = min(E[f][t], E[f][i] + E[i][t]) if E[f][t] != None else E[f][i] + E[i][t]

for i in E[1:]:
    print(*[k if k != None else 0 for k in i[1:]])
