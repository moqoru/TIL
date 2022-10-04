import sys
sys.stdin = open('sample_input.txt')

# 풀이 핵심 : nxn인 판에 n개의 퀸을 올려놓는 것이므로, 각 가로줄과 세로줄에는 각각 1개씩의 퀸을 놓을 수밖에 없다.
# 2차원 행렬에서 각 행마다 퀸을 1개씩 올려두고 열끼리 겹치는지, 대각선끼리 겹치는지 체크한다.
# 1차원 리스트 순열을 생성하면 가로와 세로가 겹치지 않는 퀸의 배치를 만들 수 있다.
# place 리스트의 인덱스 번호를 가로 좌표, 그 위치의 값을 세로 좌표가 되게 배치한다.
# 예시 [2, 0, 3, 1] => 퀸을 각각 (0, 2), (1, 0), (2, 3), (3, 1)에 배치한 것으로 생각한다.

def crosscheck(n, place):                                   # 대각선끼리 겹치는지 확인하는 함수

    flag = True                                             # 대각선 겹침 여부 체크 변수
    for i in range(n):                                      # i는 리스트의 전 원소를 순회
        for j in range(i + 1, n):                           # j는 i번 다음 번째 원소부터 순회

            x1, y1 = i, place[i]                            # 리스트의 i, j 인덱스와 기록된 값을 x, y 좌표에 대응시킨다.
            x2, y2 = j, place[j]

            if x2 - x1 == y2 - y1 or x2 - x1 == y1 - y2:    # x좌표의 차이와 y 좌표의 차이가 일치하면 같은 대각선상에 있는 것이다.
                flag = False
                break

        if not flag:
            break

    return 1 if flag else 0                                 # 대각선으로 겹치지 않으면 1, 아니면 0을 리턴한다.

def permutation(n, place):                                  # 순열을 만드는 함수, n은 크기, place는 만든 순열

    ans = 0                                                 # ans는 재귀함수를 호출하는 동안 쭉 해답 가짓수를 받아와 저장함

    if len(place) == n:                                     # 길이에 맞게 순열을 완성했다면
        ans += crosscheck(n, place)                         # 대각선 겹침 여부를 판정하고 안 겹치면 정답 가짓수가 1 늘어남

    else:                                                   # 아래 구문은 for문을 n개 중첩한 것을 재귀함수로 만든 것과 같다.
        for i in range(n):                                  # n까지의 모든 숫자에 대해 루프
            if i not in place:                              # 겹치지 않는 숫자라면
                place.append(i)                             # 리스트 맨 뒤에 숫자를 넣어준 뒤
                ans += permutation(n, place)                # 재귀함수 호출, 정답 가짓수를 받아오는 구문까지 같이 적음
                place.pop()                                 # 다시 빼서 다음 순열의 경우의 수를 고려함

    return ans                                              # 정답 가짓수를 리턴해 줌

t = int(input())
for cs in range(t):

    n = int(input())
    print(f'#{cs + 1} {permutation(n, [])}')



