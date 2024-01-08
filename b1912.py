N=int(input())
L=list(map(int,input().split()))
dp=[-1]*len(L)
dp[-1]=len(L)-1
sub_sum=[L[0]]
ans=L[-1]
for i in range(1,len(L)):
    sub_sum.append(L[i]+sub_sum[-1])
for i in range(len(L)-2,-1,-1):
    dp[i]=dp[i+1] if sub_sum[dp[i+1]]>sub_sum[i] else i
    ans=max(sub_sum[dp[i]]-(sub_sum[i-1] if i>0 else 0),ans)
print(ans)