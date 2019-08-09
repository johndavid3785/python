n=list(map(int,input().split()))
n.sort(reverse=True)
l=[]
l1=[]
l.append(n)
l.reverse()
print(''.join(map(str,*l)))
