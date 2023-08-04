import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

stk = []
stkMax = 0
ans = [0] * n

for idx, tow in enumerate(lst):
    # 첫 값만 예외처리
    if idx == 0:
        stkMax = tow
        stk.append(idx)
    # 내리막길이라면 바로 왼쪽 타워가 수신 지점, 스택에 push
    elif lst[idx - 1] > tow:
        ans[idx] = idx
        stk.append(idx)
    else:
        # 스택의 타워보다도 최대치가 더 높다면 바로 push하고 최대치 갱신
        if stkMax < tow:
            stkMax = tow
            stk.append(idx)
        else:
            while stk:
                # 스택을 하나씩 pop 하면서...
                pIdx = stk.pop()
                # 현재 위치보다 더 높은 타워가 발견되면 그 타워와 현재 타워를 같이 push하고 수신 지점 기록
                if lst[pIdx] > tow:
                    ans[idx] = pIdx + 1
                    stk.append(pIdx)
                    stk.append(idx)
                    break
for a in ans:
    print(a, end=' ')
print()