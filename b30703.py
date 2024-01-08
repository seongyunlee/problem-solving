input()
A=list(map(int,input().split()))
B=list(map(int,input().split()))
X=list(map(int,input().split()))
gap = [a-b for a,b in zip(A,B)]
times = [abs(g//x) for g,x in zip(gap,X) if g%x==0]
if len(times)!=len(gap):
    print(-1)
    exit()
if not all([t%2==times[0]%2 or X[i]==0 for i,t in enumerate(times)]):
    print(-1)
    exit()
print(max(times))