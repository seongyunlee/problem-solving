'''
https://school.programmers.co.kr/learn/courses/30/lessons/92345
'''

from copy import deepcopy
def whoWin(board,turn,aloc,bloc,cnt):
    print('s',cnt,turn,aloc,bloc)
    minMax=cnt
    win=False
    P=[aloc,bloc] if turn else [bloc,aloc]
    for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:
        naloc=list(aloc);nbloc=list(bloc)
        P=[naloc,nbloc] if turn else [nbloc,naloc]
        oR,oC=P[0]
        sR,sC=P[1]
        if not (0<=oR+dr<len(board) and 0<=oC+dc<len(board[0])):continue
        if board[oR+dr][oC+dc]==0:continue
        if sR==oR and sC==oC:
            return [turn,cnt+1]
        nB=deepcopy(board)
        nB[oR][oC]=0
        P[0][0]=oR+dr;P[0][1]=oC+dc
        result,count = whoWin(nB,not turn,naloc,nbloc,cnt+1)
        if result==turn:
            if not win:
                win=True
                minMax=count
            else:
                minMax=min(minMax,count)
        elif not win:
            minMax=max(minMax,count)
    print(cnt,turn,win,aloc,bloc,minMax)
    return [turn if win else not turn,minMax]
def solution(board, aloc, bloc):
    answer=0
    return whoWin(board,True,aloc,bloc,0)[1]
print(solution(	[[1, 1, 1, 1, 1]], [0, 0], [0, 4]))