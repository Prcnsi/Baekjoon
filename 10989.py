import sys
T=int(input())
arr=[0]*10001

for _ in range(T):
    arr[int(sys.stdin.readline())]+=1

for i in range(10001):
    if arr[i]:
        for j in range(arr[i]):
            print(i)