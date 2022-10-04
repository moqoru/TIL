import sys
sys.stdin = open('sample_input(3).txt')

# 핵심 풀이 : 가로, 세로가 겹치지 않는 길이 n개의 좌표 순서쌍을 생성하여 각 케이스에 대해 합을 구하여 최소값을 갱신한다.
# permitation 함수로 p_lst에 n-1 까지의 정수를 한 번만 쓰는 순열을 1차원 리스트 형태로 생성한다.
# 이후 p_lst의 각 값에 대해 인덱스 위치는 lst의 행, 실제 값은 lst의 열을 가리키는 좌표로 변환한다.
# p_lst 예시 : [0, 3, 1, 2] => lst에서 (0, 0), (1, 3), (2, 1), (3, 2) 위치를 가리키게 된다.
# 이후 min_check 함수에서 각 위치의 합을 구하여 최소값을 갱신한다.

def min_check(lst, p_lst, min_sum):                             # 최소값 갱신 함수
    now_sum = 0                                                 # 현재 고른 위치들의 값의 총합

    for idx, val in enumerate(p_lst):                           # p_lst의 인덱스 위치, 해당 값을 좌표로 변환한다.
        now_sum += lst[idx][val]                                # lst에서 해당 좌표의 값을 읽어 모두 더한다.

    return now_sum if now_sum < min_sum else min_sum            # 현재까지의 최소값과 비교하여 갱신한 값을 리턴한다.

def permitation(n, lst, p_lst, min_sum):                        # 순열을 구하는 함수

    if len(p_lst) == n:                                         # 생성한 순열의 길이가 맞다면
        min_sum = min_check(lst, p_lst, min_sum)                # 함수 호출로 최소값을 갱신해서 받아 온다.

    else:                                                       # 아직 순열 생성이 덜 끝났다면
        for i in range(n):                                      # n-1까지의 숫자 중 하나를 지금까지 만든 순열 끝에 숫자 1개씩 추가
            if i not in p_lst:                                  # 겹치는 숫자가 없는지 체크가 끝났다면
                p_lst.append(i)                                 # p_lst에 append로 1개씩 추가한다.
                min_sum = permitation(n, lst, p_lst, min_sum)   # 재귀함수로 순열 함수를 다시 호출, 최소값을 받아 와야 최종적으로 함수가 다 끝날 때 리턴할 수 있다.
                p_lst.pop()                                     # 탐색이 끝나면 다시 pop 해서 다음 순열의 경우의 수를 체크할 수 있게 한다.

    return min_sum                                              # 받아온 최소값을 리턴해 준다.

t = int(input())
for cs in range(t):

    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    ans = permitation(n, lst, [], 9 * n + 1)                    # 판의 크기, 숫자 판에 기록된 정보, 순열을 저장할 리스트, 최소값의 초기값을 넣어 호출
                                                                # 초기값은 판 전체에 9만 적혀있을 경우(= 최악의 경우) 나오는 값보다 더 크게 지정해 준다.
    print(f'#{cs + 1} {ans}')                                   # 리턴받아 온 최소값을 출력