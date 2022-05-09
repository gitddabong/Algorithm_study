def DFS(L):
    global cnt, res
    if L == len(num):
        if len(res) > len(num):
            res = res[2:]   # pop, slicing 둘 다 O(N). pop(0)을 2번 하면, 2N이니까 슬라이싱 사용. pop(0)을 O(1)로 하려면 deque사용하면 됨
        print("".join(res))
        cnt += 1
        return
    a = int(num[L])
    b = int("".join(num[L:L+2]))
    if a == 0:
        return
    if 0 < a < 10:
        res.append(chr(a+64))
        # res.append(a)
        DFS(L+1)
        res.pop()
    if 9 < b < 27:
        res.append(chr(b+64))
        # res.append(b)
        DFS(L+2)
        res.pop()
    
if __name__ == "__main__":
    num = list(str(input()).rstrip())
    res = []
    cnt = 0
    DFS(0)
    print(cnt)



# # 25114

# nums = input()
# # chr(65) == A

# cnt = 0
# def dfs(_str, result = []):
#   global cnt
#   if _str == "":
#     print("".join(result))
#     cnt += 1
#     return

#   for j in range(1, 3):
#     if len(_str) >= j:
#       asc_code = int(_str[:j])
#       if 1 <= asc_code <= 26:
#         result.append(chr(asc_code + 64))
#         dfs(_str[j:], result)
#         result.pop(-1)
#       elif _str[0] == '0':
#         return

# dfs(nums)
# print(cnt)





