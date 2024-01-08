token=set(["<",">","&&","||","(",")"," "])
S=input()
acc=""
T=[]
for s in S:
    if s in token:
        T.append(acc)
        T.append(s)
        acc=""
    elif acc and acc[-1]+s in token:
        T.append(acc[:-1])
        T.append(acc[-1]+s)
        acc=""
    else:
        acc+=s
T.append(acc)
print(*[x for x in T if x!=" " and x!=""])