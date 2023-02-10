N=int(input())
arr=[[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    # x,y d입력 받기
    x,y=map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            # print('좌표',i,j)
            arr[i][j]=1

area=0
for _ in range(100):
    # print(arr[_].count(1))
    area+=arr[_].count(1)
print(area)