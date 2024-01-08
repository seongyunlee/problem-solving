C=[]
T=[]
E=[]
cards=[]
def possible(idx,num):
    if len(C[idx])==0:
        return (T[idx-1]//3+T[idx-1]%3//2+T[idx-1]%3%2)<=num<=T[idx-1]
    base=num//len(C[idx])
    remain=num%len(C[idx])
    nums=[base + (1 if i<remain else 0) for i in range(len(C[idx]))]
    for i in range(len(C[idx])):
        if not possible(C[idx][i],nums[i]):
            return False
    return True
def make(num,total):
    three=(total-num)//2
    two=(total-num)%2
    one=num-three-two
    return [1]*one+[2]*two+[3]*three
def choose(idx,num):
    if len(C[idx])==0:
        cards[idx]=make(num,T[idx-1])
        return
    base=num//len(C[idx])
    remain=num%len(C[idx])
    nums=[base + (1 if i<remain else 0) for i in range(len(C[idx]))]
    for i in range(len(C[idx])):
        choose(C[idx][i],nums[i])
def insert():
    answer=[]
    while True:
        now=1
        while True:
            if len(C[now])==0:
                if len(cards[now])==0:
                    return answer
                answer.append(cards[now].pop(0))
                break
            cur = now
            now = C[now][E[now]]
            E[cur]=0 if E[cur]+1==len(C[cur]) else E[cur]+1
def solution(edges, target):
    global C,T,E,cards
    T=target
    C=[[] for _ in range(len(edges)+2)]
    for f,t in edges:
        C[f].append(t)
    for c in C:
        c.sort()
    E=[0]*(len(edges)+2)
    cards=[[] for _ in range(len(edges)+2)]
    for i in range(sum(target)//3,sum(target)+1):
        if possible(1,i):
            choose(1,i)
            return insert()
    return [-1]
print(solution([[1,2],[2,3],[2,4],[4,5]],[0,0,3,0,3]))
#print(solution([[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]],[0, 0, 0, 3, 0, 0, 5, 1, 2, 3]))