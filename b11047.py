import sys
input = sys.stdin.readline
N,K = map(int,input().split())
A = [int(input()) for _ in range(N)][::-1]
ans = 0
for a in A:
    ans += K//a
    K %= a
print(ans)
