n=int(input())
o=list(map(int,input().split()))
for i in range(0,len(o)):
        if o.count(i)>=2:
            print(i,end=" ")
            
