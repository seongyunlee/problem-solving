import sys
sys.setrecursionlimit(int(1e6))
input()
A=input().split()
B=input().split()
A=B=[i for i in range(1,100000)]
I={c:i for i,c in enumerate(A)}
s=[]
def tf(a,b,c,d):
    global s
    print(a,b,c,d)
    if None in [a,b,c,d]:return
    s+=[B[d]]
    if b-a==0:return
    tf(a if I[B[d]]>a else None,I[B[d]]-1 if I[B[d]]>a else None,c if I[B[d]]>a else None,c+I[B[d]]-1-a if I[B[d]]>a else None)
    tf(I[B[d]]+1 if I[B[d]]<b else None,b,d-b+I[B[d]] if I[B[d]]<b else None,d-1)
tf(0,len(A)-1,0,len(B)-1)
print(*s)