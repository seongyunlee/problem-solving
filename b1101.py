import copy
from importlib.util import find_spec
from itertools import permutations
N,M= map(int,input().split())
card=[]
colors=[[] for _ in range(M)]
for _ in range(N):
    card.append(list(map(int,input().split())))
bfs=[]
cnt=999999999999
for joker in range(0,N):
    now_cnt=N
    home=[False]*M
    zeros=0
    for i in range(N):
        if sum(card[i])==0:zeros+=1
        if i==joker:continue
        if card[i].count(0)==M-1:
            if home[[x!=0 for x in card[i]].index(True)]==False:
                home[[x!=0 for x in card[i]].index(True)]=True
    cnt=min(cnt,N-home.count(True)-zeros-(0 if sum(card[joker])==0 else 1))
print(cnt)

