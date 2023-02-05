sortList=[]
sum=0
for i in range(5):
    tmp=int(input())
    sum+=tmp
    sortList.append(tmp)
sortList.sort()
print(int(sum/len(sortList)))
print(int(sortList[2]))
