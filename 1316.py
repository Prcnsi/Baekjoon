N=int(input())
cnt_num=0
for i in range(N):
    word=input()
    i=0 # aple i=2
    # 연속된 중복 문자 제거
    while(len(word)!=i+1):
        # 현재 인덱스와 다음 인덱스의 값이 같으면(중복문자) 인덱스를 1 더하지 않고, 중복문자를 뺴고 단어를 합친다.
        if word[i]==word[i+1]:
            word=word[:i]+word[i+1:]
        else:
            i+=1
    print(word)
    # 연속된 중복 문자를 제거했는데 중복 원소가 있으면, 떨어져 있는 중복 원소 이므로 그룹 단어가 아님
    word_set=set(word)
    if len(word_set)==len(word):
        cnt_num+=1
print(cnt_num)
