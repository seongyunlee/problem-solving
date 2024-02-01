from collections import deque
import sys
DQ = deque()
input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    s = input().rstrip()
    if s[:4] == "push":
        DQ.append(s[5:])
    elif s == "pop":
        ans.append(DQ.popleft() if DQ else -1)
    elif s == "size":
        ans.append(len(DQ))
    elif s == "empty":
        ans.append(0 if DQ else 1)
    elif s == "front":
        ans.append(DQ[0] if DQ else -1)
    elif s == "back":
        ans.append(DQ[-1] if DQ else -1)
print("\n".join(map(str,ans)))