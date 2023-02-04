M = int(input())
lis = [False,False]+[True for i in range(2,M+1)] # 시작 범위에 관계 없이 마지막 범위까지 리스트를 만들고, 0-1번째 인덱스는 False처리
big = int(M** 0.5) 
for x in range(2, big+1):
    if lis[x] == True:
        for y in range(x+x , M+1, x) : 
            lis[y] = False

result = [x for x in range(M+1) if lis[x]== True] # 그리고 시작 범위에 대한 처리는 결과를 출력할 때 앞부분을 시작 범위로 잘라버리기 
prime_fact=[]
while(M!=1):
    for i in range(len(result)):
        if M%result[i]==0:
            prime_fact.append(result[i])
            M//=result[i]
prime_fact.sort()

for i in range(len(prime_fact)):
    print(prime_fact[i])
