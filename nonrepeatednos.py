n=int(input())
p=list(map(int,input().split()))
count=0
l=[]
for i in range(0,len(p)):
    l.append(p[i])
    if l[i] in p:
            if p.count(l[i])==1 :
                print(l[i],end=" ")

