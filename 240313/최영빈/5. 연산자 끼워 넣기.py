def dfs(start, num):
    global max_num, min_num, plus, minus, gob, nanugi
    
    if start == N:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    
    if plus > 0 :
        plus -= 1
        now_num = num + num_list[start]
        dfs(start+1, now_num)
        plus += 1

    if minus > 0 :
        minus -= 1
        now_num = num - num_list[start]
        dfs(start+1, now_num)
        minus += 1

    if gob > 0 :
        gob -= 1
        now_num = num * num_list[start]
        dfs(start+1, now_num)
        gob += 1

    if nanugi > 0:
        if num < 0:
            nanugi -= 1
            now_num = -(abs(num) // num_list[start])
            dfs(start + 1, now_num)
            nanugi += 1
        else:
            nanugi -= 1
            now_num = num // num_list[start]
            dfs(start + 1, now_num)
            nanugi += 1


N = int(input())                                        # 수의 개수 N
num_list = list(map(int, input().split()))              # 숫자들 입력
plus, minus, gob, nanugi = list(map(int, input().split()))    # 연산자 개수 입력

max_num = -1000000000   # 최대값 설정
min_num = 1000000000    # 최소값 설정

dfs(1, num_list[0])

print(max_num)
print(min_num)


# 시간초과


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