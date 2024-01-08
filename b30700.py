s = input()
idx = 0
for i in range(len(s)):
    if "KOREA"[idx%5] == s[i]:
        idx += 1
print(idx)