# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
# 1340ms
'''
1~N까지 도시, M개의 단방향 도로
모든 도로의 거리 1
X부터 출발하여 도달할 수 있는 모든 도시 중 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램
'''
'''
BFS정의, 해당 거리의 도시를 append할 리스트 생성
이후 sort, 출력
'''
from collections import deque
def bfs(start_city, dist):
    result = []
    now = start_city
    Q = deque()
    v = [0 for _ in range(city + 1)]
    v[now] = 1
    while True:
        for go in range(len(city_info[now])):
            if v[city_info[now][go]] == 0:
                Q.append(city_info[now][go])
                v[city_info[now][go]] = v[now] + 1
        
        if Q == deque():
            break
        now = Q.popleft()
    check = dist + 1
    for _ in range(1,city+1):
        if v[_] == check:
            result.append(_)
    result.sort()
    if result == []:
        return '-1'
    else:
        return result

city, road, dist, start_city = map(int,input().split())
city_info = [[] for _ in range(city + 1)]

for _ in range(road):
    start, target = map(int,input().split())
    city_info[start] += [target]

result = []
prt_lst = bfs(start_city, dist)
if prt_lst == '-1':
    print('-1')
else:
    for _ in range(len(prt_lst)):
        print(prt_lst[_])