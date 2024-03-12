# https://www.acmicpc.net/problem/14888
# 292ms
# 10e9 이런 꼴의 숫자 표현은 float로 출력하므로 이를 주의할 것.
from collections import deque
from copy import deepcopy

def rand_oper(n,lst):
    if n == N-1:
        total_oper.append(lst)
        return
    prev = 0
    for i in range(N-1):
        if v[i] == 0 and prev != oper_lst[i]:
            v[i] = 1
            prev = oper_lst[i]
            rand_oper(n+1, lst+[oper_lst[i]])
            v[i] = 0

def simple_cal(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    else:
        if num1 < 0:
            num1 = (-1)*num1
            return (-1)*int(num1/num2)
        else:
            return int(num1/num2)

N = int(input())
num_lst = list(map(int,input().split()))
oper_num = list(map(int,input().split()))
oper_lst = []
for i in range(4):
    if i == 0:
        oper_lst += ['+'] * oper_num[i]
    elif i == 1:
        oper_lst += ['-'] * oper_num[i]
    elif i == 2:
        oper_lst += ['*'] * oper_num[i]
    else:
        oper_lst += ['/'] * oper_num[i]

v = [0 for _ in range(N-1)]
total_oper = []

mx = -10e9
mn = 10e9

rand_oper(0,[])
for i in range(len(total_oper)):
    now_op_lst = deque(total_oper[i])
    now_num_lst = deque(deepcopy(num_lst))
    for j in range(N-1):
        num1 = now_num_lst.popleft()
        num2 = now_num_lst.popleft()
        op = now_op_lst.popleft()
        tmp = simple_cal(num1,num2,op)
        now_num_lst.appendleft(tmp)
    else:
        if mx < tmp:
            mx = tmp
        if mn > tmp:
            mn = tmp
print(int(mx))
print(int(mn))