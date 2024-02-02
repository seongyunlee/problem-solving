L = [list(map(int,input().split()))+[i] for i in range(int(input()))]
print(*[len([1 for x in L if x[0]>y[0] and x[1]>y[1]])+1 for y in L])