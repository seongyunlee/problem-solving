N=int(input())
P=[-1]*N
cnt=0
def dfs(idx):
    global cnt,P
    if idx==N:cnt+=1
    for col in range(N):
        chk=True
        for i in range(idx):
            if not (col!=P[i] and (i-P[i])!=(idx-col) and (i+P[i])!=(idx+col)):
                chk=False
                break
        if chk:
            P[idx]=col
            dfs(idx+1)
dfs(0)
print(cnt)