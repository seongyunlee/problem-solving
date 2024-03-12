import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
V = []
S = 1
while S < G:
    S *= 2
depth = 1
size = S
while depth <= S:
    V.append([size]*depth)
    size //= 2
    depth *= 2
def minus(idx):
    for i in range(len(V)-1,-1,-1):
        V[i][idx] -= 1
        idx //= 2
for i in range(G,S):
    minus(i)
def find(idx):
    now = idx
    isLeft = False
    prev = 0
    for depth in range(len(V)-1,-1,-1):
        if not isLeft and  V[depth][now]-prev > 0:
            break
        prev = V[depth][now]
        isLeft = (now % 2 == 0)
        now //= 2
    if isLeft and depth==0:
        return -1
    if not isLeft and depth!=len(V)-1:
        now = now*2
        depth += 1
    if V[depth][now] == 0:
        return -1
    for i in range(depth, len(V)-1):
        if V[i+1][now*2+1] > 0:
            now = now*2+1
        else:
            now = now*2
    minus(now)
    return now
KK = [int(input()) for _ in range(P)]
gate = [None]*G
for i,v in enumerate(KK):
    k = find(v-1)
    if k == -1:
        print(i)
        break
    gate[k] = i
    if i==P-1:
        print(P)

'''
20
20
15
14
13
12
11
10
9
15
15
15
15
15
15
6
1
16
17
15
15
15
'''