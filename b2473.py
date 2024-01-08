input()
A = sorted(list(map(int,input().split())))
S = A[:3]
for k in range(len(A)-2):
    l = k+1
    r = len(A)-1
    while (l<r):
        s = A[l]+A[r]+A[k]
        if abs(sum(S))>abs(s):S=[A[k],A[l],A[r]]
        if s<0:l+=1
        else:r-=1
print(*S)