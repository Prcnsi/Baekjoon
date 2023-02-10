N=str(input())
arr=[]
for _ in range(len(N)):
    arr.append(N[_])

arr.sort(reverse=True)
result=''
for _ in range(len(N)):
    result+=str(arr[_])

print(result)