import collections

def solution(s):
    answer = []
    
    s = s.replace("{", "")
    s = s.replace("}", "")
    
    li = list(s.split(","))
    
    counts = collections.Counter(li)
    sorted_li = counts.most_common()

    for num, count in sorted_li:
        answer.append(int(num))
    
    return answer