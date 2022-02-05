import sys

N = int(sys.stdin.readline())
nums = sys.stdin.readline().rstrip()

sum = 0
for num in nums:
    sum += int(num)

print(sum)