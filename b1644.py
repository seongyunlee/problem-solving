N=int(input())
if N==1:
    print(0)
    exit()
is_prime=[True]*(N+1)
for i in range(2,len(is_prime)):
    if is_prime[i]==False:continue
    m=i*2
    while m<len(is_prime):
        is_prime[m]=False
        m+=i
primes=[n for n,p in enumerate(is_prime) if p==True][2:]
cnt=0
high=1
low=0
sum=primes[0]
up=True
while low<=high:
    if sum==N:
        cnt+=1
        sum-=primes[low]
        low+=1
        up=True
    elif sum<N:
        if up:
            if high==len(primes):break
            sum+=primes[high]
            high+=1
        else:
            sum-=primes[low]
            low+=1
            up=True
    elif sum>N:
        if up:
            sum-=primes[low]
            low+=1
            up=False
        else:
            sum-=primes[high-1]
            high-=1
print(cnt)