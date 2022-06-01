from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    report = list(set(report))
    
    reported_list = defaultdict(list)
    report_cnt = defaultdict(int)
    for text in report:
        user, reported = text.split()
        report_cnt[reported] += 1
        
        reported_list[user].append(reported)
                
    for id in id_list:
        cnt = 0
        for user in reported_list[id]:
            if report_cnt[user] >= k:
                cnt += 1
        answer.append(cnt)
    
    return answer