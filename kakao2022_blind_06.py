def solution(board, skill):
    skill.sort(key=lambda x :(x[1],x[2]))
    print(skill)
    answer = 0
    for s in skill:
        isAttack=-1 if s[0]==1 else 1
        r1,c1,r2,c2,degree=s[1:]
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                board[r][c]+=isAttack*degree
    for r in board:
        for c in r:
            if c>0:
                answer+=1
    return answer
print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
