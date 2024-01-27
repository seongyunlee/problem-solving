import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def checkDoor(L,r,c,sInfo,dInfo,sMap):
    # Assume that L[r][c] is door
    if sMap[r][c] == None:
        dId = len(dInfo)
        sMap[r][c] = dId
        dInfo[dId] = [L[r][c],set(),set()]
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        nr,nc = r+dr,c+dc
        if not (0<=nr<len(L) and 0<=nc<len(L[0])):
            continue
        if L[nr][nc].isupper() and sMap[nr][nc] != None:
            dInfo[sMap[r][c]][2].add(sMap[nr][nc])
            dInfo[sMap[nr][nc]][2].add(sMap[r][c])
        elif L[nr][nc] != "*" and sMap[nr][nc] != None:
            dInfo[sMap[r][c]][1].add(sMap[nr][nc])
            sInfo[sMap[nr][nc]][0].add(sMap[r][c])
def section(L,r,c,sId,dInfo,sInfo,sMap):
    # sInfo = {"sid":[doors in section,keys in section, # of documents]}
    # dInfo = {"dorId":[two section of door]}
    sMap[r][c] = sId
    if L[r][c].islower():
        sInfo[sId][1].append(L[r][c])
    if L[r][c] == "$":
            sInfo[sId][2] += 1
    for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < len(L) and 0 <= nc < len(L[0])):
            continue
        if sMap[nr][nc] != None:
            continue
        if L[nr][nc] == "*" or L[nr][nc].isupper():
            continue
        section(L,nr,nc,sId,dInfo,sInfo,sMap)
def inp():
    L = [input().strip() for _ in range(int(input().split()[0]))]
    ##print(L)
    sMap = [[None]*len(L[0]) for _ in range(len(L))]
    dInfo = {}
    sInfo = {}
    for r in range(len(L)):
        for c in range(len(L[0])):
            if sMap[r][c] == None and (L[r][c] == "." or L[r][c].islower() or L[r][c] == "$"):
                sId = len(sInfo)
                sInfo[sId] = [set(),[],0]
                section(L,r,c,sId,dInfo,sInfo,sMap)
    for r in range(len(L)):
        for c in range(len(L[0])):
            if L[r][c].isupper() and sMap[r][c] == None:
                checkDoor(L,r,c,sInfo,dInfo,sMap)
    return L,sMap,dInfo,sInfo
def solve():
    L,sMap,dInfo,sInfo = inp()
    keys = set([x.upper() for x in list(input().strip()) if x!="0"])
    q = []
    d = set()
    for r in [0,len(L)-1]:
        for c in range(len(sMap[0])):
            if L[r][c] in [".","$"] or L[r][c].islower():
                q.append(sMap[r][c])
            if L[r][c].isupper():
                d.add(sMap[r][c])
    for c in [0,len(L[0])-1]:
        for r in range(len(sMap)):
            if L[r][c] in [".","$"] or L[r][c].islower():
                q.append(sMap[r][c])
            if L[r][c].isupper():
                d.add(sMap[r][c])
    ###print(*sMap,sep="\n")
    visited = [False]*len(sInfo)
    ans = 0
    ###print(*sInfo.items(),sep="\n")
    ###print(*dInfo.items(),sep="\n")
    openD = [False]*len(dInfo)
    # q : ready to visit section
    # d : pending for open door
    while q or d:
        oD = set()
        pD = set()
        for door in d:
            if dInfo[door][0] in keys:
                openD[door] = True
                oD.add(door)
                for dId in dInfo[door][2]:
                    if not openD[dId]:
                        pD.add(dId)
                for sId in dInfo[door][1]:
                    if not visited[sId]:
                        q.append(sId)
        for ppDD in pD:
            d.add(ppDD)
        for ooDD in oD:
            d.remove(ooDD)
        if not q and not oD:
            break
        if not q:
            continue 
        sId = q.pop()
        if visited[sId]: continue
        visited[sId] = True
        ans += sInfo[sId][2]
        for k in sInfo[sId][1]:
            keys.add(k.upper())
        for door in sInfo[sId][0]:
            d.add(door)
    return ans
print(*[solve() for _ in range(int(input()))],sep="\n")