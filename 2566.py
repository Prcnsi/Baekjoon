matrix=[]
for row in range(9):
    row=list(map(int,input().split()))
    matrix.append(row)

tmp=0
a=0
b=0
for row in range(9):
    for col in range(9):
        if tmp<matrix[row][col]:
            tmp=matrix[row][col]
            a=row
            b=cola

print(tmp)
print(a+1,b+1)