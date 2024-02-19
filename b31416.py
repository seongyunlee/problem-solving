import sys
input = sys.stdin.readline
for _ in range(int(input())):
    Ta,Tb,A,B = map(int,input().split())
    finB = Tb*B
    if Ta*A <= finB:
        print(finB)
    else:
        timeWhenBDone = (finB//Ta)*Ta
        gap = finB - timeWhenBDone
        R = A - finB//Ta
        if gap == 0:
            time = 0
            cnt = 0
            while cnt<R:
                cnt += 2
                time += Ta
            print(timeWhenBDone+time)
        else:
            time = Ta
            jump = [gap,Ta-gap]
            cnt = 1
            while cnt<R:
                cnt += 1
                time += jump[cnt%2]
            print(timeWhenBDone+time)