import sys
sys.setrecursionlimit(10000000)
A=[i for i in range(2500)]
id=2500
D={i:'' for i in range(2500)}
def get(cell):
    if D.get(cell)==None:
        return None
    if type(D[cell]) is str:
        return cell
    else:
        D[cell] = get(D[cell])
        return D[cell]
def insert(idx,value):
    global id
    D[id]=value
    A[idx]=id
    id+=1
    return id-1
def ind(r,c):
    return (int(r)-1)*50+(int(c)-1)
def solution(commands):
    answer=[]
    for c in commands:
        print(c)
        arg=c.split()
        if arg[0]=='UPDATE' and len(arg)==4:
            if get(A[ind(arg[1],arg[2])])==None:
                insert(ind(arg[1],arg[2]),arg[3])
            else:
                D[get(A[ind(arg[1],arg[2])])]=arg[3]
        elif arg[0]=='UPDATE':
            for k,v in D.items():
                if v==arg[1]:
                    D[k]=arg[2]
        elif arg[0]=='MERGE':
            org_A=get(A[ind(arg[1],arg[2])])
            org_B=get(A[ind(arg[3],arg[4])])
                
            if (org_A==None or D[org_A]=='') and (org_B!=None and D[org_B]!=''):
                if org_A==None:
                    A[ind(arg[1],arg[2])]=org_B
                else:
                    D[org_A]=org_B
            else:
                if org_A==None:
                    org_A=insert(ind(arg[1],arg[2]),'')
                if org_B==None:
                    A[ind(arg[3],arg[4])]=org_A
                else:
                    D[org_B]=org_A
        elif arg[0]=="UNMERGE":
            org_id=get(A[ind(arg[1],arg[2])])
            data=D[org_id] if org_id!=None else ''
            if org_id!=None:del(D[org_id])
            insert(ind(arg[1],arg[2]),data)
        else:
            item=get(A[ind(arg[1],arg[2])])
            if item!=None and len(D[item])>0:
                answer.append(D[item])
            else:
                answer.append("EMPTY")
        for i in range(4):
            print([str(get(A[i*4+j]))+'('+str(A[i*4+j])+')'  for j in range(4)])
        print(D)
    return answer
#print(solution(["UPDATE 1 1 A", "UPDATE 2 1 B", "MERGE 1 2 2 1"]))
#print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE "+str(i//50)+" "+str(i%50)+" "+str((i+1)//50)+" "+str((i+1)%50) for  i in range(2499)]+["UPDATE 50 50 kkk"]))