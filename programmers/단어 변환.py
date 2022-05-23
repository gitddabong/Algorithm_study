import sys
sys.setrecursionlimit(10 ** 9)

def check(temp, target):
    cnt = 0
    for i in range(len(temp)):
        if temp[i] != target[i]:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False

def dfs(temp, target, words, visited, cnt = 0):
    if temp == target:
        return cnt

    result = 0
    for i in range(len(words)):
        if not visited[i] and check(temp, words[i]):
            visited[i] = True
            result = dfs(words[i], target, words, visited, cnt + 1)
            visited[i] = False
    
    return result

def solution(begin, target, words):
    answer = 0
    
    visited = [False] * len(words)
    answer = dfs(begin, target, words, visited)
    
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))