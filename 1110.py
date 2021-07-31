N=int(input())
confirm=N
count=0
new_int=0
count=0

while 1:
    new_ill=N//10+N%10
    new_int=(N%10)*10+new_ill%10
    count+=1
    N=new_int
    if new_int==confirm:
        print(count)
        break