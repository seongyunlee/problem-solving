import sys
input = sys.stdin.readline
def calc(X,Y,x,y):
    ans = 0
    visit = [[False]*X for _ in range(Y)]
    for r in range(Y):
        for c in range(X):
            if visit[r][c]: continue
            ans += 1
            if 0<=c+x<X and 0<=r+y<Y:
                visit[r+y][c+x] = True
    return ans
for _ in range(int(input())):
    X,Y,x,y = map(int,input().split())
    print(calc(X,Y,x,y))