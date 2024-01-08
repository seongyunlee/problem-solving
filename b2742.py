h,m=map(int,input().split())
print(h if m>=45 else (h-1 if h>0 else 23), m-45 if m>=45 else m+15)