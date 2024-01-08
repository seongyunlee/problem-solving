'''
https://school.programmers.co.kr/learn/courses/30/lessons/92344
'''
def solution(board, skill):
    answer = 0
    acc=dif=[[0]*len(board[0]) for _ in range(len(board))]
    for s in skill:
        isAttack=1 if s[0]==1 else -1
        r1,c1,r2,c2,degree=s[1:]
        dif[r1][c1]+=degree*isAttack
        if c2+1<len(dif[0]): dif[r1][c2+1]-=degree*isAttack 
        if r2+1<len(dif):dif[r2+1][c1]-=degree*isAttack
        if c2+1<len(dif[0]) and r2+1<len(dif): dif[r2+1][c2+1]+=degree*isAttack
    for i in range(len(dif)):
        a=0
        for j in range(len(dif[0])):
            a+=dif[i][j]
            acc[i][j]=a+(dif[i-1][j] if i>0 else 0)
    print(*acc,sep='\n')
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]>acc[r][c]:
                answer+=1
    return answer
print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	,[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))