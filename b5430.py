import sys
input = sys.stdin.readline
from queue import deque
for _ in range(int(input())):
    M = input().strip()
    input()
    Q = deque(map(int,[x for x in input().strip("[]\n").split(",") if x]))
    front = True
    for m in M:
        if m == "D":
            if not Q:
                print("error")
                Q = None
                break
            if front:
                Q.popleft()
            else:
                Q.pop()
        else:
            front = not front
    if not Q==None:print("[" + ",".join(map(str,list(Q) if front else (list(Q)[::-1]))) + "]")
