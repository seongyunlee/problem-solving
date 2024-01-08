for _ in range(int(input())):
    a=""
    N,word=input().split()
    N=int(N)
    for w in word:
        a+=w*N
    print(a)