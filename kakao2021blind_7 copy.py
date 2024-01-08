edge={}
sale=[]
dp=[]
def get_min(p_go,p_no):
    global dp
    if dp[p_no][p_go]!=-1:
        return dp[p_no][p_go]
    acc=sale[p_no-1] if p_go else 0
    no_go=True
    for f in edge[p_no]:
        if get_min(True,f)<get_min(False,f):
            acc+=get_min(True,f)
            no_go=False
        else:
            acc+=get_min(False,f)
    if no_go and edge[p_no] and not p_go:
        _,min_f=min([[get_min(True,f)-get_min(False,f),f] for f in edge[p_no]])
        acc-=get_min(False,min_f)
        acc+=get_min(True,min_f)
    dp[p_no][p_go]=acc
    return acc
def solution(sales, links):
    global sale
    global edge
    global dp
    dp=[[-1,-1] for _ in range(len(sales)+1)]
    sale=sales
    edge={i:[] for i in range(1,len(sale)+1)}
    for l,f in links:
        edge[l].append(f)
    return min(get_min(True,1),get_min(False,1))
print(solution([5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
print(*enumerate(dp))