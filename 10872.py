# -*- coding: utf-8 -*-
# 재귀함수는 반복문처럼 동작함
def factorial(n):
    fact=1
    if n>0:
        # 한 번 호출할 때마다 조건식에 일치하는지 검사하는 듯
        fact=n*factorial(n-1)
    return fact

N=int(input()) 
print(factorial(N))