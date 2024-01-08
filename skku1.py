N,M,K=map(int,input().split())
if K>=M+N-1:
    print("YES")
    print(*[" ".join([str(y) for y in range(x,x+M)]) for x in range(1,N+1)],sep="\n")
else:
    print("NO")