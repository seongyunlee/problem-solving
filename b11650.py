print(*[str(x)+" "+str(y) for x,y in sorted([list(map(int,input().split())) for _ in range(int(input()))])],sep="\n")
