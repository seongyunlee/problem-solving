import sys
input = iter(open(0).read().split("\n")).__next__
D = list(map(int,input().split()))[::-1]
T = []
cnt = 0
ripe = []
box = set()
def inputR(axis,pos):
    global ripe,cnt
    if axis == 10:
        global cnt
        line = list(map(int,input().split()))
        for i in range(len(line)):
            if line[i]==-1:continue
            cnt+=1
            if line[i]==1:
                ripe.append(pos+[i])
                box.add(str(pos+[i]))
        return line
    else:
        now = []
        for i in range(D[axis]):
            now.append(inputR(axis+1,pos+[i]))
    return now
dMatrix = []
def get(M,pos,idx = 0):
    if not 0<=pos[idx]<len(M): return None
    if idx==10: return M[pos[idx]] 
    else: return get(M[pos[idx]],pos,idx+1)
for dir in [-1,1]:
    for dim in range(11):
        dMatrix.append([dir if i==dim else 0 for i in range(11)])
sumP = lambda x,y:[a+b for a,b in zip(x,y)]
posCheck = lambda x: all([0<=x<y for x,y in zip(x,D)])
T = inputR(0,[])
ans = 0
while len(box)<cnt:
    ans+=1
    nr = []
    for r in ripe:
        for dM in range(11):
                for dir in [-1,1]:
                    now = list(r)
                    now[dM] += dir
                    if not posCheck(now):continue
                    ele = get(T,now)
                    if ele==0 and not str(now) in box:
                        nr.append(now)
                        box.add(str(now))
                        if len(box)==cnt:
                            print(ans)
                            exit()
    if len(nr)==0:
        print(-1)
        exit()
    ripe = nr
print(ans)