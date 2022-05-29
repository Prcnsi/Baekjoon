# -*- coding: utf-8 -*-
# Python upper을 이용해 문자열을 모두 대문자로 변환
words=input().upper()
unique_words=list(set(words))

cnt_list=[]
for i in unique_words:
    # 입력 받은 문자열에서 특정 단어의 개수를 count로 세어줌
    cnt=words.count(i)
    cnt_list.append(cnt)
    
# max(cnt_list)에서 빈도의 최댓값이 2개 이상이면 '?' 출력
if cnt_list.count(max(cnt_list))>1:
    print('?')
else:
    max_index=cnt_list.index(max(cnt_list)) # 알파벳의 개수가 가장 많은 알파벳의 인덱스를 저장해서
    print(unique_words[max_index]) # 그 인덱스에 해당하는 문자를 출력