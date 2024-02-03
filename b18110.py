import sys
from math import ceil, floor
input = sys.stdin.readline
round = lambda x: ceil(x) if x-floor(x) >= 0.5 else floor(x)
N = [int(input()) for _ in range(int(input()))]
N.sort()
T = round(len(N)*0.15)
if len(N)>0: print(round(sum(N[T:len(N)-T])/(len(N)-2*T)))
else: print(0)