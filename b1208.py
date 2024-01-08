N,S=map(int,input().split())
num=list(map(int,input().split()))
sum_B=[]
cnt=0
def BSubSum(idx,sum):
    if idx==len(num)-1:
        sum_B.append(sum)
        sum_B.append(sum+num[idx])
    else:
        BSubSum(idx+1,sum)
        BSubSum(idx+1,sum+num[idx])
def ASubSum(idx,sum):
    global cnt
    if idx==len(num)//2:
        cnt+=(bisect_right(S-sum)-bisect_left(S-sum))  
    else:
        ASubSum(idx+1,sum)
        ASubSum(idx+1,sum+num[idx])
def bisect_left(t):
    l=0
    r=len(sum_B)
    while r-l>0:
        mid=(l+r)//2
        if sum_B[mid]<t:
            l=mid+1
        else:
            r=mid
    return l
def bisect_right(t):
    l=0
    r=len(sum_B)
    while r-l>0:
        mid=(l+r)//2
        if sum_B[mid]<=t:
            l=mid+1
        else:
            r=mid
    return l
BSubSum(len(num)//2,0)
sum_B.sort()
ASubSum(0,0)
print(cnt-(1 if S==0 else 0))
