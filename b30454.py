import sys
input = sys.stdin.readline
L = [len([x for x in input().strip().split('0') if x!=""]) for _ in range(int(input().split()[0]))]
print(max(L),L.count(max(L)))