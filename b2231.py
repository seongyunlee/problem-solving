N=int(input())
i=1
while True:
    if i+sum(list(map(int,list(str(i)))))==N:
        print(i)
        break
    i+=1
    if i>=N:
        print(0)
        break