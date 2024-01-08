M,N=map(int,input().split())
A={input():True for _ in range(M)}
B=[]
for i in range(N):
    if A.get(a:=input()):
        B.append(a)
print(len(B),*sorted(B),sep="\n")