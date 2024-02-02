ans = []
while True:
    S = input()[:-1]
    if not S:
        break
    stack = []
    yes = True
    for i,s in enumerate(S):
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1]  != '(':
                ans.append('no')
                yes = False
                break
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[':
                ans.append('no')
                yes = False
                break
            stack.pop()
    if yes:ans.append('yes' if not stack else 'no')
print("\n".join(ans))