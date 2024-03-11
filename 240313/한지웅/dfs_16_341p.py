# 연구소
# https://www.acmicpc.net/problem/14502
# 832ms

'''
바이러스 유출, 확산을 막기 위한 벽 세워야함.
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 퍼져나간다.(bfs)
벽을 3개 세울 때, 바이러스가 퍼질 수 없는 영역의 수(안전영역) 최대값을 구할 것.
'''
'''
1.기둥을 세우는 함수 정의
2.bfs함수 정의
3.안전구역을 세는 함수
'''
'''
64C3을 계산해보면 , 벽을 세우는 최대의 경우의 수는 41664 (가능)
벽을 세울 수 있는 위치 3개를 고르고, 그 상태에서 bfs진행, 이후 최대 결과값을 지속 갱신.
'''
from itertools import combinations
from copy import deepcopy
from collections import deque

di = [-1,1,0,0] #상하좌우
dj = [0,0,-1,1]

def bfs(matrix):
    global max_safe
    for virus_idx in range(len(virus_lst)):
        now_i = virus_lst[virus_idx][0]
        now_j = virus_lst[virus_idx][1]
        Qi = deque()
        Qj = deque()
        while True:
            for dir in range(4):
                mv_i = now_i + di[dir]
                mv_j = now_j + dj[dir]
                if 0<=mv_i<=N-1 and 0<=mv_j<=M-1:
                    if matrix[mv_i][mv_j] == 0:
                        Qi.append(mv_i)
                        Qj.append(mv_j)
                        matrix[mv_i][mv_j] = 1
            if Qi == deque():
                break
            now_i = Qi.popleft()
            now_j = Qj.popleft()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                cnt += 1
    if max_safe < cnt:
        max_safe = cnt

N, M = map(int,input().split())
matrix = []
road_lst = []
virus_lst = []
for _ in range(N):
    one_line = list(map(int,input().split()))
    for k in range(M):
        if one_line[k] == 0:
            road_lst.append((_,k))
        elif one_line[k] == 2:
            virus_lst.append((_,k))
    matrix.append(one_line)

wall = list(combinations(road_lst,3))

max_safe = -1
for i in range(len(wall)):
    copy_matrix = deepcopy(matrix)
    build_wall = wall[i]
    for k in range(3):
        copy_matrix[build_wall[k][0]][build_wall[k][1]] = 1
    bfs(copy_matrix)
print(max_safe)