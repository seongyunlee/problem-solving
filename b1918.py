s=input()
r=""
def C(s):
    if len(s)==1:return s
    else: return B(s[1:-1])
def B(s):
    P=A(s)
    tn=[]
    for i in range(0,len(P),2):
        if len(P[i])==1:
            tn.append(P[i])
            if i+1<len(P):tn.append(P[i+1])
            continue
        K=[]
        start=0
        open=0
        for idx in range(len(P[i])):
            if P[i][idx]=="(":
                if open==0:start=idx    
                open+=1
            elif P[i][idx]==")":
                open-=1
                if open==0:
                    K.append(P[i][start:idx+1])
                    start=idx+1
            else:
                if open==0:
                    K.append(P[i][idx])
                    start=idx+1
        p=C(K[0])
        for pp in range(1,len(K),2):
            p+=C(K[pp+1])
            p+=K[pp]
        tn.append(p)
        if i+1<len(P):tn.append(P[i+1])
    rr=tn[0]
    for t in range(1,len(tn),2):
        rr+=tn[t+1]
        rr+=tn[t]
    return rr

def A(s):
    P=[]
    start=0
    open=0
    for idx in range(len(s)):
        if s[idx]=="(":open+=1
        if s[idx]==")":open-=1
        if s[idx] in ["+","-"] and open==0:
            P.append(s[start:idx])
            P.append(s[idx])
            start=idx+1
        idx+=1
    P.append(s[start:])
    return P
print(B(s))