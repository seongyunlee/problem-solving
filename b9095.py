def find(n):
    if n==1:return 1
    if n==0: return 1
    return sum([find(n-x) for x in range(1,4) if n-x>=0])
print(*[find(int(x)) for x in open(0).readlines()[1:]],sep='\n')
