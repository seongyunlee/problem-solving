from itertools import combinations
N,M = map(int,input().split())
L = list(map(int,input().split()))
print(max([sum(x) for x in combinations(L,3) if sum(x)<=M]))
