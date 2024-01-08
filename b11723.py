import sys
S=[False]*21
for k in range(int(sys.stdin.readline())):
    M=sys.stdin.readline().split()
    if M[0]=="all":
        S=[True]*21
    elif M[0]=="empty":
        S=[False]*21
    elif M[0]=='add':
        S[int(M[1])]=True
    elif M[0]=="remove":
        S[int(M[1])]=False
    elif M[0]=="check":
        print(int(S[int(M[1])]))
    elif M[0]=="toggle":
        S[int(M[1])]= not S[int(M[1])]