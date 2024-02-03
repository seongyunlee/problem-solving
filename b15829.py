input()
pow = lambda x: 1 if x==0 else 31*pow(x-1)%1234567891
print(sum([((ord(x)-96)*(pow(i)))%1234567891 for i,x in enumerate(input())])%1234567891)