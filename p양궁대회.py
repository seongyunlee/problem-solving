#https://school.programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    answer = [-1]
    maxi=0
    gap=lambda x:sum([((10-i) if info[i]!=x[i] else 0)*(1 if x[i]>info[i] else -1) for i in range(11)])
    for i in range(2**11,-1,-1):
        bits=bin(i)[2:].zfill(11)
        k=[(info[i]+1 if bits[i]=='1' else 0) for i in range(11)]
        if sum(k)>n:continue
        now_gap=gap(k)
        if (answer!=[-1] and now_gap<maxi) or now_gap<=0:continue
        remain=n-sum(k)
        for i in range(10,-1,-1):
            if bits[i]=='1':
                k[i]+=remain
                remain=0
            else:
                k[i]=min(remain,info[i])
                remain-=k[i]
            if remain==0:break
        if answer!=[-1] and now_gap==maxi and k>answer:continue
        answer=k
        maxi=now_gap
    return answer
print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))