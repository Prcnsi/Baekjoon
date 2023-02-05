N=int(input())
sortList=[]
for i in range(N):
    tmp=int(input())
    sortList.append(tmp)

sortList.sort()
for i in range(N):
    print(sortList[i])