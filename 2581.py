M=int(input())
N=int(input())
#M<=N - N이 더 크다, 소수 리스트를 찾아야
arr=[True]*(N-M+1)
lastRange=int(N**0.5) # 마지막 범위의 수에 루트를 씌운 것
# 모든 범위 사이의 수를 순회하는 반복문
for num in range(lastRange):
    primeCheck=0
    maxDrain=int((num+N)//(num+M)) # 최대 배수
    # 소수 판단 - 한 수에 대해서 모든 수로 나눠보는 반복문
    for i in range(1,M+num+1):            
        if (num+M)%i==0: # num+N = 시작하는 수
            
            primeCheck+=1

    if primeCheck==2: # 해당 num이 소수라면 그 수만 True, 그 수의 배수는 False로 설정
        arr[num]=True
        for i in range(1,maxDrain): #2
            print(num,len(arr),i)
            arr[num+i*(M+num)]=False

    else: # 해당 num이 소수가 아니라면 그 수도 False 그 배수를 모두 False로 설정
        for i in range(maxDrain):
            arr[num+i*(M+num)]=False
            

primeList=[i+M for i in range(N-M+1) if arr[i] == True]
print(primeList)
print(len(primeList))

print(list(range(40)))
