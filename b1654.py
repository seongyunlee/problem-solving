K,N=map(int,input().split())
nums=[]
div=[]
for i in range(K):
    nums.append(int(input()))
end=max(nums)
start=max(1,end//N)
def check(mid):
    cnt=0
    for n in nums:
        cnt+=n//mid
    return cnt
while True:
    mid=(start+end)//2
    cnt=check(mid)
    if cnt<N:
        end=mid-1
    else:
        if end-start==1:
            if check(end)>=N:
                print(end)
                break
            else:
                print(start)
                break
        elif end==start:
            print(mid)
            break
        else:
            start=mid