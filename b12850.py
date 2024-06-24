from copy import deepcopy
G = [[1,2],[0,2,3],[0,1,3,4],[1,2,4,7],[2,3,5,7],[4,6],[5,7],[3,4,6]]
N = [[0]*8 for _ in range(8)]
def calcNext(N):
    nextN = [[0]*8 for _ in range(8)]
    for i in range(8):
        for x in range(8):
            for y in range(8):
                nextN[x][y] += N[x][i]*N[i][y]%1000000007
    return nextN
for i in range(8):
    for j in G[i]:
        N[i][j] = 1
I = int(input())
T = I
bins = {}
while T != 0:
    lowest = T&-T
    bins[lowest] = None
    T -= lowest
maxBins = max(bins.keys())
bins[1] = deepcopy(N)
i = 2
while i <= maxBins:
    N = calcNext(N)
    if i in bins:
        bins[i] = deepcopy(N)
    i <<= 1
if not 1&I: del bins[1]
ans = bins[maxBins]
del bins[maxBins]
for k,v in bins.items():
    nextAns = [[0]*8 for _ in range(8)]
    if not v: continue
    for i in range(8):
        for x in range(8):
            for y in range(8):
                nextAns[x][y] += ans[x][i]*v[i][y]%1000000007
    ans = nextAns
print(ans[0][0]%1000000007)


    
