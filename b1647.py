import sys
input= sys.stdin.readline
N,M=map(int,input().split())
E=[list(map(int,input().split()))[::-1] for _ in range(M)]
E.sort()
P=[i for i in range(N+1)]
S=0
answer=0
def findRoot(idx):
    if idx==P[idx]:return idx
    else: return findRoot(P[idx])
for c,f,t in E:
    fR=findRoot(f)
    tR=findRoot(t)
    if tR==fR:continue
    S+=1
    answer+=c
    if fR<tR:
        P[tR]=P[t]=P[f]=fR
    elif fR>tR:
        P[fR]=P[t]=P[f]=tR
    if S==N-2:
        break
print(answer)