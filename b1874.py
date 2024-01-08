nums=[int(input()) for _ in range(int(input()))]
stack=[]
now=1
idx=0
answer=''
while idx<len(nums):
    if stack and nums[idx]==stack[-1]:
        answer+="-"
        stack.pop()
        idx+=1
    elif idx==len(nums):break
    else:
        stack.append(now)
        answer+='+'
        now+=1
        if now>len(nums)+1:
            break
if now>len(nums)+1:
    print('NO')
else:
    print(*answer,sep="\n")