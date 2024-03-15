import sys
input = sys.stdin.readline
XYZ = [list(map(int,input().split())) for _ in range(int(input()))]
def dis(A,B):
    x1,y1,z1 = A
    x2,y2,z2 = B
    return min([abs(x1-x2),abs(y1-y2),abs(z1-z2)])