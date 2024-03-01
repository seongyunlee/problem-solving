import sys
input = sys.stdin.readline
def calc(N):
    return int("1"*(N-1))*11
for _ in range(int(input())):
    N = int(input())
    if N==1:
        print(0)
    else:
        print(calc(N))