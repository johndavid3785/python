o=int(input())
n=list(map(int,input().split()))
n.reverse()
l=[]
l.append(n)
print('->'.join(map(str,*l)))
