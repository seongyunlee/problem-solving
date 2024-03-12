import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]
start = [(0,i) for i in range(N)] + [(i,0) for i in range(1,N)]
def fill(how,idx,isFill):
    if idx == 2*N-1:
        return True
    if how[idx]==0:
        return fill(how,idx+1,isFill)
    r,c = start[idx]
    while r<N and c<N:
        if M[r][c]==1 and not r+c in isFill:
            nn = fill(how,idx+1,isFill|{r+c})
            if nn: return nn
        r += 1
        c += 1
    return False
for i in range(2*N-2,0,-1):
    for pick in combinations(range(0,2*N-1),i):
        how = [0]*(2*N-1)
        for p in pick:
            how[p] = 1
        if fill(how,0,set()):
            print(i)
            exit()
print(0)