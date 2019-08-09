n=list(map(int,input().split()))
p=n[0:1]
l=n[1:2]
ab = [p[i]*l[i] for i in range(len(p))]
print(*ab)
