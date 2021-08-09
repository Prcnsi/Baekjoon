int_list=[]
count=0

for i in range(10):
    Get=int(input())
    Get=Get%42
    int_list.append(Get)

int_list=set(int_list)
print(len(int_list))

