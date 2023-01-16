a,b,c=map(int, input().split())
input_set=set([a,b,c])

if len(input_set)==1:
    print(10000+a*1000)
elif len(input_set)==2:
    if a==b:
        print(1000+a*100)
    elif a==c:
        print(1000+a*100)
    else:
        print(1000+c*100)
elif len(input_set)==3:
    print(max(input_set)*100)