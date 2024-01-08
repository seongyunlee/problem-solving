def combi(n,m):
    k=1
    for i in range(m):
        k*=(n-i)
    for i in range(1,m+1):
        k=k//i
    return k
n,m=map(int,input().split())
print(combi(n,m))