import sys
sys.setrecursionlimit(10**6)
from copy import deepcopy


input = sys.stdin.readline
N,M = map(int,input().split())
A = [list(input().strip()) for _ in range(N)]
orgA = deepcopy(A)

drdc = [(0,1),(0,-1),(1,0),(-1,0)]
group = {}

def dfs(r,c,i):
    A[r][c] = i
    group[i] += 1
    for dr,dc in drdc:
        if not (0<=r+dr<N and 0<=c+dc<M): continue
        if A[r+dr][c+dc] == '1': continue
        if A[r+dr][c+dc] == i: continue
        dfs(r+dr,c+dc,i)
now = 0

for r in range(N):
    for c in range(M):
        if A[r][c] == '0':
            group[now] = 0
            dfs(r,c,now)
            now += 1
ansA = []
for r in range(N):
    for c in range(M):
        if orgA[r][c] == '0':
            ansA.append('0')
        else:
            T = {}
            for dr,dc in drdc:
                if not (0<=r+dr<N and 0<=c+dc<M) or A[r+dr][c+dc] == '1':
                    continue
                if not A[r+dr][c+dc] in T:
                    T[A[r+dr][c+dc]] = group[A[r+dr][c+dc]]
            ansA.append(str((sum(T.values())+1)%10))
    ansA.append('\n')
print(''.join(ansA))
            
    
