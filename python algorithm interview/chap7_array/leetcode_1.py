# # target을 만들 수 있는 두 페어를 찾는 문제
# # 브루트 포스로 풀이
# # 실행시간 3512ms ㅁㅊ; 
# # 뭔가 빠른 방법이 있을 것 같다
# nums = [2,7,11,15]
# target = 9
# success_flag = False

# idx1 = 0
# idx2 = 0

# for i in range(len(nums)-1):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             idx1 = i
#             idx2 = j
#             success_flag = True
#             break
#     if success_flag:
#         break
# print([idx1,idx2])


nums = [2,7,11,15]
target = 9

nums_map = {}
# 키와 값을 바꿔서 딕셔너리로 저장
# 값과 인덱스에 빠르게 접근할 필요가 있으므로 딕셔너리 자료형을 사용.
# {2:0, 7:1, 11:2, 15:3}
for i, num in enumerate(nums):
    nums_map[num] = i

# 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
for i, num in enumerate(nums):
    # num과 합을 만들 수 있는 페어가 있고 i가 페어의 인덱스가 아닌 경우에 찾기완료 (중복된 숫자가 들어올 수도 있으므로 검사)
    # in 키워드로 딕셔너리를 검색하면 키를 검색한다.
    if target - num in nums_map and i != nums_map[target-num]:
        print([i, nums_map[target-num]])
        break

