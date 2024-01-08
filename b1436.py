idx=int(input())
cnt=0
num=666
while True:
    if '666' in str(num):
        cnt+=1
    if cnt==idx:
        print(num)
        break
    num+=1