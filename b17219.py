import sys
input = sys.stdin.readline
N,M = map(int,input().split())
D = {}
for i in range(N):
    a,b = input().split()
    D[a] = b
print(*[D[input().strip()] for _ in range(M)], sep='\n')