from collections import Counter
import sys
N=int(input())

target = [int(sys.stdin.readline().strip()) for _ in range(N)]
target.sort()

print(round(sum(target)/N))
print(target[N//2])
count=Counter(target).most_common()
if len(count) == 1:
    print(count[0][0])
elif count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(target[N-1]-target[0])