


N = int(input())                                        # 수의 개수 N
num_list = list(map(int, input().split()))              # 숫자들 입력
plus, minus, gob, nanugi = map(int, input().split())    # 연산자 개수 입력

max_num = 987654321     # 최대값 설정
min_num = -987654321    # 최소값 설정

for i in num_list:
    if plus > 0:
        i + (i+1)
    if minus > 0:
        i - (i+1)
    if gob > 0:
        i * (i+1)
    if nanugi > 0:
        i // (i+1)

          




'''
2
5 6
0 0 1 0

30
30

3
3 4 5
1 0 1 0

35
17

6
1 2 3 4 5 6
2 1 1 1

54
-24
'''