G=None
C=None
def dfs(i,g):
    if G[i]!=-1:return
    G[i]=g
    for j in range(len(G)):
        if C[i][j]==1 and G[i]==-1:dfs(j,g)
def solution(n, computers):
    global G,C
    G=[-1]*n
    C=computers
    idx=-1
    for i in n:
        if G[i]!=-1:
            idx+=1
            dfs(i,idx)
    return idx
solution(3	,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])