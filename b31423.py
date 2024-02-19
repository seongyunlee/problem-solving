import sys
input = sys.stdin.readline
K = int(input())
N = [input().strip() for _ in range(K)]
R = [None]*K
T = [i for i in range(K)]
V = [False]*K
for _ in range(K-1):
    a,b = map(int,input().split())
    R[T[a-1]] = b-1
    T[a-1] = T[b-1]
    V[b-1] = True
start = V.index(False)
A = ''
while start != None:
    print(N[start],end='')
    start = R[start]
print(A)
