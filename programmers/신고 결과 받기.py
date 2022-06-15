# from collections import defaultdict

# def solution(id_list, report, k):
#     answer = []
    
#     report = list(set(report))
    
#     reported_list = defaultdict(list)
#     report_cnt = defaultdict(int)
#     for text in report:
#         user, reported = text.split()
#         report_cnt[reported] += 1
        
#         reported_list[user].append(reported)
                
#     for id in id_list:
#         cnt = 0
#         for user in reported_list[id]:
#             if report_cnt[user] >= k:
#                 cnt += 1
#         answer.append(cnt)
    
#     return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

def solution(id_list, report, k):
    # 유저아이디는 해쉬테이블(딕셔너리)로 {아이디:신고횟수} 구조로 만들어 놓자
    dict = {}
    for x in id_list:
        dict[x] = 0
        
    # report->set으로 동일 인물 동일 신고 제외
    report = set(report)
    
    # report[i].split()으로 분리 되는지, 되면 report[i][1]의 신고 수 += 1 카운팅 해줌(딕셔너리)
    for i in report:
        a, b = i.split()
        dict[b] += 1
    
    # 딕셔너리 value값이 k보다 큰 id를 result에 따로 저장한다.
    result = []
    
    for item in dict.items():
        if item[1] >= k:
            result.append(item[0])
    
    answer = [0] * len(id_list)
    for i in report:
        a, b = i.split()
        for name in result:
            if name == b:
                answer[id_list.index(a)] += 1
    
    return answer

print(solution(id_list, report, 2))