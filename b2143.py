T= int(input())
N = int(input())
A= list(map(int,input().split()))
M= int(input())
B= list(map(int,input().split()))
subA = [0]
subB= [0]
for i in A:
    subA.append(subA[-1]+i)
for i in B:
    subB.append(subB[-1]+i)
cntB = {}
for f in range(M):
    for t in range(f+1,M+1):
        fTot = subB[t]-subB[f]
        if fTot in cntB: cntB[fTot]+=1
        else: cntB[fTot] = 1
ans = 0
for f in range(N):
    for t in range(f+1,N+1):
        fTot = subA[t]-subA[f]
        if T-fTot in cntB:
            ans += cntB[T-fTot]
print(ans)