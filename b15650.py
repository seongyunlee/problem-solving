import itertools
N,M=map(int,input().split())
for k in itertools.permutations(sorted(list(map(int,input().split()))),M):
    print(*k)