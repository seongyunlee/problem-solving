import sys
input = sys.stdin.readline
C = [0]*10001
for _ in range(int(input())):
    C[int(input())]+=1
for i,c in enumerate(C):
    for _ in range(c):
        print(i)

