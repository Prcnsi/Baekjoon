import sys
N,M=map(int,input().split())
arr=[i+1 for i in range(N+1)]

for num in range(M):
    tmp=0
    i, j=map(int, input().split())
    tmp=arr[j-1]
    arr[j-1]=arr[i-1]
    arr[i-1]=tmp
    
for i in range(N):
    print(arr[i],end=' ')