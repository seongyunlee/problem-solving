N=int(input())
print(sum([v*(N-idx) for idx,v in enumerate(sorted(list(map(int,input().split()))))]))