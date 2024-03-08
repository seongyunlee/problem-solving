S = input()
B = input()
stack = []
for s in S:
    if not stack:
        stack.append([s,1 if s==B[0] else 0])
    else:
        if B[stack[-1][1]] == s:
            stack.append([s,stack[-1][1]+1])
        else:
            if s==B[0]:
                stack.append([s,1])
            else:
                stack.append([s,0])
    if stack[-1][1] == len(B):
        for _ in range(len(B)):
            stack.pop()
if stack:
    print("".join([k[0] for k in stack]))
else:
    print("FRULA")