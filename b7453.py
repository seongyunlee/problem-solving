from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
N = [[] for _ in range(4)]
for _ in range(int(input())):
    for idx, n in enumerate(map(int, input().split())):
        N[idx].append(n)
K = [a+b for a in N[0] for b in N[1]]
T = [c+d for c in N[2] for d in N[3]]
K.sort()
T.sort()
ans = 0
kIdx, tIdx = 0, len(T)-1
while kIdx < len(K) and tIdx >= 0:
    if K[kIdx] + T[tIdx] == 0:
        kCnt = tCnt = 0
        orgK = K[kIdx]
        orgT = T[tIdx]
        while kIdx < len(K) and K[kIdx] == orgK:
            kIdx += 1
            kCnt += 1
        while tIdx >= 0 and T[tIdx] == orgT:
            tIdx -= 1
            tCnt += 1
        ans += (kCnt)*(tCnt)
    elif K[kIdx] + T[tIdx] > 0:
        tIdx -= 1
    else:
        kIdx += 1
print(ans)
    