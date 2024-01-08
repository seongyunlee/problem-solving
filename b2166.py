import sys
input = sys.stdin.readline
P = [list(map(int,input().split())) for _ in range(int(input()))]
def deter(a,b):
    return a[0]*b[1]-a[1]*b[0]
P.append(P[0])
print(round(0.5*abs(sum([deter(P[idx],P[idx+1]) for idx in range(len(P)-1)])),1))
