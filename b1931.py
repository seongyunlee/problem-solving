I=[list(map(int,input().split())) for _ in range(int(input()))]
I.sort(key=lambda x:[x[1],x[0]])
cnt=0
prev=0
idx=0
while idx<len(I):
    if I[idx][0]>=prev:
        cnt+=1
        prev=I[idx][1]
    idx+=1
print(cnt)
