T, N = map(int, input().split())
L, K = map(int, input().split())
danger = list(map(int, input().split()))
safe = list(map(int, input().split()))


def bisect(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid][0] < target:
            left = mid + 1
        else:
            right = mid
    return right

def find(arr, frm, target):
    for i in range(frm, len(arr)):
        if arr[i][1] >= target:
            return i
    return -1


segment = None


def makeSegmentTree(arr):
    global segment
    segment = [[x[1] for x in arr]]
    while len(segment[-1]) > 1:
        segment.append([])
        for i in range(0, len(segment[-2]), 2):
            segment[-1].append(max(segment[-2][i] ,segment[-2][i+1] if i+1 < len(segment[-2]) else 0))
    segment = segment[::-1]

def find(tar, level, idx, following):
    if len(segment) - 1 == level:
        if  segment[level][idx] >= tar:
            return idx
        elif idx + 1 < len(segment[level]) and segment[level][idx+1] >= tar:
            return idx + 1
        return -1
    if segment[level+1][idx*2] >= tar:
        return find(tar, level+1, idx*2)
    return find(tar, level+1, idx*2+1) if idx*2+1 < len(segment[level+1]) else -1

def dfs(childIdx,level):
    if level == len(segment) - 1:
        return childIdx[level]
    if childIdx[level] == "0":
        


def query(frm, tar):
    global segment
    ans = 0
    idx = bin(frm)[2:].zfill(len(segment)-1)
    for i in range(len(idx)):
        if idx[i] == '0':
            left 
    return ans
    
    
    


danger.append(T)
D=[]
for i in range(len(danger)-1):
    D.append([danger[i], danger[i+1] - danger[i]])
print(D)
makeSegmentTree(D)
print(segment)
time = 1
for i in range(len(safe)-1):
    if safe[i+1] - safe[i] == 1:
        time += 1
    else:
        gap = safe[i+1] - safe[i] - 1
        idx = bisect(D, time%(2*T))
        waitFor = find(D, idx, gap)
        if waitFor != -1:
            time += (D[waitFor][0] - (time%(2*T)) -1 + gap)
        else:
            print("What is that map newbie...")
            exit()
print(time+1)


        
