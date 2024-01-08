s="("+input()+")"
r=""
q=[]
p={"*":2,"/":2,"+":1,"-":1}
for c in s:
    if c=="(":
        q.append(c)
    elif c.isalpha():
        r+=c
    elif c==")":
        while q:
            t=q.pop()
            if t=="(":break
            r+=t
    else:
        while q[-1]!="(" and p[q[-1]]>=p[c]:r+=q.pop()
        q.append(c)
print(r)