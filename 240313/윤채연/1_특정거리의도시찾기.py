"""
백준_18352번 : 특정 거리의 도시 찾기 (BFS 알고리즘 활용)
N: 도시의 개수
M: 도로의 개수
k: 거리 정보
X: 출발 도시의 번호

--> 따라서, N은 노드의 수 M은 간선의 수
"""

# deque를 사용하기 위해
from collections import deque
n, m, k, x = map(int, input().split())

# 데이터를 처음 0번째부터 넣지 않고 1번쨰부터 넣기 떄문에
graph = [[] for _ in range(n+1)]

# 도로의 개수(M)번 도로의 연결 정보를 받아 graph에 삽입
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
# 방문하지 않은 도시는 -1 이기에
dis = [-1] * (n+1)

# 시작 도시 -> 시작 도시 거리는 0
dis[x] = 0

# BFS(너비우선 탐색)을 위해 deque()를 사용
q = deque()
q.append(x)

# q가 빌 때까지 반복
while q:

    # now에는 1이 담기고, q는 비게 된다
    now = q.popleft()

    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next in graph[now]:

        # 아직 방문하지 않은 도시라면,
        if dis[next] == -1:

            # 최단 거리 갱신
            # 현재 도시와 출발 도시 사이의 거리 + 1
            dis[next] = dis[now] + 1
            q.append(next)

# 출발 도시로부터의 최단 거리가 K인 도시가 존재하지 않는다면,
# -1을 출력하기 위해 check 변수를 False로 초기화

check = False
for i in range(1, n+1):

    # 도시들 간에 최단 거리를 확인하여 K와 동일하면 그 도시를 출력
    if dis[i] == k:
        print(i)

        # 최단거리가 K인 도시가 존재한다면, check를 True로 바꿔주어 -1이 출력되지 않도록 함
        check = True

# 만약, 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)