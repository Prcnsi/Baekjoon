N,cut=map(int,input().split())
line=input()
line=line.split(sep=' ')   
target=[]
for i in range(N):
    tmp=int(line[i])
    target.append(tmp)
target.sort(reverse=True)
print(target[cut-1])
