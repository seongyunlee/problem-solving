import sys
input = sys.stdin.readline
for _ in range(int(input())):
    H,W,N = map(int,input().split())
    print(str((N-1)%H+1)+str((N-1)//H+1).zfill(2))