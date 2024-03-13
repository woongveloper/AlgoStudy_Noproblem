'''
입력 조건
• 첫째 줄에 자연수 N. K가 주어지며, 각 자연수는 공백으로 구분합니다.
  (1 < N <200,1 < K < 1.000)
• 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어집니다. 
  각 행은 이개의 원소로 구성되며 해당위치에 존재하는 바이러스의 번호가 주어지며 공백으로 구분합니다. 
  단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어집니다. 
  또한 모든 바이러스의 번호는 K 이하의 자연수로만 주어집니다.
• N + 2번째 줄에는 S, X, Y가주어지며 공백으로구분합니다. (0 < S < 10,000,1 <X,Y < N)

출력 조건 
• S초 뒤에 (X. Y)에 존재하는 바이러스의 종류를 출력합니다. 
만약 S초 뒤에 해당 위치에 바이러스가존재하지 않는다면, 0을 출력합니다.

'''
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, K = map(int, input().split())

arr = []    # 시험관 NxN에 정보 입력하기
for _ in range(N):
    arr.append(list(map(int, input().split())))

# print(arr)    # [[1, 0, 2], [0, 0, 0], [3, 0, 0]]

S, X, Y = map(int, input().split()) # S초 뒤에, (X, Y)에 존재하는 바이러스의 번호


queue = []  # 빈 큐 만들기

# arr을 순회하면서 0이 아닌 바이러스가 있으면 큐에 추가할것
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            queue.append(arr[i][j]) # 큐에 해당 바이러스 집어넣기

queue.sort()            # 낮은 번호 바이러스부터 나와야하니까 오름차순로 만들어야 함

# print(arr)      # [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
print(queue)    # [1, 2, 3]


## 틀린코드2        
time = 0    # 1초 지날때마다 시간 계산할 변수

while queue:
    virus = queue.pop(0)
    if time == S:
        break
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                arr[ni][nj] = virus
                time += 1
print(arr[X-1][Y-1])
print(arr)

# 이거는 3번 바이러스만 증식함
# 테케는 맞는데 백준은 틀림







## 틀린 코드
# for i in range(N):
#     for j in range(N):
#         if time == S:   # S초가 되면 정지하라
#             break
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 if arr[ni][nj] == 0:
#                     arr[ni][nj] = queue[0]
#                     time += 1
# print(arr)
# print(arr[X-1][Y-1])

# 위에 델타에서 바이러스 1번만 증식하고 2, 3번은 증식도 안함
# 두번째 테케는 또 1만 무한 증식함



'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2
3

3 3
1 0 2
0 0 0
3 0 0
1 2 2
0
'''