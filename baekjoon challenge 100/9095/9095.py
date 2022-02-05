import sys
# input = sys.stdin.readline()

T = int(sys.stdin.readline())

count = 0
def get_count(n):
    global count

dp = [0,1,2,4]
for i in range(4, 12):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for _ in range(T):
    num = int(sys.stdin.readline())
    
    print(dp[num])