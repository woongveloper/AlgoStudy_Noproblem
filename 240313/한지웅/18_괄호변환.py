'''
진행 방향
1. 옳은 것인지 균형있는 것인지 판단하는 함수
2. 이를 기반으로 solution 재귀
'''
def check_right(lst):
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def make_uv(lst):
    u = ''
    v = ''
    cnt_r = 0
    cnt_l = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            cnt_l += 1
            u += lst[i]
        elif lst[i] == ')':
            cnt_r += 1
            u += lst[i]
        if cnt_r == cnt_l:
            if i != len(lst)-1:
                v += lst[i+1:]
            return u,v

def solution(p):
    result = ''
    if p == '':
        return ''
    u,v = make_uv(p)
    if check_right(u) == True:
        result += u + solution(v)
        return result
    else:
        result += '(' + solution(v) + ')'
        tmp = u[1:-1]
        for i in range(len(tmp)):
            if tmp[i] == '(':
                result += ')'
            else:
                result += '('
        return result    

print(solution(input()))