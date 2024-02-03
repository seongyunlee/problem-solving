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
print(S)
for idx, H in enumerate(L):
    small = H*idx - S[idx]
    big = S[-1]-S[idx+1] - H*(N-idx-1)
    time = small+ big*2
    if B + big - small >= 0:
        if time < A[0]:
            A[0] = time
            A[1] = H
    print(idx, H, small,big,time)
print(*A)            
