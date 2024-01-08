def f(N):
    r=1
    for i in range(N,1,-1):
        r*=i
    return r
for i,c in enumerate(str(f(int(input())))[::-1]):
    if c!='0':
        print(i)
        break