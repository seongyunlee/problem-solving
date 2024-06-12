for _ in range(int(input())):
    bitMask = [bin(x)[2:].zfill(3) for x in list(map(int, input().split()))]
    print("YES" if any([all([mask[i] == bitMask[0][i] for mask in bitMask]) for i in range(3)]) else "NO")
    
    
