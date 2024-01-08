import sys
input = sys.stdin.readline
N=[list(input().strip()) for _  in range(int(input()))]
for n in N:
    if all([int(d) in [0,1] for d in n]):
        print("Hello, BOJ 2023!")
        continue
    C=[(0,'')]
    for idx in range(len(n)):
        nC=[]
        for acc,now in C:
            nC.append((acc+int(now+n[idx]),''))
            if idx<len(n)-1:nC.append((acc,now+n[idx]))
        C=nC
    C.sort()
    m=1
    cnt=0
    idx=0
    while True:
        power=sum([int(d)**m for d in n])
        if power>int(''.join(n)):break
        while C[idx][0]<=power:
            if power==C[idx][0]:
                cnt+=1
                break
            idx+=1
        m+=1
    print(cnt)