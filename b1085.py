words=[]
for _ in range(int(input())):
    words.append(input())
words.sort(key=lambda x:[len(x),x])
prev=""
for w in words:
    if not prev==w:
        print(w)
        prev=w