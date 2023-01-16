hour,minute=map(int,input().split())
spent_time=int(input())

spent_minute=minute+spent_time
plus_time=(minute+spent_time)//60

# 조리시간(현재시간 + 조리시간)을 더 했을 때 1시간이 넘어가면
if spent_minute>=60:
    # 조리시간이 1시간을 넘어가면 시간 +1하고 분-60 하기, 이때 시간+1을 해야하는데 현재 23시이면
    if hour+plus_time>=24:
        # 이 조건문에 걸리는 함수는 plus_time이 최소 1이니까 plus_time-1시라고 해도 됨
        print(hour+plus_time-24,spent_minute%60)
    else:
        print(hour+plus_time,spent_minute%60) 
else:
    # 시간과 분을 더했을 때 60분을 넘지 않으면, 시간은 그대로 분만 더해서 출력
    if hour>=24:
        hour=hour-24
    print(hour,spent_minute)


# ----------------------------------------------------------------------------------------------
# 아래 주석 처리 내용은 디버깅시에 사용한 Test Case Builder 함수
# ----------------------------------------------------------------------------------------------
# from random import randint

# def Oven(hour,minute,spent_time):
#     # hour,minute=map(int,input().split())
#     # spent_time=int(input())

#     spent_minute=minute+spent_time
#     plus_time=(minute+spent_time)//60

#     # 조리시간(현재시간 + 조리시간)을 더 했을 때 1시간이 넘어가면
#     if spent_minute>=60:
#         # 조리시간이 1시간을 넘어가면 시간 +1하고 분-60 하기, 이때 시간+1을 해야하는데 현재 23시이면
#         # 이 알고리즘의 문제는 hour가 23일 때만 고려하고 print 문을 짜서 틀림 
#         if hour+plus_time>=24:
#             # 이 조건문에 걸리는 함수는 plus_time이 최소 1이니까 plus_time-1시라고 해도 됨
#             print('result: ',hour+plus_time-24,spent_minute%60)
#         else:
#             print('result: ',hour+plus_time,spent_minute%60) 
#     else:
#         # 시간과 분을 더했을 때 60분을 넘지 않으면, 시간은 그대로 분만 더해서 출력
#         if hour>=24:
#             hour=hour-24
#         print('result: ',hour,spent_minute)
#     return 0

# def test_excute():
#     for i in range(100):    
#         hour=randint(0,23)
#         minute=randint(0,59)
#         spent_time=randint(0,1000)
#         print('Test Case',i,'hour:',hour,'minute:',minute,'spent_time',spent_time)
#         Oven(hour,minute,spent_time)
#         #print('\n')
#     return 0

# test_excute()