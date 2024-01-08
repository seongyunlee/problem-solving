def solution(rows, columns, queries):
    A=[[i for i in range(k,k+columns)] for k in range(1,rows*columns,columns)]
    print(A)
    answer=[]
    for r1,c1,r2,c2 in queries:
        prev=A[r1-1][c1]      
        dxdy=[[0,1]]*(c2-c1)+[[1,0]]*(r2-r1)+[[0,-1]]*(c2-c1)+[[-1,0]]*(r2-r1)+[[0,1]]
        print(dxdy)
        minA=rows*columns
        r,c=r1-1,c1-1
        for i in range(len(dxdy)):
            r,c=r+dxdy[i][0],c+dxdy[i][1]
            print(i,r,c)
            minA=min(minA,A[r][c])
            prev,A[r][c]=A[r][c],prev
        answer.append(minA)
        print(*A,sep='\n')
    return answer
print(solution(6,	6	,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))