X,Y = map(int,input().split())

# 0 부터 11...11(x-bit) 까지 1의 개수
def ones(x):
    return x*(2**x)//2

# 0 부터 dec 까지 1의 개수
def calc(dec):
    if dec == 0:return 0
    binary = bin(dec)[2:]
    acc = 0
    acc += ones(len(binary)-1)
    lowerDec = dec & int('0'+'1'*(len(binary)-1),2)
    acc += (lowerDec+1)
    acc += calc(lowerDec)
    return acc
print(calc(Y)-calc(X-1))
