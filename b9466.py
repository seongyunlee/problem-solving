import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    L = [0]+list(map(int,input().split()))
    visited = [False]*(n+1)
    s = 0
    order = [[None,None]]*(n+1)
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = True
        root = i
        order[i] = [root,1]
        while True:
            if order[L[i]][0] == None and not visited[L[i]]:
                order[L[i]] = [root,order[i][1] + 1]
                i = L[i]
                visited[i] = True
            elif order[L[i]][0] == root:
                s += order[i][1] - order[L[i]][1] + 1
                break
            else: break
    return n-s
for _ in range(int(input())):
    print(solve())