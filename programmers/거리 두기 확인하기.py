# 허용하지 않는 경우 :
# 거리 2 안에 응시자가 있고, 그 응시자에게 향하는 블록 중에 파티션이 없는 경우

from collections import deque

def check(place, x, y):
    dx = [-2,-1,1,2,0,0,0,0,-1,-1,1,1]
    dy = [0,0,0,0,-2,-1,1,2,-1,1,-1,1]
    
    for i in range(12):
        n_x = x + dx[i]
        n_y = y + dy[i]
        
        md = abs(x - n_x) + abs(y - n_y)
        if 0 <= n_x < 5 and 0 <= n_y < 5:
            if place[n_x][n_y] == 'P':
                if md == 1:
                    return True
                else:
                    # 같은 세로열 or 가로열일 경우
                    if x == n_x and y != n_y:
                        tmp = 0
                        if dy[i] > 0:
                            tmp = 1
                        else:
                            tmp = -1
                        if place[x][y+tmp] != 'X':
                            return True

                    elif x != n_x and y == n_y:
                        tmp = 0
                        if dx[i] > 0:
                            tmp = 1
                        else:
                            tmp = -1
                        if place[x+tmp][y] != 'X':
                            return True

                    # 대각위치인 경우 양쪽이 모두 X인지 확인
                    else:
                        if place[x+dx[i]][y] != 'X' or place[x][y+dy[i]] != 'X':
                            return True
            
    return False

def search_case(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and check(place, i, j):
                print(i, j)
                return False
    return True
    
    
def solution(places):
    answer = []
    
    for i, place in enumerate(places):
        print(i)
        if search_case(place):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer