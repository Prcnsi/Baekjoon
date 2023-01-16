target_set=set(range(1,31))
input_set=set()

for i in range(28):
    value=int(input())
    input_set.add(value)

diff=list(target_set-input_set)
print(min(diff))
print(max(diff))
