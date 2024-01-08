import sys
sys.setrecursionlimit(1000000)
B=''
def chk(frm,to):
    if frm==to:return True
    root=(frm+to)//2
    if B[root]=='0':
        return not any(['1'== b for b in B[frm:to+1]])
    return chk(frm,root-1) and chk(root+1,to)
def solution(numbers):
    global B
    answer = [0]*len(numbers)
    for idx,n in enumerate(numbers):
        b=bin(n)[2:]
        length='1'*(len(bin(len(b)))-2)
        while int(length,2)<2*len(b):
            B='0'*(int(length,2)-len(b))+b
            if chk(0,len(B)-1):
                answer[idx]=1
                break
            length+='1'
    return answer
print(solution([7, 42, 5]))