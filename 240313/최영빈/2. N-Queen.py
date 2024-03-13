'''
8*8 체스보드에 8개의 퀸을 서로 공격하지 못하게 놓는 문제는 잘 알려져 있는 문제이다. 
퀸은 같은 행, 열, 또는 대각선 위에 있는 말을 공격할 수 있다. 

N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇 가지가 있을까?

N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 한가지 경우를 출력하는 프로그램을 작성하시오.

입력조건
첫째 줄에 N이 주어진다. N은 8, 26, 213, 2012, 99991, 99999중 하나이다.

출력조건
N개의 줄을 출력해야 한다. 
i번째 줄에는 하나의 정수를 출력해야 하고, 이 정수는 i번째 행에 있는 퀸이 있는 열의 번호이다.
'''
# 8방향 설정
di = [0, 1, 0, -1, 1, 1, -1, -1]
dj = [1, 0, -1, 0, 1, -1, -1, 1]

N = int(input())    # 보드판 크기 입력

arr = [[0] * N for _ in range(N)]
  
counts = 0

for i in range(N):
    for j in range(N):
        if counts < 9:
            arr[i][j] == 1
            counts += 1
        for p in range(N):
            for q in range(N):
                if arr[p][q] == 1:
                    for k in range(1, N):
                        for l in range(8):
                            ni = i + di[l] * k
                            nj = i + dj[l] * k
                            if 0 <= ni < N and 0 <= nj < N:
                                if arr[ni][nj] == 1:
                                    break
print(arr)  # 왜 다 0으로 채워지지?

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            print(j)



'''
입력
8
출력
3
6
8
1
4
7
5
2
'''