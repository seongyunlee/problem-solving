#https://school.programmers.co.kr/learn/courses/30/lessons/92343
I=E=None
answer=0
def chooseChild(childs,sheep,wolf):
    global answer
    answer=max(sheep,answer)
    for i in range(len(childs)):
        if childs[i]:
            n_childs=list(childs)
            n_childs[i]=False
            if I[i]==0 or sheep>wolf+1:
                for k in E[i]:
                    n_childs[k]=True
                chooseChild(n_childs,sheep+(1 if I[i]==0 else 0),wolf+(1 if I[i]==1 else 0))
        
def solution(info, edges):
    global I,E,answer
    I=info
    E={i:[] for i in range(len(info))}
    for f,t in edges:
        E[f].append(t)
    chooseChild([True]+[False]*(len(info)-1),0,0)
    return answer
print(solution([0,0,1,1,1,0,1,0,1,0,1,1],	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))