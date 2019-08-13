n=int(input())
l =list(map(int,input().split()))
l.sort()
z=[]
for i in range (len (l) -1):
    if l[i] == l[i+1]:
        z.append(l[i])
    #elif print("unique"):
        if l[i] in z:
            if z.count(l[i])==1 :
                print(l[i],end=" ")
if z.count(l[i])==0:
    print("unique")




