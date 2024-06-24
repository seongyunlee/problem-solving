N = int(input())
L = input().split()
fruits = [[-1,-1],[-1,-1]]
ans = min(2, N)
start = 0
for idx, l in enumerate(L):
    if len(fruits) == 2 and not l in [fruits[0][0], fruits[1][0]]:
        start = fruits[0][1] + 1
        fruits[0] = fruits[1]
        fruits[1] = [l, idx, idx]
    else:
        if l == fruits[0][0]:
            fruits[0][1] = idx
        elif l == fruits[1][0]:
            fruits[1][1] = idx
    ans = max(ans, idx - start + 1)
print(ans)