from itertools import combinations
edge={}
sale=[]
dp=[]
def total(go_list,p):
    acc=sum([sale[i-1] for i in go_list])
    go_dic={i:True for i in go_list}
    for f in edge[p]:
        acc+=dfs(go_dic.get(f)!=None,f)
    return acc
def dfs(p_go,p_no):
    global dp
    min_w=1e17
    if dp[p_no][p_go]!=-1:
        return dp[p_no][p_go]
    if edge[p_no]==[]:
        dp[p_no][p_go]=0
        return 0
    leader=[]
    no_leader=[]
    for i in edge[p_no]:
        if edge[i]==[]:no_leader.append(i)
        else:leader.append(i)
    if p_go:
        min_w=min(min_w,total([],p_no))
    for i in range(1,len(leader)+1):
        for c in combinations(leader,i):
            min_w=min(min_w,total(c,p_no))
    if not p_go:
        for nl in no_leader:
            min_w=min(min_w,total([nl],p_no))
    dp[p_no][p_go]=min_w
    return min_w
def solution(sales, links):
    global sale
    global edge
    global dp
    dp=[[-1,-1] for _ in range(len(sales)+1)]
    sale=sales
    edge={i:[] for i in range(1,len(sale)+1)}
    for l,f in links:
        edge[l].append(f)
    edge[0]=[1]
    return dfs(True,0)