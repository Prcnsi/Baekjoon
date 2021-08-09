N=int(input())
avg=list(map(float,input().split()))
stand=avg[0]
new_avg=0
for i in range(N):
    #최댓값 구하기
    if stand<avg[i]:
        stand=avg[i]

#새로운 평균 구하기
for i in range(N):
    avg[i]=(avg[i]/stand)*100
    new_avg+=avg[i]

print(new_avg/N)