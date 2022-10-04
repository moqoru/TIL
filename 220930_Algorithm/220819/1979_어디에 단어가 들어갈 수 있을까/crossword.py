import sys
sys.stdin = open('input.txt')

def is_same(a, b):
    return 1 if a == b else 0                           # 두 값이 같으면 1, 다르면 0

t = int(input())

for cs in range(t):
    n, k = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst_tr = list(zip(*lst))                            # 세로 방향 탐색을 위해 전치 행렬을 만듦
    ans = 0                                             # 정답 개수 카운트

    for i in range(n):                                  # 한 행씩 탐색함
        cnt, cnt_tr = 0, 0                              # 원본행렬의 1의 개수, 전치행렬의 1의 개수

        for j in range(n):                              # 한 열씩 탐색하면서 1의 개수를 셈

            if lst[i][j] == 0:                          # 원본 행렬부터 탐색, 0이 나왔다면
                ans += is_same(cnt, k)                  # 직전까지 센 1의 길이가 k일 경우 정답 카운트가 1 증가
                cnt = 0                                 # 1의 길이 리셋
            else:                                       # 1이 나왔다면
                cnt += 1                                # 1의 길이를 늘려줌

            if lst_tr[i][j] == 0:                       # 전치행렬도 동일하게 탐색, 세로방향이라는 걸 제외하면 차이는 없음
                ans += is_same(cnt_tr, k)
                cnt_tr = 0
            else:
                cnt_tr += 1

        ans += is_same(cnt, k) + is_same(cnt_tr, k)     # 마지막 칸까지 셌을 때 1의 길이가 딱 맞는 경우가 있으므로,
                                                        # 정답 카운트 구문을 한번 더 적음
    print(f'#{cs + 1} {ans}')