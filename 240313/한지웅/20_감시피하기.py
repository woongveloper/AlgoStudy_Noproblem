# https://www.acmicpc.net/problem/18428
# 256ms
'''
N은 3이상 6이하로, 매트릭스를 만들고 탐색하는 과정은 어렵지 않은 과정이다.

매트릭스를 생성하고, 이를 탐색하며 선생들의 위치를 담은 리스트를 생성한다.
더불어 학생도 선생도 없는 좌표를 담은 리스트를 생성한다.

이후 아무도 없는 좌표 comb 3을 진행해 장애물을 설치한다. (deepcopy, combinations 활용)
이를 선생의 위치에서 bfs를 진행한다.
combinations list만큼 모두 진행했을 때에도 학생이 탐지되지 않는 경우는 No
위 과정 중 피할 수 있는 경우를 발견한다면, Yes출력 후 반복 중단.
'''
from copy import deepcopy
from itertools import combinations
from collections import deque

di = [-1,1,0,0] #상하좌우
dj = [0,0,-1,1]
def bfs(coord_T, matrix):
    for i in range(len(coord_T)):
        now_i = coord_T[i][0]
        tmp_i = deepcopy(now_i)
        now_j = coord_T[i][1]
        tmp_j = deepcopy(now_j)
        for dir in range(4):
            now_i = deepcopy(tmp_i)
            now_j = deepcopy(tmp_j)
            while True: # 4방향을 탐색
                mv_i = now_i + di[dir]
                mv_j = now_j + dj[dir]
                if N-1<mv_i or 0>mv_i or N-1<mv_j or 0>mv_j: #인덱스를 벗어난 경우
                    break
                if matrix[mv_i][mv_j] == 'X': # 빈칸이라면
                    matrix[mv_i][mv_j] = 'T'
                elif matrix[mv_i][mv_j] == 'S': # 학생이라면
                    return False # 학생 탈출 실패
                elif matrix[mv_i][mv_j] == 'O':
                    break
                now_i = mv_i
                now_j = mv_j
    else:
        return True # 학생 탐지에 실패했으므로 True return

def check(matrix, wall_lst):
    for i in range(len(wall_lst)):
        candidate = wall_lst[i]
        paper = deepcopy(matrix)
        for j in range(3): # 벽 3개를 세운다.
            a,b = candidate[j]
            paper[a][b] = 'O'
        
        can_escape = bfs(coord_T, paper)
    
        if can_escape == False: # 해당 케이스에서 발각되는 경우
            continue
        elif can_escape == True: # 발각되지 않는 경우가 있다면
            return 'YES'
    else:
        return 'NO'

N = int(input())
matrix = []
coord_T = []
coord_empty = []

for i in range(N):
    oneline = list(input().split())
    for j in range(N):
        if oneline[j] == 'X':
            coord_empty.append((i,j))
        elif oneline[j] == 'T':
            coord_T.append((i,j))
    matrix.append(oneline)
    
wall_lst = list(combinations(coord_empty,3))
print(check(matrix,wall_lst))