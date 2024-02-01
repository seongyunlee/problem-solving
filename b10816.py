from collections import defaultdict
input()
D = defaultdict(int)
for i in input().split():
    D[i]+=1
input()
print(*[D[x] for x in input().split()])