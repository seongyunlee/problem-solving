def solution(a):
    E={i:[] for i in range(len(a))}
    for i in range(len(a)):
        E[a[i]].append(i)
    S=list(E.items())
    S.sort(key=lambda x:len(x[1]),reverse=True)
    answer=None
    for k,v in S:
        reserv=-1
        length=0
        idx=0
        while idx<len(v):
            if reserv<v[idx]-1:
                length+=2
                idx+=1
                continue
            elif idx==len(v)-1:break
            for i in range(idx+1,len(v)):
                if (i+1==len(v) and i<len(a)) or v[i]-v[i-1]>1:
                    reserv=v[i-1]+1
                    length+=2
                    idx=i
                    break
        answer=max(answer,length) if answer else length
    return answer
print(solution([1,0]))