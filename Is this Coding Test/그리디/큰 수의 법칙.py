n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

first = nums[-1]
second = nums[-2]

# # 반복문으로 푸는 방법 O(n)
# cnt = 0
# total = 0
# for _ in range(m):
#   if cnt == k:
#     total += second
#     cnt = 0
#   else:
#     total += first
#     cnt += 1

# 수열의 연산 횟수를 계산하여 푸는 방법 O(1)
sec_cnt = m // (k + 1)
fst_cnt = m - sec_cnt

total = fst_cnt * first + sec_cnt * second

print(total)
