x,y = map(int,input().split())
L = list(range(1,x+1))
A = []
idx = 0
while len(A)!=x:
    if idx%y == y-1:
        A.append(L[idx])
    else:
        L.append(L[idx])
    idx += 1
print("<"+", ".join(map(str,A))+">")
