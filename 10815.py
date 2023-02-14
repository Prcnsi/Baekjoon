import sys 
n = int(input()) #sys.stdin.readline()는 input()이랑 정확히 똑같은 뜻으로 input()이 들어가던 자리에 가면 됨!
card = list(map(int, sys.stdin.readline().split())) # 내가 가지고 있는 카드
m = int(input())
check = list(map(int, sys.stdin.readline().split())) # 검사할 카드

card.sort()
def binary_search(card, target, start, end):
    cnt=0
    while start <= end:

        mid = (start + end) // 2 # 이게 card[mid] < target일 때 인덱스 값을 한 칸 뒤로 이동하는 역할이군. 
        if card[mid] == target: # card[mid]는 내가 가지고 있는 값중 중간 값(기준 값)
            return mid
        elif card[mid] < target: # 이게 더 크면 card에 가장 큰 값까지 검사했는데, target 값이 없었다는 뜻이므로, 카드 리스트에 없음
            start = mid + 1
        else: # target 값이 더 크니까 카드의 인덱스 +1해서 큰 쪽으로 감. 이걸 start(검사할 인덱스)가 끝에 도착할 때까지 검사
            end = mid - 1
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')