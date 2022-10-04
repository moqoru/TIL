import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")

def one_by_one(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a - b
    elif operator == 2:
        return a * b
    # 나눗셈만 경우의 수가 3가지나 됨. 먼저 0으로 나눌 경우는 연산 불가 처리
    elif b == 0:
        return None
    # 앞쪽 숫자가 음수일 경우 문제의 조건대로 처리
    elif a < 0: # -1 // 3을 연산하면 원래는 -1이 나오지만 문제상으로는 0이 나와야 함.
        return -a // b * -1
    else:
        return a // b

def overall(depth, prev_result):
    if depth >= n - 1:
        global ans_min, ans_max
        ans_min, ans_max = min(ans_min, prev_result), max(ans_max, prev_result)
    else:
        for i in range(4):
            # 해당 연산자를 쓸 수 있을 경우에만 연산 진행
            if opers[i]:
                opers[i] -= 1
                now_result = one_by_one(prev_result, nums[depth + 1], i)
                # 0으로 나눈 경우를 제외하고 출력
                if now_result != None:
                    overall(depth + 1, now_result)
                opers[i] += 1

n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
ans_min, ans_max = 100 ** n + 1, -(100 ** n + 1) # 나올 수 있는 가장 큰, 작은 숫자?
overall(0, nums[0])
print(ans_max, ans_min)