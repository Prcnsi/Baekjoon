# -*- coding: utf-8 -*-
a,b=input().split()

# [::-1]은 역순으로 출력
a=int(a[::-1])
b=int(b[::-1])

if a>b:
    print(a)
else:
    print(b)