# -*- coding: utf-8 -*-
# ��ü ���� ���� ����
all_num=list(range(100,1000))
one_num=list(range(100))
result_num=[]

# �� ���� ���ϰ�
for num in all_num:
    num=str(num)
    if int(num[2])-int(num[1])==int(num[1])-int(num[0]):
        one_num.append(int(num))

a=int(input()) # ���� �Է� �޾Ƽ�

for i in range(1,len(one_num)): # �� ���� �ݺ��� ���鼭 a ������ �Ѽ� ����
    if a>=one_num[i]:
        result_num.append(one_num[i])

print(len(result_num))