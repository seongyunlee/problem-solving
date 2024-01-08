import sys
input = sys.stdin.readline
N,D = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
M = []
A = []
for a,x in X:
    if a==1:
        M.append(x)
    else:A.append(x)
Na = len(A)
A.sort(reverse=True)
M.sort()
ans = 0
for m in M:
    while D<=m:
        if len(A)==0:
            print(ans+Na)
            exit()
        a = A.pop()
        D *= a
    ans += 1
    D += m
print(ans+Na)