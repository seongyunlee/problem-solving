file=open('input.txt')
M=list(map(int,file.read().strip().split()))
q=[[0,len(M)-1]]
s=[]
def check(idx,b):
    for i in range(idx,b+1):
        if M[i]>M[idx]:
            return i
    return None
while q:
    print(s,q)
    a,b=q.pop()
    s+=[M[a]]
    c=check(a,b)
    if a==b: continue
    if c==None or c==a+1:
        q+=[[a+1,b]]
    else:
        q+=[[a+1,c-1],[c,b]]
print(*s[::-1],sep="\n")