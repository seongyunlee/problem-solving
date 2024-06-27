import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
P = [tuple(map(int,input().split())) for _ in range(N)]
x,y,z = 0,1,2
prev,next = 0,1
class Node:
    def __init__(self, v):
        self.val = v
        self.neighbor = [[None,None],[None,None],[None,None]]
        self.visit = False
    def __lt__(self, other):
        return True
    def remove(self):
        self.visit = True
        for axis in range(3):
            if self.neighbor[axis][prev]:
                self.neighbor[axis][prev].neighbor[axis][next] = self.neighbor[axis][next]
            if self.neighbor[axis][next]:
                self.neighbor[axis][next].neighbor[axis][prev] = self.neighbor[axis][prev]
    def __str__(self) -> str:
        return str(self.val)


nodes = [Node(p) for p in P]


P_sx = sorted(nodes,key=lambda a:a.val[x])
P_sy = sorted(nodes,key=lambda a:a.val[y])
P_sz = sorted(nodes,key=lambda a:a.val[z])

P_x = {v:i for i,v in enumerate(P_sx)}
P_y = {v:i for i,v in enumerate(P_sy)}
P_z = {v:i for i,v in enumerate(P_sz)}

P_dict = [P_x,P_y,P_z]
P_sort = [P_sx,P_sy,P_sz]


for n in nodes:
    for axis in range(3):
        if P_dict[axis][n] != 0:
            n.neighbor[axis][prev] = P_sort[axis][P_dict[axis][n]-1]
        if P_dict[axis][n] != N-1:
            n.neighbor[axis][next] = P_sort[axis][P_dict[axis][n]+1]


def calc_cost(node1,node2):
    return min([abs(node1.val[x]-node2.val[x]),abs(node1.val[y]-node2.val[y]),abs(node1.val[z]-node2.val[z])])
ans = 0
PQ = [[0,nodes[0]]]
while PQ:
    cost,now = heappop(PQ)
    if now.visit:
        continue
    ans += cost
    now.remove()
    for axis in range(3):
        if n:=now.neighbor[axis][prev]:
            heappush(PQ,(calc_cost(n,now),n))
        if n:=now.neighbor[axis][next]:
            heappush(PQ,(calc_cost(n,now),n))
print(ans)
        