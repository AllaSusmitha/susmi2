n,m=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
for i in range (n):
	if m==l[i]:
		print("yes")
		break
else:
	print("no")
