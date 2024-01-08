import sys
input = sys.stdin.readline
ans = []
def getMinLargeRoot(n):
    # get minimum integer x where the sqaure root of (x) is Integer and x>=n
    if n==0:return 0
    if n==1:return 1
    l,r = 1,n
    while l<r:
        m = (l+r)//2
        if m*m>=n:
            r = m
        else:
            l = m+1
    return l
for _ in range(int(input())):
    N = int(input())
    D = getMinLargeRoot(N)
    rows = N//D
    rows += 1 if N%D!=0 else 0
    ans.append(rows*2+D*2)
print("\n".join(map(str,ans)))
    