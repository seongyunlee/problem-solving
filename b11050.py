from itertools import combinations
x,y = map(int,input().split())
print(len(list(combinations(range(1,x+1),y))))