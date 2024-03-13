# https://www.acmicpc.net/problem/16234
'''
인구이동은 하루동안 진행된다.
아래의 방법에 따라 인구 이동이 없을 때 까지 지속된다.

국경선을 공유하는 두 나라 인구차이가 L명이상 R명이하라면,
    두 나라가 공유하는 국경선을 하루동안 연다.
위 조건에 따라 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어, 인접한 칸만을 이동할 수 있다면,
    그 나라를 하루동안은 연합이라고 한다.
연합을 이루는 각 칸의 인구수는 (연합의 인구수)/(연합을 이루는 칸)가 된다.
    편의상 소수점은 버린다. (새로 할당한 인구수에 int)
'''
'''
인구 정보를 받은 후, bfs를 통해 연합 영역을 새로 지정  (숫자 1,2, ..)
새로 지정을 완료했다면 이를 활용해 인구수를 구하고, 인구를 새로 할당한다.

이후 새로운 연합이 형성 가능한지를 판단한다.
이후 새로운 연합 영역을 구하고 인구를 할당한다.

이를 변화가 없을 때 까지 반복한다.
'''
'''
정의할 함수
1. 연합을 생성할 bfs함수 (visited활용, 0인경우 탐색하며 숫자 작성,
    숫자는 탐색시 마다 1개씩 올려 연합 구별)
    위 함수가 한번 종료될 때 마다 cnt + 1(날짜)
2. 연합을 구성한 데이터를 바탕으로 인구를 새로 할당하는 함수
3. 위 두개의 함수를 묶어 변화가 없을 때 까지 반복시키는 함수
'''
from collections import deque
from copy import deepcopy

N, mn, mx = map(int,input().split())
# NxN size, mn이상mx이하 차이인 경우 연합 구성
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]

def bfs():
    global matrix
    v = [[0]*(N) for _ in range(N)]
    union_name = 1
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0: #연합 여부를 판단하지 않은 국가라면
                now_i = i
                now_j = j
                v[now_i][now_j] = union_name
                Qi = deque()
                Qj = deque()
                people = matrix[now_i][now_j] # 인구를 세며 연합화 진행
                num_union = 1
                union_lst = [(now_i,now_j)]
                while True:
                    for dir in range(4):
                        mv_i = now_i + di[dir]
                        mv_j = now_j + dj[dir]
                        if 0<=mv_i<=N-1 and 0<=mv_j<=N-1:
                            if v[mv_i][mv_j] == 0 and mn<=abs(matrix[now_i][now_j]-matrix[mv_i][mv_j])<=mx:
                                # 연합여부를 판단하지 않음과 동시에 차이가 조건을 만족하는 경우
                                v[mv_i][mv_j] = union_name
                                Qi.append(mv_i)
                                Qj.append(mv_j)
                                union_lst.append((mv_i, mv_j))
                                people += matrix[mv_i][mv_j]
                                num_union += 1
                    if Qi == deque():
                        divided = int(people/num_union)
                        for k in range(len(union_lst)):
                            union_i = union_lst[k][0]
                            union_j = union_lst[k][1]
                            matrix[union_i][union_j] = divided
                        union_name += 1 # 다음 연합을 구성하기 위한 +1
                        break
                    now_i = Qi.popleft()
                    now_j = Qj.popleft()
            else:
                continue
    return v

def check_day():
    cnt = 0
    tmp = deepcopy(matrix)
    while True:
        after_move = bfs()
        if tmp == after_move:
            return cnt-1
        tmp = deepcopy(after_move)
        cnt += 1

print(check_day())