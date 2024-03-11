# https://www.acmicpc.net/problem/18405
# 경쟁적 전염
# 216ms

'''
NxN 크기의 시험관, 특정한 위치엔 바이러스 존재 할 수 있다.
바이러스의 종류는 1~K까지 존재
시험관의 바이러스는 bfs 규칙에 따라 이동, 단 매 초마다 번호가 낮은 종류의 바이러스 먼저 증식한다.
    바이러스 증식 과정에서 다른 곳에 바이러스가 존재한다면, 그곳은 증식할 수 없다.
S초가 지난 후 X,Y에 존재하는 바이러스의 종류를 출력하는 프로그램 작성할 것.
'''
'''
가장 왼쪽 위 (1,1)이므로, Idx 주의
'''
from copy import deepcopy

di = [-1,1,0,0] # 상하좌우
dj = [0,0,-1,1]

def bfs(S,X,Y):
    global matrix
    virus = deepcopy(virus_lst)
    for sec in range(S):
        if matrix[X][Y] != 0:
            break
        new_vir = []
        for vir in range(len(virus)):
            vir_name = virus[vir][0]
            vir_i = virus[vir][1]
            vir_j = virus[vir][2]
            for dir in range(4):
                mv_i = vir_i + di[dir]
                mv_j = vir_j + dj[dir]
                if 0<=mv_i<=N-1 and 0<=mv_j<=N-1:
                    if matrix[mv_i][mv_j] == 0:
                        matrix[mv_i][mv_j] = vir_name
                        new_vir.append((vir_name, mv_i, mv_j))
        virus = deepcopy(new_vir)
    print(matrix[X][Y])

N, K = map(int,input().split())
# 시험관 사이즈 N
# 바이러스의 개수 K

matrix = []
virus_lst = []
for k in range(N):
    check = list(map(int,input().split()))
    for l in range(N):
        if check[l] != 0: # 바이러스인 경우
            virus_lst.append((check[l],k,l)) # 바이러스 종류, i좌표, j좌표 입력
    matrix.append(check)
virus_lst.sort()
S,X,Y = map(int,input().split())
X = X-1
Y = Y-1
bfs(S,X,Y)
