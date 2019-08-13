n=int(input())
l =list(map(int,input().split()))
l.sort()
s=[]
for i in range (len (l) -1):
    if l[i] == l[i+1]:
        s.append(l[i])
    #elif print("unique"):
        if l[i] in s:
            if s.count(l[i])==1 :
                print(l[i],end=" ")
if s.count(l[i])==0:
    print("unique")




