orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]


from collections import defaultdict

def addCount(dic, li, limit, depth = 0, result = [], idx = 0):
    if depth == limit:
        dic["".join(sorted(result))] += 1
        return
    
    for i in range(idx, len(li)):
        result.append(li[i])
        addCount(dic, li, limit, depth + 1, result, i + 1)
        result.pop()

def solution(orders, course):
    answer = []
    
    dic = defaultdict(int)
    for order in orders:
        for i in course:
            if i <= len(order):            
                addCount(dic, list(order), i)
            
    max_cnts = defaultdict(int)
    result = defaultdict(list)
    
    for key, value in dic.items():
        # key = "AB", value = 3
        if max_cnts[len(key)] < value:
            max_cnts[len(key)] = value
            result[len(key)].clear()
            if value >= 2:
                result[len(key)].append(key)
            continue
        
        if max_cnts[len(key)] == value:
            if value >= 2:
                result[len(key)].append(key)
                
    for piece in course:
        answer += result[piece]

    answer.sort()
    
    return answer

print(solution(orders, course))