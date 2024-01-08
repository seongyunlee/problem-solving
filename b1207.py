import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = {} # True if it's marked
XY = [list(map(int,input().split())) for _ in range(N)]
P = list(map(int,input().split()))
R = list(map(int,input().split()))
isMarked = [False]*N
squareDis = lambda x,y: (x[0]-y[0])**2+(x[1]-y[1])**2
for p in range(M):
    isMarked[P[p]-1] = True
    for idx in range(N):
        if squareDis(XY[idx],XY[P[p]-1])<=R[p+1]**2:
            isMarked[idx] = True
now = set([i for i in range(N) if not isMarked[i]])
dirty = set([i for i in range(N) if isMarked[i]])
ans = 0
while True:
    nextNow = set()
    for idx in now:
        ans +=1
        clean = set()
        for p in dirty:
            if squareDis(XY[idx],XY[p])<=R[0]**2:
                nextNow.add(p)
                clean.add(p)
        for c in clean:
            dirty.remove(c)
    if len(nextNow)==0:
        break
    now = nextNow
print(ans)
    