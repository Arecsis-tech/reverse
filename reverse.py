n=int(input())
a=list(map(int,input().split()))
r=[]
for i in range(n):
    if a[i]!=0:
        r.append(a[i])
    if a[i]==0:
        r.reverse()
        r.append(0)
for i in range(n):        
    print(r[i],end=" ")
