dp = None
L = None
N = None
E = []
def getDP(idx,K):
    print(idx,K)
    if idx==-1 or K==0:
        return [None,None,None]
    if dp[idx][K][0] != None:
        return dp[idx][K]
    minMax = 900000000
    sub = 900000000
    isContain = False
    for left in range(1,K+1):
        # 왼쪽 child가 없다면 오른쪽으로만 확인
        if E[idx][0]==-1:
            if E[idx][1]==-1:
                #오른쪽도 없다면
                dp[idx][K] =  [N[idx],N[idx],True] if K==1 else [None,None,None]
                return dp[idx][K]
            # 오른쪽 연결
            rightS,rightMax,contain = getDP(E[idx][1],K)
            if not rightS == None and min([rightS+N[idx],rightMax])<minMax:
                isContain = rightMax<rightS+N[idx]
                minMax = min([rightS+N[idx],rightMax])
                sub = rightS+N[idx]
            # 오른쪽 안연결
            if K-1>0:
                rightS,rightMax,contain = getDP(E[idx][1],K-1)
                if not rightS == None and min([rightS+N[idx],rightMax])<minMax:
                    isContain = rightS+N[idx]<rightMax
                    minMax = min([rightS+N[idx],rightMax])
                    sub = rightS+N[idx]
            break
        # 왼쪽 subTree를 left개 group으로 나눈다.
        leftS,leftMax,contain = getDP(E[idx][0],left)
        if leftS==None:
            continue
        # 왼쪽만 연결
        if K>=K-left+1>0:
            rightS,rightMax,contain = getDP(E[idx][1],K-left+1)
            if not rightS==None and min([rightMax,leftS+N[idx],leftMax])<minMax:
                minMax = min([rightMax,leftS+N[idx],leftMax])
                sub = leftS + N[idx]
        #오른쪽만 연결
            if not rightS==None and min([rightMax,rightS+N[idx],leftMax])<minMax:
                minMax = min([rightMax,rightS+N[idx],leftMax])
                sub = rightS + N[idx]
        #양쪽 연결
        if K>=K-left+2>0:
            rightS,rightMax,contain = getDP(E[idx][1],K-left+2)
            if not rightS==None and min([rightMax,rightS+N[idx],leftMax])<minMax:
                minMax = min([rightMax,rightS+leftS+N[idx],leftMax])
                sub = rightS + N[idx] + leftS
        #둘다 안 연결
        if K-left>0:
            rightS,rightMax,contain = getDP(E[idx][1],K-left)
            if not rightS==None and min([rightMax,N[idx],leftMax])<minMax:
                minMax = min([rightMax,N[idx],leftMax])
                sub = N[idx]
    dp[idx][K] = [sub,minMax,isContain]
    return dp[idx][K]
parents = {}
def getRoot(idx):
    if parents.get(idx)==None:
        return idx
    else:return getRoot(parents[idx])
def solution(k, num, links):
    global dp,E,L,N,parents
    E= links
    for idx in range(len(E)):
        l,r = E[idx]
        parents[l] = idx
        parents[r] = idx
    root = getRoot(0)
    N = num
    dp = [[[None,None,None] for _ in range(k+2)] for _ in range(len(num))]
    A =  getDP(root,k)[1]
    print(dp)
    return(A)
print(solution(1,[6, 9, 7, 5],[[-1, -1], [-1, -1], [-1, 0], [2, 1]]))