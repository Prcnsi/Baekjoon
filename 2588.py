a=input()
b=input()
a=int(a)
b=int(b)
baek=a//100
ship=a//10-10*baek
ill=a-10*(a//10)

baek_2=b//100
ship_2=b//10-10*baek_2
ill_2=b-10*(b//10)
print(a*ill_2)
print(a*ship_2)
print(a*baek_2)
print(a*b)
