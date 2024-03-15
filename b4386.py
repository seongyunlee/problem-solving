import sys
from heapq import heappush, heappop
input = sys.stdin.readline
XY = [list(map(float,input().split())) for _ in range(int(input()))]
def dist(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x1-x2)**2)+((y1-y2)**2)
D = [[dist(a,b) for a in XY] for b in XY]
A = 0
H = [[0,0]]
visit = [False]*len(XY)
while H:
    cost,node = heappop(H)
    if visit[node]:continue
    visit[node] = True
    A += cost**(0.5)
    for i in range(len(XY)):
        heappush(H,(D[i][node],i))
print(A)