import sys

input = sys.stdin.readline()
num = int(input())

slash = 2
while num > 1:
    if num % slash == 0:
        print(slash)
        num /= slash
    else:
        slash += 1