import sys
N=int(input())
target=[int(sys.stdin.readline().strip()) for _ in range(N)]
# sort에서 reverse True가 내림차순, False가 오름차순으로 디폴트 값 
target.sort()
for i in range(N):
    print(target[i])
