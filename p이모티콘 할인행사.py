
def solution(users, emoticons):
    J=P=0
    S=[10,20,30,40]
    for i in range(2**(2*len(emoticons))):
        j=p=0
        bits=bin(i)[2:].zfill(2*len(emoticons))
        sale = [S[int(bits[idx:idx+2],2)] for idx in range(0,len(bits),2)]
        print(sale)
        for u in users:
            buy=sum([emoticons[idx]//100*(100-sale[idx]) for idx in range(len(emoticons)) if sale[idx]>=u[0]])
            if buy>=u[1]:
                j+=1
            else:
                p+=buy
        if j>J:
            J=j;P=p
        elif j==J and p>P:
            P=p
    return [J,P]
print(solution([[40, 10000], [25, 10000]]	,[7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))