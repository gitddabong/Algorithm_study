import collections

strs = ["eat","tea","tan","ate","nat","bat"]

anagrams = collections.defaultdict(list)

# step1. word를 문자열로 정렬해서 공백없이 다시 합친 값을 키로 사용 (이렇게 하면 eat, tea, ate 모두 키는 aet가 된다.)
# 그리고 그 키값에다 본래 문자열을 append

# step2. anagrams.values()로 딕셔너리의 값만 가져오고 이를 list로 감싸서 리스트 형태로 만들기
for word in strs:
    # 정렬하여 딕셔너리에 추가
    anagrams[''.join(sorted(word))].append(word)
# print(list(anagrams.values()))
print(anagrams.values())