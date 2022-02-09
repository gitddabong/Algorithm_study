import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

result = list1 + list2
result.sort()
print(*result, sep = ' ')