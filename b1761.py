import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)
N = int(input())
E = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    f,t,c = map(int,input().split())
    E[f].append([t,c])
    E[t].append([f,c])
P = [{} for i in range(1,N+1)]
L = [0]*(N+1)
P = [None]*(N+1)
P[1] = [-1,0]
def dfs(prev,idx,level):
    L[idx]=level
    P[idx][0] = prev
    up = 1
    while True:
        if P[P[idx][i-1]]
        P[idx][up]
    for ch,co in E[idx]:
        if prev == ch : continue
        P[ch] = [idx,co]
        dfs(idx,ch,level+1)
dfs(-1,1,0)
A = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    ans = 0
    while L[a]!=L[b]:
        if L[a]<L[b]:
            ans += P[b][1]
            b = P[b][0]
        else:
            ans += P[a][1]
            a = P[a][0]
    while a!=b:
        ans += P[b][1]
        ans += P[a][1]
        a = P[a][0]
        b = P[b][0]
    A.append(str(ans))
print('\n'.join(A))