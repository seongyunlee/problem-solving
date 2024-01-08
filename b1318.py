

from itertools import combinations
cards=[]
cnt=[0]*12
idx={'top':0,'one':1,'two':2,'tripple':3,'straight':4,'backstraight':5,'mountain':6,'flush':7,'fullhouse':8,'four':9,'stifle':10,'royal':11}
for i in range(4):
    for j in range(13):
        cards.append([j,i])
rtf=[0]*4
hands=list(combinations(cards,6))
for c in hands:
    rank=-1
    pick=list(combinations(c,5))
    
    for p in pick:
        flush=False
        straight=False
        nums=[k[0] for k in p]
        symbol=[x[1] for x in p]
        if all([x==symbol[0] for x in symbol]):flush=True
        nums.sort()
        if all(nums[x]==nums[x-1]+1 for x in range(1,len(nums))):straight=True
        if flush and [0,1,2,3,4]==nums:
            rank=idx['royal']
            rtf[symbol[0]]+=1
        if rank>=idx['royal']:continue
        if straight and flush:rank=idx['stifle']
        if rank>=idx['stifle']:continue
        number=[nums.count(x) for x in set(nums)]
        if 4 in number:rank=idx['four']
        if rank>=idx['four']:continue
        if 3 in number and 2 in number:rank=idx['fullhouse']
        if rank>=idx['fullhouse']:continue
        if flush:rank=idx['flush']
        if rank>=idx['flush']:continue
        if [0,9,10,11,12]==nums:rank=idx['mountain']
        if rank>=idx['mountain']:continue
        if [0,1,2,3,4]==nums:rank=idx['backstraight']
        if rank>=idx['backstraight']:continue
        if straight:rank=idx['straight']
        if rank>=idx['straight']:continue
        if 3 in number:rank=idx['tripple']
        if rank>=idx['tripple']:continue
        if number.count(2)==2: rank=idx['two']
        if rank>=idx['two']:continue
        if 2 in number: rank=idx['one']
        if rank>=idx['one']:continue
        if rank==-1:rank=idx['top']      
    cnt[rank]+=1
print(cnt)
print(rtf)
print(sum(cnt),len(hands))

for c in cnt:
    a=c
    b=20358520
    fin=False
    while not fin:
        for i in range(2,a+1):
            if a%i==0 and b%i==0:
                a=a//i
                b=b//i
                break
            if i==a:
                fin=True
            if a==1:break

        if a==1: fin=True
    print(str(a)+'/'+str(b))
print("1005/3094")
print("486537/1017926")
print("24354/195755")
print("1408/39151")
print("14103/1017926")
print("9/4606")
print("9/4606")
print("25747/2544815")
print("228/27965")
print("3/4165")
print("184/2544815")
print("1/108290")