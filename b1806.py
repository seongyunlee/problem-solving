N,T=map(int,input().split())
A=list(map(int,input().split()))
S=[A[0]]
for i in A:
    S.append(S[-1]+i)
if(S[-1]<T):
    print(0)
    exit()
start=0
end=len(A)
while start<end:
    print(start,end)
    mid=(start+end)//2
    for i in range(len(S)-mid):
        if S[i+mid]-S[i]>=T:
            end=mid
            break
        if i==len(S)-mid-1:
            start=mid+1
print(start)