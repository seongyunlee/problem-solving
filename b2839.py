N = int(input())
i = N//5
while i>=0:
    if (N-5*i)%3==0:
        print(i+(N-5*i)//3)
        exit()
    i-=1
print(-1)