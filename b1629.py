a,b,c=map(int,input().split())
def power(n):
    if n<=2:
        return (a**n)%c
    else:
        return ((power(n//2)**2)*(a**(n%2)))%c
print(power(b))