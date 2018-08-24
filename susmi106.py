n,m=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
sum=0
for i in range (n):
	if m==l[i]:
		sum=sum+1
print sum
		
