# -*- coding: utf-8 -*-
# Python upper을 이용해 문자열을 모두 대문자로 변환
A,B,C=map(int,input().split())

diff=0
N=1
#while(1):
#    prev_diff=diff
#    if A+N*B<C*N: # 생산 비용보다 수입이 더 커지면
#        print(N) #그때의 노트북 개수 N을 출력
#        break
#    else:
#        diff=(A+N*B)-(C*N)
    
#    if prev_diff>diff: # 총생산비용 - 총수입 이 줄어드면 정상
#        pass
#    else:
#        if N==1:
#            pass
#        else:
#            print('-1') # 차이가 줄어들지 않는다면 적자이기 때문에 -1 출력
#            break
#    N+=1    

if B>=C:
    print('-1')
else:
    diff=C-B
    print(A//diff+1)
