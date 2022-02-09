import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

dict = defaultdict(int)
for num in list1:
    dict[num] += 1

for num in list2:
    dict[num] += 1

count = 0
for num, val in dict.items():
    if val != 1:
        count += 1

print(n + m - (count*2))