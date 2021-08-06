N=int(input())
int_list=list(map(int,input().split()))

max=int_list[0]
low=int_list[0]
i=1

for i in range(len(int_list)):
	if max < int_list[i]:
		max=int_list[i]
	if low > int_list[i]:
		low=int_list[i]

print(low,max)