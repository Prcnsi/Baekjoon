import sys
N,M=map(int,input().split())
arr=[0 for i in range(N+1)]

for i in range(M):
    # i부터 j까지의 배열에 k 값을 다 넣기
    i,j,k=map(int,sys.stdin.readline().split())
    for val in range(i-1,j):
        arr[val]=k

for i in range(N):
    print(arr[i],end=' ')
