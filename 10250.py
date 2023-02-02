T=int(input())
for i in range(T):
    H,W,N=map(int,input().split())
    if N%H == 0:
        # ex 6층(행), 12호수(열)인데서 18번째 손님은 603호 배정
        row=N//H
        print(100*H+row)
    else:
        row=N%H # 행, 층수
        col=(N//H)+1 # 열, 호수 (열 개수+1 == 호수)
        print(row*100+col)