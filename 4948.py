import sys
# 이거 다 풀고 다른 사람들은 입력을 어떻게 처리했는지 확인하기
while(1):
    N=int(float(sys.stdin.readline()))
    if N==0:
        break

    arr=[False,False]+[True for i in range(2*N+1)]
    for x in range(int((2*N)**0.5)+1):
        if arr[x]==True:
            for i in range(x+x,2*N+1,x):
                arr[i]=False
    result=[x for x in range(N+1,2*N+1) if arr[x]==True]
    print(len(result))
