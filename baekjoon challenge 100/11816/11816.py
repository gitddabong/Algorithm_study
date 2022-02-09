import sys

num = sys.stdin.readline().rstrip()

if num[0] == '0':
    # 16진수
    if num[1] == 'x':
        print(int(num, 16))
    # 8진수
    else:
        print(int(num, 8))
# 10진수
else:
    print(int(num, 10))