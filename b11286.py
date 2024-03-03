from heapq import heappush, heappop
import sys
input = sys.stdin.readline
H = []
for _ in range(int(input())):
    N = int(input())
    if N==0:
        print(heappop(H)[1] if H else 0)
    else:
        heappush(H,(abs(N),N))
