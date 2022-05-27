# -*- coding: utf-8 -*-
# 전체 숫자 집합 생성
all_num=list(range(100,1000))
one_num=list(range(100))
result_num=[]

# 한 수를 구하고
for num in all_num:
    num=str(num)
    if int(num[2])-int(num[1])==int(num[1])-int(num[0]):
        one_num.append(int(num))

a=int(input()) # 값을 입력 받아서

for i in range(1,len(one_num)): # 한 수를 반복문 돌면서 a 이하의 한수 저장
    if a>=one_num[i]:
        result_num.append(one_num[i])

print(len(result_num))