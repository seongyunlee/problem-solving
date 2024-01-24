y = int(input().split()[1])
print(*[x for x in list(map(int,input().split())) if x < y],sep=" ")