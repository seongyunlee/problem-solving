N=int(input())
L=list(map(int,input().split()))
S=[L[0]]
for i in range(1,len(L)):
    S.append(S[-1]+L[i])
def cnt(idx):
    left=idx+1
    right=N-1
    while left<right:
        mid=(left+right)//2
        if (S[mid-1]-S[idx-1])>(S[-1]-S[mid-1]):
            right=mid
        else:
            left=mid+1
    if left==(N-1) and (S[-2]-S[idx-1])<=L[-1]:
        return 0
    minS=right
    if (S[-1]-S[minS-1])<S[idx-1]:return 0
    left=minS
    right=N-1
    while left<right:
        mid=(left+right)//2
        if (S[-1]-S[mid-1])>S[idx-1]:
            left=mid
        else:
            right=mid-1
        if left+1==right:
            if (S[-1]-S[right-1])>S[idx-1]:
                left=right
            else:break
    return left-minS+1
print(sum([cnt(idx) for idx in range(1,N-1)]))