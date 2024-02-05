import sys
input = sys.stdin.readline
N,M,B = map(int,input().split())
L = []
for _ in range(N):
    L.extend(map(int,input().split()))
L.sort()
A = [50000000,0]
S = [0]
# sum of L from x to y = S[y+1]-S[x]
for l in L:
    S.append(S[-1]+l)
N = N*M
idx = len(L)-1
for H in range(L[-1],-1,-1):
    while L[idx]>H and idx>0:
        idx -= 1
    small = H*(idx+1) - S[idx+1]
    big = S[-1]-S[idx+1] - H*(N-idx-1)
    time = small+ big*2
    print(H,idx,small,big,time)
    if B + big - small >= 0:
        if time < A[0]:
            A[0] = time
            A[1] = H
print(*A)            
