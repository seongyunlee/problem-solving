import sys
input = sys.stdin.readline
while True:
    a,b,c = map(int,input().split())
    if sum([a,b,c]) == 0:
        break
    if max([a,b,c])**2 == sum([x**2 for x in [a,b,c] if x!=max([a,b,c])]):
        print("right")
    else: print("wrong")