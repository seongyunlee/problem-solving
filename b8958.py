for _ in range(int(input())):
    now=0
    total=0
    for c in input():
        if c=="O":now+=1
        else:now=0
        total+=now
    print(total)