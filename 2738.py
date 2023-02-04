N,M = map(int, input().split())
A_ = [ 0 for i in range(M*N)]
B_ = [ 0 for i in range(M*N)]

for i in range(1):
    tmp=0 # row number M
    for i in range(N): #M
        A_set=list(map(int,input().split()))
        A_[tmp:tmp+N]=A_set
        tmp+=M # input the next line

for i in range(1):
    tmp=0 # row number M
    for i in range(N): #M
        B_set=list(map(int,input().split()))
        B_[tmp:tmp+N]=B_set
        tmp+=M # input the next line

result=[A_[i]+B_[i] for i in range(M*N)]
K=0
if M==0 or N==0:
    print(0)
else:
    for i in range(N):
        for j in range(M):  
            print(result[j+K], end=" ")
        K+=M
        if i==M-1 and j==N-1:
            pass
        else:
            print()