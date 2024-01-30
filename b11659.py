import sys
input = sys.stdin.readline
N,M = map(int,input().split())
L = list(map(int,input().split()))
A = [0]
for i in range(N):
    A.append(A[i]+L[i])
print(*[A[y]-A[x-1] for x,y in [map(int,input().split()) for _ in range(M)]],sep="\n")