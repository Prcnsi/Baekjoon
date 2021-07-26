N=int(input())
array=list(map(int,input().split()))
Y_Price=M_Price=0
for i in array:
    Y_Price+=(i//30+1)*10
    M_Price+=(i//60+1)*15
if(Y_Price>M_Price):
    print('M',M_Price)
elif(Y_Price<M_Price):
    print('Y',Y_Price)
else:
    print('Y','M',M_Price)