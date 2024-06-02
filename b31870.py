N = int(input())
nums = list(map(int, input().split()))

def findSortedMin(tar):
    pos = [[i,v] for i,v in enumerate(nums)]
    ans = 0
    for i in range(N):
        for ii in range(N):
            if tar[i] == pos[ii][1]:
                ans += abs(pos[ii][0]-i)
                pos[ii][0] = -1
                break
            else:
                pos[ii][0] += 1
    return ans

print(min(findSortedMin(sorted(nums)), findSortedMin(sorted(nums, reverse=True))+1))

    


        