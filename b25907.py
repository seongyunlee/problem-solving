import sys
input=sys.stdin.read
def print(str):
    sys.stdout.write(str+"\n")
    sys.stdout.flush()
N=int(input())
f=1
l=N
while True:
    day=(f+l)//2
    print("? "+str(day))
    s=int(input())
    w=day-s
    if s==w:
        print("! "+str(day))
        exit()
    if s>w:
        f=day+1
    else:
        l=day-1

    
