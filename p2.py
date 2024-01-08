def find(queue1,queue2):
    q=queue1+queue2
    s=0
    e=1
    now=q[0]
    if sum(q)%2==1: return 999999
    half=sum(q)//2
    answer=999999
    while e<=len(q) and s<len(queue1):
        if now<=half:
            if e==len(q):break
            now+=q[e]
            e+=1
        elif now>half:
            now-=q[s]
            s+=1
        if now==half:
            if e>len(queue1):
                answer=min(s+e-len(queue1),answer)
            elif e==len(queue1):
                answer= min (s,answer)
            else:
                answer=min(e+len(queue2)+s,answer)
    return answer
def solution(queue1, queue2):
    answer= min(find(queue1,queue2), find(queue2,queue1))
    if answer==999999:return -1
    return answer
print(solution([2,1,1,1,10],	[1,6]))
#solution([1, 2, 1, 2],	[1, 10, 1, 2])