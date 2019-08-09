o=int(input())
n=list(map(int,input().split()))
n.sort(reverse=True)
l=[]
l.append(n)
print('->'.join(map(str,*l)))
