from itertools import combinations
N,M = map(int,input().split())
A = sorted(set(map(int,input().split())))
N = len(A)
def make(L):
    if len(L)==M:
        return [L]
    A = []
    for i in range(L[-1],N+1):
        A += make(L+[i])
    return A
T = []
for i in range(1,N+1):
    T += make([i])
for t in T:
    print(*[A[i-1] for i in t])