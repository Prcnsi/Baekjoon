int_list=[]
for i in range(9):
	n=int(input())
	int_list.append(n)

max=max(int_list)
print(max)
index=int_list.index(max)

print(index+1)