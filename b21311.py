atEven = {}
S = input()
for i,k in enumerate(S):
    if k in atEven:
        if atEven[k]==4:
            print("NO")
            exit()
        if S[i-1]==S[i]:
            atEven[k]=4
        elif atEven[k] == (3 if (i%2==0) else 2):
            print("NO")
            exit()
        else:
            atEven[k] = 4
    else: atEven[k] = 3 if (i%2==0) else 2
print("YES")