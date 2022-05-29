# -*- coding: utf-8 -*-
S=str(input())
alphabets="abcdefghijklmnopqrstuvwxyz"
result=0


for i in alphabets:
    if i in S:
        print(S.find(i))
    else:
        print("-1")
   

