'''
arr에 선생님, 학생을 집어넣고
장애물 3개의 위치를 골라서
3개를 다 설치하고 선생님들 델타로 상하좌우 뒤져서 학생이 안나오면 ans를 YES로 바꾼다.

'''
dp = [0, 1, 0, -1]
dq = [1, 0, -1, 0]


N = int(input())    # 복도의 크기

arr = [list(input().split()) for _ in range(N)]    # 복도 입력

ans = 'NO'  # 기본 출력은 NO로 설정, 차후 막을 수 있게 된다면 YES로 바꿀 것

# num_x = 0   # X가 적힌 위치의 개수 (장애물이 설치가능한 곳)
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 'X':
#             num_x += 1

for i in range(N):
    for j in range(N):
        for l in range(3):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
            for p in range(N):
                for q in range(N):
                    for a in range(1, N):
                        for b in range(4):
                            if arr[p][q] == 'T':
                                np = p + dp[b] * a
                                nq = q + dq[b] * a
                                if 0 <= np < N and 0 <= nq < N:
                                    if arr[np][nq] != 'S':
                                        ans = 'YES'
                                    if arr[np][nq] == 'S':
                                        ans = 'NO'
print(ans)


  

'''
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
YES

4
S S S T
X X X X
X X X X
T T T X
NO
'''