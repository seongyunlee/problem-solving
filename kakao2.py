E = {}
joint = set()
import sys
sys.setrecursionlimit(10**3)
def checkCycle(goal,now):
    print(goal,now ,E[now])
    if now == goal : return True
    if (not now in E) or len(E[now])!=1:return False
    if checkCycle(goal,E[now][0]):
        return True
def isBar(start,now):
    if start==now:return False
    if not now in E: return True
    if len(E[now])>1:
        return False
    return isBar(E[now][0])
def solution(edges):
    global E
    for f,t in edges:
        if f in E:
            E[f].append(t)
        else:
            E[f]=[t]
    center = None
    eight = 0
    bar = 0
    dought = 0
    for node in E.keys():
        if len(E[node])==2:
            if center!=None:
                joint.add(node)
                eight +=1
            elif all([checkCycle(node,child) for child in E[node]]):
                joint.add(node)
                eight +=1
            else:
                center = node
        elif len(E[node])>2:
            center = node
    for n in E[center]:
        if n in joint: continue
        if isBar(n,n):
            bar += 1
        else:
            dought +=1
    return [center,dought,bar,eight]
solution([[2, 3], [4, 3], [1, 1], [2, 1]])