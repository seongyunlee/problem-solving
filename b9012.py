import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def isValid(s):
    if s[0] == ')':
        return False
    else:
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
for _ in range(int(input())):
    print("YES" if isValid(input().rstrip()) else "NO")
    