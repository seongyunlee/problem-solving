a,b=map(int,[str(x)[::-1] for x in input().split()])
print(a if a>b else b)