N=int(input())
arr=list(map(int, input().split()))
target=int(input())
cnt=0

for i in range(N):
    if arr[i]==target:
        cnt+=1

print(cnt)