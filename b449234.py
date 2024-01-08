from queue import heappop,heappush
def solution(a, b, g, s, w, t):
    answer = -1
    q=[]
    answer=0
    for i in range(len(g)):
        heappush(q,[-(min(min(a,g[i])+min(b,s[i]),w[i])/t[i]),i,t[i]])
    while q and (a>0 or b>0):
        print(q,a,b,g,s,answer)
        _,i,tt=heappop(q)
        on=min(w[i],g[i],a)
        g[i]-=on
        a-=on
        r=min(w[i]-on,s[i],b)
        s[i]-=r
        b-=r
        answer+=tt
        heappush(q,[-(min(min(a,g[i])+min(b,s[i]),w[i])/(2*t[i])),i,2*t[i]])
    return answer
print(solution(90,500,[70,70,0]	,[0,0,500]	,[100,100,2],	[4,8,1]))