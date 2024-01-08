import sys
sys.setrecursionlimit(100001)
input=sys.stdin.readline
E={i:[] for i in range(1,int(input())+1)}
for _ in range(len(E)-1):
    f,t= map(int,input().split())
    E[f].append(t)
    E[t].append(f)
P=[-1]*len(E)
def dfs(idx,prev):
    for c in E[idx]:
        if c==prev:continue
        P[c-1]=idx
        dfs(c,idx)
dfs(1,-1)
print(*P[1:],sep="\n")