n=int(input())
p=list(map(int,input().split()))
count=0
for i in range(0,len(p)):
    if i==p[i]:
        print(i,end=" ")
        count=count+1
if count==0:
    print("-1")
