import sys
from collections import defaultdict
input = sys.stdin.readline
for _ in range(int(input())):
    input()
    P = input().strip().split()
    cnt = {i:defaultdict(int) for i in range(1,5)}
    for p in P:
        for mask in range(16):
            bit = bin(mask)[2:].zfill(4)
            flag = ''.join([p[i] for i in range(4) if bit[i]=='1'])
            if 1<=len(flag)<=4:
                cnt[len(flag)][flag] += 1
    for i,a in [[4,0],[3,2],[2,4],[1,6]]:
        if any([k>2 for k in cnt[i].values()]):
            print(a)
            break
        if i==2:print(8)
    