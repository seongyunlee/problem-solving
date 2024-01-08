from collections import deque
def rotate():
    global L,R,B,T
    if len(L)==0:
        T.appendleft(B.popleft())
        B.append(T.pop())
        return
    T.appendleft(L.popleft())
    R.appendleft(T.pop())
    B.append(R.pop())
    L.append(B.popleft())
def shift():
    global L,R,M,B,T
    if len(M)==0:
        T,B=B,T
        return
    L.appendleft(T.popleft())
    R.appendleft(T.pop())
    M.append(T)
    T=B
    B=M.popleft()
    B.appendleft(L.pop())
    B.append(R.pop())
L,R,T,B,M=[deque() for _ in range(5)]
def solution(rc, operations):
    global L,R,B,T,M
    L,R,T,B,M=[deque() for _ in range(5)]
    for i in range(len(rc[0])):
        T.append(rc[0][i])
        B.append(rc[-1][i])
    for i in range(1,len(rc)-1):
        L.append(rc[i][0])
        R.append(rc[i][-1])
    for i in range(len(rc)-2,0,-1):
        dq=deque()
        for j in range(1,len(rc[0])-1):
            dq.append(rc[i][j])
        M.append(dq)
    for o in operations:
        if o[0]=="S":
            shift()
        else:rotate()
    RC=[]
    RC.append([T.popleft() for _ in range(len(rc[0]))])
    for i in range(len(rc)-2):
        RC.append([L.popleft()]+[M[-(i+1)].popleft() for _ in range(len(rc[0])-2)]+[R.popleft()])
    RC.append([B.popleft() for _ in range(len(rc[0]))])
    return RC
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],	["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]],	["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
print(solution([[1,2],[3,4]],["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))