from collections import defaultdict

def solution(phone_book):
    answer = True
    
#     for key in phone_book:
#         for cmp in phone_book:
#             if key == cmp:
#                 continue
            
#             if key == cmp[:len(key)]:
#                 return False
    
#     return True

    nums = defaultdict(int)
    lens = []
    for phone in phone_book:
        lens.append(len(phone))
        nums[phone] = 1

    lens = list(set(lens))
        
    for mobile in phone_book:
        for length in lens:
            temp = mobile[:length]
            if temp == mobile:
                continue

            if nums[temp] == 1:
                return False
    return True