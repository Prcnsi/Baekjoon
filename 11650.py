import sys
N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
    
# sort()함수는 key 속성을 통해 정렬 기준 설정 가능
# lambda 함수는 입력함수로 (labda 입력: 출력)형태로 사용
# key 함수에 함수를 넘겨주면 우선순위가 정해짐
arr.sort(key=lambda x: (x[0],x[1]))


for i in arr:
    print(i[0],i[1])