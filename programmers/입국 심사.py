def check(mid, times):
    cnt = 0
    for time in times:
        cnt += mid // time
        
    return cnt

def solution(n, times):    
    answer = 0
    left = 1
    right = max(times) * n
    mid = (left + right) // 2
    while left <= right:
        cnt = check(mid, times)

        if cnt >= n:
            answer = mid
            right = mid - 1
            mid = (left + right) // 2
        else:
            left = mid + 1
            mid = (left + right) // 2
    
    return answer