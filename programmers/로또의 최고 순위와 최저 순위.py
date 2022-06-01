def solution(lottos, win_nums):
    answer = []
    
    same = []
    zero_cnt = 0
    for num1 in lottos:
        if num1 == 0:
            zero_cnt += 1
        for num2 in win_nums:
            if num1 == num2:
                same.append(num1)
    same = list(set(same))
    
#     print(same)
#     print(zero_cnt)
    
    # 1위가 6개, 2위가 5개, 3위가 4개, 4위가 5개 ...
    max_point = len(same) + zero_cnt
    min_point = len(same)
    
    answer.append(7 - max(max_point, 1))
    answer.append(7 - max(min_point, 1))
    
    return answer

# 간단한 답
# def solution(lottos, win_nums):
#     cnt = len(set(lottos) & set(win_nums))
#     zero = lottos.count(0)
    
#     return [7-max(cnt+zero,1) ,7-max(cnt,1)]