import sys
input = sys.stdin.readline
W,H,K,T = map(int, input().split())
V = [tuple(map(int, input().split())) for _ in range(K)]
A = 1
for x,y in V:
    top = max(1,y-T)
    bottom = min(H,y+T)
    left = max(1,x-T)
    right = min(W,x+T)
    dots = (bottom-top+1)*(right-left+1)
    A = A*dots%998244353
print(A)
