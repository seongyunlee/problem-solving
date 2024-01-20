import sys
input = sys.stdin.readline
print(*[sum(x) for x in [map(int,input().split()) for _ in range(int(input()))]],sep="\n")