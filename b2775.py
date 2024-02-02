import sys
input = sys.stdin.readline
A = [list(range(1,15))]
for _ in range(14):
    S = 0
    T = []
    for i in range(14):
        S += A[-1][i]
        T.append(S)
    A.append(T)
for _ in range(int(input())):
    K = int(input())
    N = int(input())
    print(A[K][N-1])
