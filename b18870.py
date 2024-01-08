input()
a=sorted([(v,k) for k,v in enumerate(map(int,input().split()))])
A=[-1]*len(a)
cnt=0
prev=a[0][0]
for v,k in a:
    if v!=prev:
        cnt+=1
    A[k]=cnt
    prev=v
print(*A)