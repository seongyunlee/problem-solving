N,M = map(int,input().split())
ans = 1
toBin = bin(M)[2:]
while True:
    if not toBin:
        print(-1)
        exit()
    if int(toBin,2) == N:
        print(ans)
        exit()
    if toBin[-1]=="1":
        toBin = toBin[:-1]+"0"
        before = int(toBin,2)
        if before % 10 !=0:
            print(-1)
            exit()
        toBin = bin(before//10)[2:]
    elif toBin[-1]=="0":
        toBin = toBin[:-1]
    ans += 1
