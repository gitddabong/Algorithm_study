# from collections import defaultdict
# from itertools import combinations

# def multiply(li):
#     result = 1
#     for num in li:
#         result *= num
#     return result

# def solution(clothes):
#     answer = 0
#     answer += len(clothes)
    
#     pitting = defaultdict(list)
#     for name, option in clothes:
#         pitting[option].append(name)
    
#     cnt_list = []
#     for key, val in pitting.items():
#         cnt_list.append(len(val))
    
#     if len(cnt_list) >= 2:
#         for i in range(2, len(cnt_list)+1):
#             combi = list(combinations(cnt_list, i))
#             for tuple in combi:
#                 answer += multiply(tuple)
    
#     return answer

from collections import defaultdict

def solution(clothes):
    pitting = defaultdict(int)
    for cloth, type in clothes:
        pitting[type] += 1
    
    answer = 1
    for key, val in pitting.items():
        answer *= val + 1
    
    return answer - 1