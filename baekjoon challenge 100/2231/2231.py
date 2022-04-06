
# inserted = input()

# n = int(inserted)
# numList = list(map(int, inserted))
# loop = len(numList)

# result = 10000001

# for i in range(min(loop * 9, n)):
#     # 테스트 케이스 만들기
#     case = n - i - 1
#     case_list = list(map(int, str(case)))
    
#     sum = 0
#     # 각 자리의 총합
#     for j in range(len(case_list)):
#         sum += case_list[j]

#     if n == case + sum:
#         result = min(result, case)

# if result == 10000001:
#     print("0")
# else:
#     print(result)



# 68ms
import sys
input = sys.stdin.readline

n = int(input())

# 생성자가 존재할 수 있는 범위는 n - (9 * 각 자리수)부터 n까지.

result = float('inf')
for i in range(min(n, 9*len(str(n)))):
    const = n - i - 1
    
    temp = const + sum(list(map(int, str(const))))
    if temp == n:
        result = min(result, const)

if result == float('inf'):
    print(0)
else:
    print(result)

